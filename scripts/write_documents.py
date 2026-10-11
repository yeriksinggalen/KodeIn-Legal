from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://yeriksinggalen.github.io/KodeIn-Legal'
EMAIL = 'singgalen.yerik@gmail.com'

def page(filename, title, body, rootfile=None):
    (ROOT / 'docs' / filename).write_text(f'---\ntitle: "{title}"\npermalink: /{filename[:-3]}.html\n---\n\n' + body.strip() + '\n')
    if rootfile:
        public_body = body.strip()
        for name in ['privacy-policy', 'terms-of-service', 'account-deletion', 'licenses', 'support']:
            public_body = public_body.replace(f']({name}.html)', f']({BASE}/{name}.html)')
        (ROOT / rootfile).write_text(f'# {title}\n\n' + public_body + '\n')

page('privacy-policy.md', 'Kebijakan Privasi / Privacy Policy', '''
**Aplikasi / Application:** KodeIn (`com.yerik.kodein`)  
**Pengembang / Developer:** Yerik Afrianto Singgalen  
**Berlaku dan diperbarui / Effective and updated:** 11 October 2026  
**Kontak privasi / Privacy contact:** [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com)

[Bahasa Indonesia](#bahasa-indonesia) · [English](#english) · [Penghapusan akun / Account deletion](account-deletion.html)

## Bahasa Indonesia

### 1. Ruang lingkup
KodeIn membantu peneliti mengelola proyek, transkrip, coding kualitatif, literatur, visualisasi, dan laporan. Kebijakan ini menjelaskan pemrosesan data dalam aplikasi Android KodeIn. Pengembang bertanggung jawab atas pemrosesan data untuk operasional layanan; peneliti tetap bertanggung jawab atas dasar pemrosesan data peserta penelitian yang dimasukkan ke aplikasi.

### 2. Data yang diproses dan tujuannya

| Jenis data | Tujuan |
| --- | --- |
| ID akun Firebase, email, nama, informasi autentikasi, waktu pembuatan akun dan login | Pendaftaran, masuk, pemulihan akun, keamanan, dan pengaitan ruang kerja dengan pemiliknya. Password dikelola Firebase Authentication, bukan disimpan sebagai teks biasa oleh KodeIn. |
| Profil yang Anda isi: peran, bio, institusi/afiliasi, foto dan metadata foto | Menampilkan identitas peneliti dan preferensi profil. Foto bersifat opsional. |
| Metadata proyek, transkrip, segmen, kode, kategori, tema, keputusan/review coding, memo, catatan audit, literatur, dan catatan peneliti | Penyimpanan dan sinkronisasi penelitian, coding, pencarian, analisis, pelacakan keputusan, dan pembuatan laporan. Data ini dapat memuat informasi pribadi/sensitif jika Anda memasukkannya. |
| Gambar ruang kerja yang Anda pilih dan metadata gambar | Menampilkan gambar proyek yang Anda tambahkan secara sukarela. |
| Draft lokal, cache offline, preferensi bahasa/tampilan, dan pengaturan literatur | Mempertahankan pekerjaan dan menyediakan akses offline. |
| Kunci API Scopus, label kode, nama kategori/tema relevan, dan filter pencarian | Mengambil metadata literatur melalui layanan Elsevier yang Anda aktifkan. |
| Isi email dukungan/penghapusan yang Anda kirim | Menangani pertanyaan, verifikasi kepemilikan akun, dan permintaan hak privasi. |

KodeIn menggunakan pemilih dokumen/foto Android untuk mengakses file yang Anda pilih. Aplikasi saat ini tidak meminta akses kontak, lokasi, mikrofon, atau izin kamera, tidak memasang SDK iklan, dan tidak memasang Firebase Analytics/Crashlytics. Penyedia autentikasi, penyimpanan, hosting, dan API dapat memproses informasi teknis seperti alamat IP dan log permintaan untuk menjalankan serta mengamankan layanan mereka.

### 3. Penyedia layanan dan penerima data

- **Google/Firebase Authentication:** autentikasi email/password dan Google. Login Google menyediakan identitas akun yang digunakan untuk masuk.
- **Google Cloud Firestore:** profil dan ruang kerja penelitian tersimpan di cloud; SDK juga menyimpan cache persisten pada perangkat untuk akses offline. Pengaturan akses aplikasi membatasi proyek kepada akun pemilik; versi ini tidak menyediakan keanggotaan proyek atau kolaborasi multi-pengguna.
- **Cloudinary:** menerima foto profil/gambar proyek yang Anda unggah. Gambar menggunakan URL HTTPS yang dapat diakses oleh orang yang mengetahui URL; jangan unggah gambar sensitif atau gambar peserta yang belum mendapat izin.
- **Elsevier Scopus (opsional):** menerima kunci API Anda, label kode, nama kategori/tema relevan, dan filter. Potongan transkrip serta istilah ranking yang diturunkan dari potongan transkrip tidak dikirim ke Scopus. Karena label kode bisa mengandung informasi sensitif, gunakan label yang sudah dide-identifikasi. Kunci API disimpan dalam preferensi terenkripsi pada perangkat dan tidak dimasukkan ke snapshot cloud maupun backup proyek.
- **Ekspor yang Anda pilih:** laporan CSV/PDF/DOCX dan backup tersimpan ke lokasi yang Anda pilih. Penerima file yang Anda bagikan berada di bawah kendali Anda.

Kami tidak menjual data pribadi atau data penelitian dan tidak menggunakannya untuk iklan. Pengungkapan dapat diperlukan untuk menjalankan layanan, menindaklanjuti permintaan Anda, atau memenuhi kewajiban hukum yang berlaku. Layanan pihak ketiga dapat memproses data di negara lain sesuai konfigurasi dan infrastruktur mereka; KodeIn tidak menjamin bahwa seluruh data tinggal di Indonesia.

Kebijakan penyedia: [Google](https://policies.google.com/privacy), [Firebase](https://firebase.google.com/support/privacy), [Cloudinary](https://cloudinary.com/privacy), dan [Elsevier](https://www.elsevier.com/legal/privacy-policy).

### 4. Penyimpanan dan penghapusan
Data akun dan ruang kerja disimpan selama akun/proyek digunakan, sampai Anda menghapusnya atau mengajukan penghapusan. Transkrip yang dipindah ke Trash memiliki masa pemulihan 30 hari; pembersihan item kedaluwarsa dijalankan saat fitur aplikasi yang terkait diakses, sehingga tidak ada jaminan penghapusan terjadwal tepat pada hari ke-30. Anda dapat menghapusnya permanen lebih awal. Catatan audit terkait tetap mengikuti umur proyek sampai proyek/akun dihapus.

Penghapusan akun dalam aplikasi menghapus ruang kerja Firestore milik akun, koleksi penelitian di dalamnya, dokumen profil, dan akun Firebase Authentication. Proses membutuhkan koneksi internet dan login baru; operasi bertahap dapat gagal sebagian sehingga perlu dicoba kembali atau dibantu melalui email.

**Gambar Cloudinary tidak otomatis dimusnahkan oleh tombol hapus akun.** Penghapusan gambar dilakukan secara administratif melalui [permintaan penghapusan](account-deletion.html). Foto lama atau unggahan yang belum berhasil terhubung ke profil/proyek juga mungkin membutuhkan penelusuran administratif. Cache pada perangkat lain, draft lokal, kunci API, backup, dan laporan yang telah diekspor tidak otomatis dihapus dari semua lokasi. Setelah menghapus akun, hapus penyimpanan aplikasi melalui pengaturan Android di perangkat Anda dan kelola salinan ekspor/backup Anda sendiri.

Jika data tertentu harus dipertahankan karena kewajiban hukum yang benar-benar berlaku atau penanganan sengketa/keamanan, kami akan menjelaskan alasan, lingkup, serta masa penyimpanannya ketika menangani permintaan sejauh diizinkan hukum. Infrastruktur penyedia dapat memiliki log, backup, atau cache yang dihapus mengikuti siklus penyedia; kami tidak menjanjikan pemusnahan seketika atas seluruh salinan infrastruktur.

### 5. Hak dan pilihan Anda
Anda dapat mengubah profil di Pengaturan, mengekspor data melalui fitur aplikasi, menghapus proyek/transkrip, menonaktifkan integrasi opsional dengan menghapus kunci API atau penyimpanan aplikasi, dan meminta akses, koreksi, penghapusan, atau penanganan keberatan/pembatasan pemrosesan sesuai hak yang berlaku. Kirim permintaan ke [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com). Kami hanya meminta informasi yang diperlukan untuk memverifikasi kepemilikan dan menjalankan permintaan; jangan kirim password, token, kunci API, atau transkrip peserta.

### 6. Keamanan dan penelitian sensitif
Komunikasi layanan menggunakan HTTPS; preferensi kunci Scopus menggunakan penyimpanan terenkripsi. Cache/draft dan file ekspor tidak semuanya menggunakan enkripsi khusus aplikasi. Tidak ada sistem yang dapat menjamin keamanan absolut. Gunakan perangkat terlindungi, minimalkan data pribadi, lakukan de-identifikasi, dan ikuti persetujuan peserta, aturan etik, serta kebijakan institusi Anda sebelum memasukkan data ke layanan cloud.

Auto-coding dan ranking literatur saat ini dilakukan dengan logika aplikasi/lokal, bukan mengirim transkrip ke layanan AI generatif eksternal. Hasil otomatis memerlukan pemeriksaan peneliti.

### 7. Anak dan perubahan kebijakan
KodeIn ditujukan untuk kegiatan penelitian, bukan layanan yang ditujukan kepada anak di bawah 13 tahun. Hubungi kami jika Anda mengetahui data anak dikirim tanpa dasar yang sesuai. Penelitian yang melibatkan anak tetap memerlukan kewenangan, persetujuan, dan perlindungan yang sesuai dari peneliti. Kebijakan dapat diperbarui; tanggal pembaruan tercantum di halaman ini. Perubahan material akan diinformasikan melalui aplikasi atau sarana komunikasi layanan yang tersedia.

## English

### Scope, data and purposes
KodeIn is an Android tool for qualitative research projects, transcripts, coding, literature, visualization and reports, developed by **Yerik Afrianto Singgalen**. The developer handles data for operating the service; researchers are responsible for the lawful processing of participant data they supply.

We process Firebase account identifiers, email, name, authentication information, account creation/login times; optional profile role, biography, institution, photo and photo metadata; project metadata, transcripts, segments, codes, categories, themes, coding/review decisions, memos, audit records, literature and researcher notes; optional workspace images; local drafts, offline caches and preferences; optional Scopus credentials and search inputs; and support/deletion correspondence. Purposes are authentication, recovery/security, ownership and synchronization, research analysis and reporting, optional literature retrieval, and handling your requests. Firebase Authentication manages passwords; KodeIn does not store them in plain text.

The app reads documents/images selected through Android pickers. This version does not request contacts, location, microphone or camera permissions, include advertising SDKs, or integrate Firebase Analytics/Crashlytics. Providers may process IP addresses and technical request logs to operate and secure their services.

### Providers, sharing and transfers
Firebase Authentication supports email/password and Google sign-in. Cloud Firestore stores profiles and research workspaces and maintains a persistent offline device cache. Projects are limited to the owning account; there is no project membership or multi-user collaboration in this version.

Cloudinary receives optional uploaded profile/workspace images. Images have HTTPS URLs accessible to people who know the URL; avoid sensitive or unauthorized participant images. Optional Elsevier Scopus requests include your API key, code labels, relevant category/theme names and filters. Transcript excerpts and excerpt-derived ranking terms are not sent to Scopus. De-identify labels before using this integration. Credentials are stored in encrypted device preferences and excluded from project cloud snapshots/backups.

Exports and backups are saved to locations you choose; you control sharing. We do not sell personal/research data or use it for advertising. Disclosure may occur to operate the service, fulfill your requests or comply with applicable legal obligations. Providers may process data across countries; we do not promise Indonesia-only storage. See [Google](https://policies.google.com/privacy), [Firebase](https://firebase.google.com/support/privacy), [Cloudinary](https://cloudinary.com/privacy) and [Elsevier](https://www.elsevier.com/legal/privacy-policy) policies.

### Retention and deletion
Account/workspace data remains while used, until deletion or a deletion request. Trash transcripts have a 30-day recovery period; expired records are purged when related app features run, rather than by a guaranteed day-30 server schedule. Permanent deletion is available sooner. Audit records remain with the project until project/account deletion.

In-app account deletion removes owned Firestore workspaces and their research collections, the profile document and Firebase Authentication account. It requires internet and a fresh sign-in. The sequence can partially fail; retry or contact support.

**Cloudinary images are not automatically destroyed by the in-app account deletion button.** Request administrative removal using the [deletion page](account-deletion.html), including old/unlinked uploads when relevant. Other-device caches, local drafts, API keys and exported backups/reports are not automatically removed everywhere. Clear KodeIn storage through Android Settings on your devices after deletion and manage exported copies yourself.

If an actual legal obligation or security/dispute need requires limited retention, we will explain the scope, reason and duration when handling your request where legally allowed. Provider infrastructure logs, backups and caches follow provider removal cycles; immediate erasure of every infrastructure copy is not promised.

### Your choices and security
Edit your profile, export records, delete projects/transcripts, remove optional API credentials or app storage, or request access, correction, deletion, restriction/objection handling as applicable by emailing [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com). We request only information needed for ownership verification and fulfillment. Never send passwords, tokens, API keys or participant transcripts.

Service traffic uses HTTPS and Scopus credential preferences are encrypted. Drafts/caches and exports do not all have app-specific encryption. Protect devices, minimize and de-identify data, and satisfy participant consent, institutional ethics and applicable requirements before cloud upload. No system guarantees absolute security. Current auto-coding and literature ranking use app/local logic and do not transmit transcripts to an external generative AI service; researchers must review results.

KodeIn is intended for research, not directed at children under 13. Contact us about unauthorized child data; researchers working with children still need appropriate authority, consent and protections. Updates carry a revised date; material changes will be communicated through available app/service channels.
''', 'PRIVACY_POLICY.md')

