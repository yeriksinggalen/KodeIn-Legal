# KodeIn Legal & Support

Public legal documents for the KodeIn Android application (`com.yerik.kodein`), developed by Yerik Afrianto Singgalen.

Contact: [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com).

## Public links

| Document | URL |
| --- | --- |
| Privacy Policy | [Privacy Policy](https://yeriksinggalen.github.io/KodeIn-Legal/privacy-policy.html) |
| Terms of Service | [Terms of Service](https://yeriksinggalen.github.io/KodeIn-Legal/terms-of-service.html) |
| Account & Data Deletion | [Account & Data Deletion](https://yeriksinggalen.github.io/KodeIn-Legal/account-deletion.html) |
| Licenses | [Licenses](https://yeriksinggalen.github.io/KodeIn-Legal/licenses.html) |
| Support | [Contact & Support](https://yeriksinggalen.github.io/KodeIn-Legal/support.html) |

Use the Privacy Policy URL in Play Console's privacy policy field and the Account & Data Deletion URL in the account deletion field. No account or app installation is required to read these pages or initiate an email request.

## Android integration

`LegalLinks.kt` in the KodeIn application defines these URLs. Settings → Application links to all five pages. Registration provides clickable privacy and terms links in the required consent text. Login contains authentication controls; deletion and support remain available in Settings. Settings → Session contains the actual in-app deletion control in KodeIn 1.1.0.

## Maintenance

GitHub Pages publishes `docs/` from `main`. The site uses Jekyll, a custom accessible layout and local CSS, without analytics, cookies, external scripts or a public personal-data form.

Edit policy source in `scripts/write_documents.py`, then run it to regenerate bilingual pages and root Markdown. Edit `docs/licenses.md` for license presentation; use `scripts/generate_notices.py` with a current release runtime dependency report and a directory containing Maven POM files to regenerate dependency notices. Keep root Markdown links pointing to the public site and dates in the layout consistent.

Cloudinary image destruction requires administrative action; never put provider API secrets into the Android client. Monitor the published support mailbox and process verified account/data requests. See [Play Console guide](PLAY_CONSOLE_GUIDE.md).
