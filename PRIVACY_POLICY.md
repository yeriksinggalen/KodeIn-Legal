# Kebijakan Privasi / Privacy Policy

**Aplikasi / Application:** KodeIn (`com.yerik.kodein`)  
**Pengembang / Developer:** Yerik Afrianto Singgalen  
**Berlaku dan diperbarui / Effective and updated:** 11 October 2026  
**Kontak privasi / Privacy contact:** [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com)

[Bahasa Indonesia](#bahasa-indonesia) · [English](#english) · [Penghapusan akun / Account deletion](https://yeriksinggalen.github.io/KodeIn-Legal/account-deletion.html)

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

**Gambar Cloudinary tidak otomatis dimusnahkan oleh tombol hapus akun.** Penghapusan gambar dilakukan secara administratif melalui [permintaan penghapusan](https://yeriksinggalen.github.io/KodeIn-Legal/account-deletion.html). Foto lama atau unggahan yang belum berhasil terhubung ke profil/proyek juga mungkin membutuhkan penelusuran administratif. Cache pada perangkat lain, draft lokal, kunci API, backup, dan laporan yang telah diekspor tidak otomatis dihapus dari semua lokasi. Setelah menghapus akun, hapus penyimpanan aplikasi melalui pengaturan Android di perangkat Anda dan kelola salinan ekspor/backup Anda sendiri.

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

**Cloudinary images are not automatically destroyed by the in-app account deletion button.** Request administrative removal using the [deletion page](https://yeriksinggalen.github.io/KodeIn-Legal/account-deletion.html), including old/unlinked uploads when relevant. Other-device caches, local drafts, API keys and exported backups/reports are not automatically removed everywhere. Clear KodeIn storage through Android Settings on your devices after deletion and manage exported copies yourself.

If an actual legal obligation or security/dispute need requires limited retention, we will explain the scope, reason and duration when handling your request where legally allowed. Provider infrastructure logs, backups and caches follow provider removal cycles; immediate erasure of every infrastructure copy is not promised.

### Your choices and security
Edit your profile, export records, delete projects/transcripts, remove optional API credentials or app storage, or request access, correction, deletion, restriction/objection handling as applicable by emailing [singgalen.yerik@gmail.com](mailto:singgalen.yerik@gmail.com). We request only information needed for ownership verification and fulfillment. Never send passwords, tokens, API keys or participant transcripts.

Service traffic uses HTTPS and Scopus credential preferences are encrypted. Drafts/caches and exports do not all have app-specific encryption. Protect devices, minimize and de-identify data, and satisfy participant consent, institutional ethics and applicable requirements before cloud upload. No system guarantees absolute security. Current auto-coding and literature ranking use app/local logic and do not transmit transcripts to an external generative AI service; researchers must review results.

KodeIn is intended for research, not directed at children under 13. Contact us about unauthorized child data; researchers working with children still need appropriate authority, consent and protections. Updates carry a revised date; material changes will be communicated through available app/service channels.