page('terms-of-service.md', 'Syarat Layanan / Terms of Service', '''
**KodeIn · Yerik Afrianto Singgalen · Effective / Berlaku: 11 October 2026**  
**Contact:** [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com)

[Bahasa Indonesia](#bahasa-indonesia) · [English](#english) · [Privacy Policy](privacy-policy.html)

## Bahasa Indonesia

### 1. Layanan dan persetujuan
KodeIn adalah alat bantu coding dan analisis penelitian kualitatif. Dengan membuat akun atau menggunakan layanan, Anda menerima syarat ini dan memahami [Kebijakan Privasi](privacy-policy.html). Jika tidak setuju, hentikan penggunaan dan gunakan jalur ekspor/penghapusan yang tersedia. Persetujuan syarat ini tidak menggantikan persetujuan peserta penelitian.

### 2. Akun
Gunakan informasi akun yang benar, lindungi kredensial dan perangkat, serta laporkan dugaan akses tanpa izin. Anda bertanggung jawab atas aktivitas akun yang Anda kendalikan. Jangan menggunakan akun orang lain tanpa izin. KodeIn bukan layanan yang ditujukan kepada anak di bawah 13 tahun; Anda harus memiliki kapasitas hukum untuk menerima syarat atau izin pihak yang berwenang jika diwajibkan.

### 3. Data penelitian dan hak Anda
Anda mempertahankan hak atas data dan materi penelitian Anda. Anda memberi izin terbatas kepada pengembang dan penyedia operasional untuk menyimpan, memproses, menampilkan, serta mentransmisikan materi tersebut hanya untuk menjalankan fitur layanan dan permintaan Anda, sesuai Kebijakan Privasi. Izin ini tidak memberikan hak untuk menjual data penelitian Anda.

Anda harus memiliki kewenangan dan dasar yang sesuai untuk mengunggah transkrip, gambar, artikel, atau informasi peserta. Penuhi persetujuan, kerahasiaan, etik penelitian, hak cipta, dan kebijakan institusi yang berlaku. Hapus identitas yang tidak diperlukan dan jangan memasukkan rahasia/identitas sensitif yang tidak layak disimpan pada layanan ini.

### 4. Penggunaan yang dilarang
Jangan memakai KodeIn untuk aktivitas melanggar hukum, melanggar hak orang lain, mengunggah materi tanpa izin, menyebarkan malware, mencoba mengakses data akun lain, membocorkan kredensial, atau mengganggu keamanan dan ketersediaan layanan. Jangan menyajikan hasil otomatis sebagai temuan yang telah diverifikasi tanpa pemeriksaan metodologis.

### 5. Hasil analisis dan layanan pihak ketiga
Auto-coding, pencarian, frekuensi, visualisasi, rekomendasi literatur, dan ringkasan laporan adalah alat bantu. Periksa kutipan, konteks, keputusan coding, hasil berlawanan, sumber asli dan sitasi. Frekuensi bukan bukti mandiri tentang signifikansi tema. Metadata/rationale relevansi artikel bukan pengganti pembacaan dan verifikasi temuan artikel.

Firebase/Google, Cloudinary dan Elsevier memiliki ketentuan masing-masing. Anda bertanggung jawab atas hak akses/kunci API Scopus dan kepatuhan terhadap lisensi metadata/artikel. KodeIn tidak menjanjikan akses penuh artikel berbayar, hasil tertentu, atau ketersediaan layanan pihak ketiga. Setiap biaya penyedia/internet yang Anda aktifkan berada di bawah ketentuan penyedia tersebut.

### 6. Lisensi aplikasi
Pengembang mempertahankan hak atas kode, identitas dan desain KodeIn, dengan pengecualian komponen pihak ketiga yang mengikuti lisensinya sendiri. Anda memperoleh izin terbatas untuk menggunakan aplikasi sesuai syarat ini. Anda tidak memperoleh kepemilikan perangkat lunak. Hak yang secara wajib diberikan oleh hukum atau lisensi open-source tetap berlaku. Lihat [Lisensi dan pemberitahuan pihak ketiga](licenses.html).

### 7. Ketersediaan, tanggung jawab dan backup
Layanan diberikan sesuai kondisi dan ketersediaannya sejauh hukum mengizinkan. Kami tidak menjamin operasi tanpa gangguan, kesalahan, kehilangan data, atau bahwa hasil sesuai setiap tujuan penelitian. Simpan backup, periksa sinkronisasi dan ekspor sebelum menghapus akun/proyek.

Sejauh diizinkan hukum, pengembang tidak bertanggung jawab atas kerugian tidak langsung akibat gangguan pihak ketiga, penggunaan yang melanggar syarat, atau keputusan penelitian berdasarkan hasil yang tidak diverifikasi. Syarat ini tidak membatasi hak konsumen wajib, tanggung jawab yang tidak dapat dikecualikan, atau kewajiban pengembang berdasarkan hukum yang berlaku.

### 8. Pengakhiran dan penghapusan
Anda dapat berhenti menggunakan layanan dan [menghapus akun/data](account-deletion.html). Penghapusan bersifat permanen untuk data yang berhasil dihapus; file ekspor dan gambar Cloudinary memiliki langkah penanganan tersendiri yang dijelaskan di halaman penghapusan. Akses dapat dibatasi untuk pelanggaran syarat, keamanan, atau kewajiban hukum; kami akan memberikan pemberitahuan dan bantuan pemulihan/ekspor bila layak dan diizinkan.

### 9. Perubahan, hukum dan kontak
Perubahan material akan diberitahukan melalui kanal layanan yang tersedia, dengan tanggal baru pada halaman ini. Hukum yang berlaku ditentukan menurut ketentuan wajib pada yurisdiksi yang relevan; syarat ini tidak menghapus perlindungan wajib pengguna. Hubungi [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com) untuk pertanyaan atau penyelesaian masalah terlebih dahulu.

## English

### Agreement and accounts
KodeIn is a qualitative coding/research tool by **Yerik Afrianto Singgalen**. Creating an account or using the service means accepting these terms and understanding the [Privacy Policy](privacy-policy.html). If you disagree, stop using it and use available export/deletion routes. This agreement does not replace participant consent.

Provide accurate account information, protect credentials/devices, and report unauthorized access. You are responsible for activity under your control and must not use another person's account without authorization. The service is not directed at children under 13; have legal capacity or required authorization to agree.

### Your content and acceptable use
You retain rights to your research content. You authorize limited storage, processing, display and transmission by the developer/operational providers to deliver features and fulfill your requests under the Privacy Policy, without a right to sell your research data. Obtain the necessary permissions, lawful basis, ethics approvals, confidentiality safeguards and copyright rights before supplying transcripts, images, articles or participant information. De-identify unnecessary identifiers and avoid unsuitable secrets/sensitive identities.

Do not break laws, infringe rights, upload unauthorized material/malware, access others' data, disclose credentials or disrupt the service. Do not portray unverified automated output as verified research findings.

### Research outputs and third parties
Auto-coding, search, frequencies, charts, literature recommendations and report summaries are aids requiring review of evidence, context, decisions, contrary cases, original sources and citations. Frequency alone does not establish thematic significance. Metadata/relevance rationales do not replace reading and verifying article findings.

Firebase/Google, Cloudinary and Elsevier have separate terms. Maintain authorized Scopus API access and comply with metadata/article licenses. Full-text access, specific research outcomes and third-party uptime are not guaranteed. Provider/internet charges you activate follow their terms.

### Software rights, availability and responsibility
The developer retains KodeIn software/brand/design rights, subject to third-party component licenses. You receive limited permission to use the app under these terms, not software ownership. Mandatory legal and open-source rights are preserved; see [Licenses](licenses.html).

The service is provided as available to the extent law permits, without guarantees of uninterrupted/error-free operation, prevention of data loss or fitness for every research purpose. Keep backups and check synchronization/exports before deletion. To the extent legally permitted, the developer is not liable for indirect loss from third-party outages, misuse or decisions based on unverified results. Mandatory consumer rights, non-excludable liabilities and developer obligations remain unaffected.

### Ending use, changes and contact
You may stop using the service and [delete your account/data](account-deletion.html). Completed deletion is permanent; exports and Cloudinary images require the separate steps explained there. Access may be restricted for violations, security or legal obligations, with notice and recovery/export assistance where appropriate and allowed.

Material updates will be announced through available service channels and dated here. Applicable law follows mandatory requirements of relevant jurisdictions; mandatory protections remain intact. Contact [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com) first to discuss questions or problems.
''', 'TERMS_OF_SERVICE.md')

