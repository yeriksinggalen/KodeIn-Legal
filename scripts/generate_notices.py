"""Extract release runtime license metadata from Gradle's report and cached POMs.
Usage: python3 scripts/generate_notices.py <release-dependencies.txt> <Gradle cache>
Run ./gradlew :app:dependencies --configuration releaseRuntimeClasspath first.
"""
import csv
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
report = Path(sys.argv[1]).read_text()
cache = Path(sys.argv[2])
coordinates = set()
for line in report.splitlines():
    if line.endswith('(c)'):
        continue
    match = re.search(r'([\w.-]+):([\w.-]+):([^\s]+)(?: -> ([^\s]+))?', line)
    if not match:
        continue
    group, artifact, version, replacement = match.groups()
    if replacement:
        if ':' in replacement:
            group, artifact, version = replacement.split(':')
        else:
            version = replacement
    coordinates.add((group, artifact, version))
ns = {'m': 'http://maven.apache.org/POM/4.0.0'}

def metadata(coord, seen=None):
    seen = seen or set()
    if coord in seen:
        return [], ''
    seen.add(coord)
    poms = list((cache / coord[0] / coord[1] / coord[2]).glob('*/*.pom'))
    if not poms:
        return [], ''
    pom = ET.parse(poms[0]).getroot()
    licenses = [(l.findtext('m:name', '', ns), l.findtext('m:url', '', ns)) for l in pom.findall('m:licenses/m:license', ns)]
    url = pom.findtext('m:url', '', ns)
    if not licenses:
        parent = pom.find('m:parent', ns)
        if parent is not None:
            pcoord = tuple(parent.findtext('m:' + key, '', ns) for key in ['groupId', 'artifactId', 'version'])
            licenses, parent_url = metadata(pcoord, seen)
            url = url or parent_url
    return licenses, url

# Official upstream fallbacks for POMs without license metadata.
fallbacks = {
    'javax.inject:javax.inject:1': ([('Apache License 2.0', 'https://github.com/javax-inject/javax-inject/blob/master/src/javax/inject/Inject.java')], 'https://github.com/javax-inject/javax-inject'),
    'org.bouncycastle:bcprov-jdk15to18:1.72': ([('Bouncy Castle License (MIT)', 'https://github.com/bcgit/bc-java/blob/r1rv72/LICENSE.html')], 'https://github.com/bcgit/bc-java'),
    'org.bouncycastle:bcutil-jdk15to18:1.72': ([('Bouncy Castle License (MIT)', 'https://github.com/bcgit/bc-java/blob/r1rv72/LICENSE.html')], 'https://github.com/bcgit/bc-java'),
}
rows = []
for coord in sorted(coordinates):
    licenses, url = metadata(coord)
    if not licenses and ':'.join(coord) in fallbacks:
        licenses, url = fallbacks[':'.join(coord)]
    rows.append((':'.join(coord), '; '.join(n for n, _ in licenses) or 'See provider terms / POM has no license declaration', '; '.join(u for _, u in licenses), url))
with (root / 'DEPENDENCY_LICENSES.csv').open('w') as f:
    writer = csv.writer(f)
    writer.writerow(['coordinate', 'license', 'license_url', 'project_url'])
    writer.writerows(rows)
body = 'License declarations from the resolved KodeIn 1.1.0 release runtime dependencies and their Maven POMs, supplemented with official upstream licenses where a POM has no declaration (11 October 2026). Constraints are omitted. POM metadata is not a substitute for license text, required upstream notices, or proprietary SDK terms.\n\n'
body += '| Dependency | Declared license | License source |\n| --- | --- | --- |\n'
for coord, license_name, license_urls, url in rows:
    links = ' · '.join(f'[License]({u})' for u in license_urls.split('; ') if u.startswith('http'))
    links = links or (f'[Provider]({url})' if url.startswith('http') else 'Provider SDK terms apply; consult upstream package')
    body += f'| `{coord}` | {license_name.replace("|", "/")} | {links} |\n'
(root / 'THIRD_PARTY_NOTICES.md').write_text('# Third-party dependency notices\n\n' + body)
(root / 'docs/third-party-notices.md').write_text('---\ntitle: "Third-party dependency notices"\npermalink: /third-party-notices.html\n---\n\n' + body)
print(f'Extracted {len(rows)} dependency declarations; {sum("no license" in r[1] for r in rows)} use provider terms.')
