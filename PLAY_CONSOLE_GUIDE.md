# KodeIn Play Console guide

Implementation snapshot: 11 October 2026, local KodeIn 1.1.0. This is a developer checklist, not a completed Play Console submission or an assurance of approval.

## URLs to enter

- Privacy policy: https://yeriksinggalen.github.io/KodeIn-Legal/privacy-policy.html
- Account deletion: https://yeriksinggalen.github.io/KodeIn-Legal/account-deletion.html
- Support email: singgalen.yerik@gmail.com
- App identity: KodeIn, package `com.yerik.kodein`; developer identified in policy as Yerik Afrianto Singgalen. Match the actual store listing.

## Data safety evidence

Review the actual release APK and the current form before submitting. Google defines collection/sharing separately; transfer to a service provider can have a sharing exception but can still be collection. Do not mark all data as uncollected merely because the app has no advertising.

| Implementation | Data to assess in current form | Purpose / optionality |
| --- | --- | --- |
| Firebase Auth and Firestore profile | Name, email, user IDs, optional professional profile information | Account management, app functionality; profile extras optional |
| Cloud Firestore research records | User-provided text/documents and other content, which may themselves contain personal/sensitive information | App functionality and cloud synchronization |
| Cloudinary uploads | Photos/images and image identifiers/metadata | Optional profile/workspace functionality |
| Scopus requests | User-supplied API credential, code/category/theme labels, filters | Optional literature retrieval; excerpt text stays local |
| Android document/photo pickers | Only selected user files/images | Import and optional upload |
| Provider SDK technical operation | Assess IP/request/device diagnostics under current Firebase, Google Identity and ML Kit disclosures | Provider operation/security; inspect actual release dependencies |
| User-initiated exports | CSV/PDF/DOCX and backup files | User-selected file creation/sharing; assess applicable exclusions |

No advertising SDK, Firebase Analytics or Crashlytics dependency is currently configured. Auto-coding/ranking runs locally. No contact/location/microphone/camera runtime permission is declared. Do not infer that all SDK technical collection is absent from these facts.

## Deletion operations

The app has an in-app deletion control and a public page with an email request route. The developer must monitor and fulfill requests, including users who cannot reinstall the app. Verify ownership using minimum information, never passwords or API keys.

In-app deletion covers owned Firestore projects/subcollections, profile and Firebase Auth. Cloudinary assets require administrative destruction. Look up all associated assets, including previous profile photos and orphaned uploads, before removing the metadata needed to identify them. Use authenticated server/admin tooling; do not put a Cloudinary secret in the APK. The policies do not promise an automated image deletion backend.

The client checks for a recent sign-in before starting research-data removal. Deletion spans several requests, so failures can leave partial deletion; retry/support must finish remaining records. Verify in an isolated Firebase environment, never by deleting a real research account as a test.

Users clear app storage on their devices and manage exported copies. Trash has a 30-day recovery expiry but is purged on related app operations, not by an installed server scheduler. Provider log/backup cycles can differ.

## Before store submission

- Verify each public URL loads anonymously over HTTPS and the support mailbox works.
- Ship an APK/AAB containing the connected legal menus and deletion flow. Editing source or installing a debug build does not update the production listing.
- Complete Data safety, target audience and any other Play Console forms from release behavior; these forms are not submitted by this repository.
- Check current deployed Firestore rules, provider storage settings and administrative image deletion handling.
- Keep license notices aligned with release dependency changes.

Primary guidance: [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311), [Account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111), [Data safety form](https://support.google.com/googleplay/android-developer/answer/10787469).