page('account-deletion.md', 'Penghapusan Akun & Data / Account & Data Deletion', '''
**KodeIn (`com.yerik.kodein`) · Developer: Yerik Afrianto Singgalen**  
**Updated: 11 October 2026**

## Minta penghapusan tanpa aplikasi / Request deletion without the app

Anda dapat meminta penghapusan akun dan data terkait tanpa memasang ulang KodeIn, tanpa akun GitHub, dan tanpa formulir publik.  
You can request account and associated data deletion without reinstalling KodeIn, a GitHub account or a public form.

**[Kirim email permintaan penghapusan / Email a deletion request](mailto:singgalen.yerik@gmail.com?subject=KodeIn%20account%20and%20data%20deletion)**

Alamat / Address: **singgalen.yerik@gmail.com**  
Subjek / Subject: **KodeIn account and data deletion**

1. Kirim dari email yang dipakai untuk akun KodeIn jika Anda masih memiliki akses. / Send from your KodeIn account email if you still have access.
2. Nyatakan apakah ingin menghapus **akun dan seluruh data**, hanya **proyek/data tertentu**, atau **gambar yang pernah diunggah**. / State whether you want the account and all data, specific projects/data only, or uploaded images removed.
3. Jika tidak lagi dapat mengakses email akun, jelaskan keadaan tersebut agar kami dapat membantu verifikasi dengan informasi minimum yang diperlukan. / If you cannot access that email, explain the situation so we can arrange minimal ownership verification.
4. Kami memverifikasi kepemilikan sebelum menghapus, memproses permintaan, dan mengonfirmasi hasil atau menjelaskan jika perlu langkah/waktu tambahan. / We verify ownership, process the request and confirm the result or explain any additional steps/time needed.

**Jangan kirim password, token login, kunci API, atau transkrip peserta. Jangan mengajukan permintaan berisi data pribadi di GitHub Issues.**  
**Do not send passwords, login tokens, API keys or participant transcripts. Do not post personal deletion requests in GitHub Issues.**

## Hapus dari aplikasi / Delete in the app

1. Ekspor backup/laporan yang ingin disimpan. Penghapusan tidak dapat dibatalkan. / Export backups/reports you need first. Deletion cannot be undone.
2. Pastikan koneksi internet tersedia. Demi keamanan, keluar lalu masuk kembali dan mulai penghapusan dalam dua menit. / Connect to the internet. For security, sign out and back in, then start deletion within two minutes.
3. Buka **Settings / Pengaturan → Session / Sesi → Delete account and cloud data**. / Open Settings → Session → Delete account and cloud data.
4. Baca dialog lalu tekan **Delete permanently** untuk mengonfirmasi. / Read the dialog and confirm Delete permanently.
5. Jika proses gagal, sebagian data mungkin sudah terhapus. Masuk kembali untuk mencoba lagi atau gunakan email di atas. / If it fails, some data may already be deleted; sign in again to retry or email us.

## Apa yang dihapus / What is removed

Penghapusan akun dalam aplikasi mencakup akun Firebase Authentication, dokumen profil, proyek Firestore milik akun, serta transkrip, segmen, kode, versi kode, hasil coding, kategori, tema, memo, metadata gambar, literatur/catatan, Trash/payload dan catatan audit dalam proyek tersebut. State literatur lokal per proyek ikut dibersihkan ketika proyek dihapus.

In-app account deletion removes the Firebase Authentication account, profile document, owned Firestore projects, and their transcripts, segments, codes/code versions, coding records, categories, themes, memos, image metadata, literature/notes, Trash/payload and audit records. Per-project local literature state is cleared when that project is deleted.

## Gambar, perangkat dan salinan / Images, devices and copies

- **Cloudinary:** tombol aplikasi menghapus referensi gambar, tetapi tidak otomatis memusnahkan file gambar di Cloudinary. Email kami untuk penghapusan administratif foto profil/gambar proyek, termasuk foto lama atau unggahan yang belum terhubung jika relevan. Jika punya URL gambar/ID proyek, Anda dapat menyertakannya secara privat; jangan menunda permintaan jika tidak tahu ID tersebut. / The app deletes image references but does not automatically destroy Cloudinary files. Email us for administrative deletion, including old/unlinked uploads. Privately include image URLs/project IDs if available; they are not required to initiate a request.
- **Perangkat:** setelah penghapusan, gunakan **Android Settings → Apps → KodeIn → Storage → Clear storage** pada setiap perangkat yang Anda gunakan untuk menghapus cache, draft dan kunci API lokal. Keluar akun atau uninstall saja bukan permintaan penghapusan cloud. / After deletion, use Android Settings → Apps → KodeIn → Storage → Clear storage on your devices to remove caches, drafts and local API keys. Signing out or uninstalling alone does not request cloud deletion.
- **Ekspor dan backup:** file di penyimpanan Anda, layanan lain atau penerima yang Anda pilih tetap di bawah kendali Anda. Hapus salinan tersebut secara terpisah. / Exports/backups in your storage, other services or chosen recipients remain under your control; remove them separately.
- **Log/backup penyedia:** dapat mengikuti siklus penghapusan penyedia. Jika kewajiban hukum atau kebutuhan keamanan/sengketa tertentu mengharuskan retensi terbatas, kami menjelaskan alasan, lingkup dan durasinya saat menangani permintaan sejauh diizinkan hukum. Tidak ada janji pemusnahan seketika semua salinan infrastruktur. / Provider logs/backups may follow provider deletion cycles. We explain specific legal/security/dispute retention reasons, scope and duration when handling the request where permitted; instant erasure of all infrastructure copies is not promised.

Permintaan penghapusan akun tidak memerlukan pembayaran. Status permintaan dan kebutuhan tambahan dikomunikasikan melalui email. / There is no fee to request account deletion. Request status and any additional needs are communicated by email.

## Hapus sebagian data / Delete selected data

Anda dapat menghapus proyek tanpa menghapus akun, memindahkan transkrip ke Trash dan menghapus permanen dari Trash, atau meminta penghapusan data tertentu melalui email. Trash menawarkan masa pemulihan 30 hari; pembersihan kedaluwarsa berjalan saat fitur terkait diakses. Audit proyek tetap tersimpan sampai proyek/akun dihapus.

You can delete projects while keeping your account, move transcripts to Trash and permanently delete them there, or request selected-data deletion by email. Trash has a 30-day recovery period; expired items are purged when related features run. Project audit records remain until project/account deletion.

Lihat [Kebijakan Privasi / Privacy Policy](privacy-policy.html) untuk rincian pemrosesan dan penyimpanan.
''', 'ACCOUNT_DELETION.md')

