CUELSHII — MASKOT 360 INTERAKTIF

ISI FILE
- index.html                 Viewer interaktif 360 derajat (model 3D sudah disematkan di dalamnya)
- cuelshii_mascot_360.glb    Model 3D untuk software yang mendukung GLB
- make_qr.py                 Skrip untuk membuat QR setelah halaman publik aktif

CARA MELIHAT
- Buka index.html di Chrome/Edge/Safari terbaru. Viewer ini sudah offline dan tidak memerlukan library eksternal atau koneksi internet untuk melihat model.
- Tarik atau geser untuk memutar, cubit untuk memperbesar di HP.

CARA MEMBUAT QR YANG BISA DIPAKAI DARI HP (CONTOH GITHUB PAGES)
1. Buat repository GitHub baru bernama cuelshii-360.
2. Upload file index.html ke root repository (file GLB tidak perlu diupload karena sudah tersemat dalam HTML).
3. Buka Settings → Pages → Build and deployment: Deploy from a branch, branch main, folder /(root).
4. Setelah dipublikasikan, halaman akan tersedia dalam format https://USERNAME.github.io/cuelshii-360/
5. Jalankan: python make_qr.py https://USERNAME.github.io/cuelshii-360/ (ganti dengan URL yang benar)
6. Alternatif: kirim URL publik ke ChatGPT dan minta dibuatkan QR code PNG.

PENTING
- Ini model 3D rekonstruksi berdasarkan gambar maskot Cuelshii yang tersedia, bukan mesh 3D asli.
- Jangan membuat QR code sampai halaman publik aktif. Jika URL sudah tersedia, QR bisa dibuat tanpa mengubah viewer.
- Viewer menggunakan WebGL2 native tanpa dependensi eksternal; bisa dibuka secara offline setelah diunduh.