page('support.md', 'Kontak & Bantuan / Contact & Support', '''
**KodeIn · Yerik Afrianto Singgalen · Updated 11 October 2026**

## Dukungan / Support

**[singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com?subject=KodeIn%20support)**

Untuk masalah aplikasi, sertakan versi KodeIn, versi Android, langkah terjadinya masalah, dan tangkapan layar yang sudah menghapus informasi pribadi. Jangan kirim password, kunci API, token, atau transkrip peserta. / For app problems, include your KodeIn/Android versions, reproduction steps and screenshots with personal information removed. Do not send passwords, API keys, tokens or participant transcripts.

## Privasi dan penghapusan / Privacy and deletion

Gunakan [halaman penghapusan akun/data](account-deletion.html) atau email yang sama dengan subjek **KodeIn privacy request**. Permintaan ditangani secara privat; GitHub Issues bukan tempat untuk informasi akun atau peserta. / Use the [account/data deletion page](account-deletion.html) or the same email with subject **KodeIn privacy request**. Requests are handled privately; GitHub Issues should not contain account or participant information.

## Masalah keamanan / Security concerns

Email secara privat dengan subjek **KodeIn security report**. Jelaskan dampak dan langkah reproduksi dengan data sintetis. Jangan publikasikan kerentanan yang melibatkan data pengguna atau kredensial. / Email privately using **KodeIn security report**, describing impact and reproduction with synthetic data. Do not publicly disclose vulnerabilities exposing user data or credentials.

## Dokumen / Documents

- [Kebijakan Privasi / Privacy Policy](privacy-policy.html)
- [Syarat Layanan / Terms of Service](terms-of-service.html)
- [Penghapusan Akun & Data / Account & Data Deletion](account-deletion.html)
- [Lisensi / Licenses](licenses.html)
''', 'SUPPORT.md')

page('index.md', 'KodeIn Legal & Support', '''
Dokumen resmi untuk aplikasi Android **KodeIn**, alat bantu penelitian kualitatif dari **Yerik Afrianto Singgalen**. / Official documents for **KodeIn**, the Android qualitative research tool developed by **Yerik Afrianto Singgalen**.

**Updated / Diperbarui: 11 October 2026**

| Dokumen / Document | Isi / Contents |
| --- | --- |
| [Privacy Policy](privacy-policy.html) | Data, tujuan pemrosesan, penyedia, penyimpanan dan hak pengguna. / Data, purposes, providers, retention and your rights. |
| [Terms of Service](terms-of-service.html) | Syarat penggunaan, kepemilikan data dan tanggung jawab penelitian. / Use, content rights and research responsibilities. |
| [Account & Data Deletion](account-deletion.html) | Penghapusan dalam aplikasi atau permintaan email tanpa memasang ulang. / In-app deletion or an email request without reinstalling. |
| [Licenses](licenses.html) | Hak aplikasi dan komponen pihak ketiga. / App rights and third-party components. |
| [Contact & Support](support.html) | Bantuan, permintaan privasi dan laporan keamanan secara privat. / Support, privacy requests and private security reports. |

**[Minta penghapusan akun/data / Request account/data deletion](account-deletion.html)**

Contact: [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com)
''')
# Home must resolve both the repository's base URL and its trailing slash.
p = ROOT / 'docs/index.md'
p.write_text(p.read_text().replace('permalink: /index.html', 'permalink: /'))
