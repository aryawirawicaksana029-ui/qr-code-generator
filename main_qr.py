import qrcode
import sys

def cetak_header():
    print("\n" + "="*40)
    print("      🔥 QR CODE GENERATOR PRO 🔥      ")
    print("="*40)

def generate_basic_qr():
    print("\n--- 1. GENERATE BASIC QR CODE ---")
    data = input("Masukkan URL atau Teks yang ingin diubah: ").strip()
    if not data:
        print("❌ Data tidak boleh kosong!")
        return

    nama_file = input("Masukkan nama file hasil (contoh: my_qr): ").strip()
    if not nama_file:
        nama_file = "qrcode_hasil"
    
    # Menambahkan ekstensi .png jika user belum menulisnya
    if not nama_file.endswith('.png'):
        nama_file += '.png'

    print("⏳ Sedang memproses...")
    try:
        img = qrcode.make(data)
        img.save(nama_file)
        print(f"✅ Sukses! QR Code berhasil disimpan dengan nama: {nama_file}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

def generate_custom_qr():
    print("\n--- 2. GENERATE CUSTOM QR CODE ---")
    data = input("Masukkan URL atau Teks yang ingin diubah: ").strip()
    if not data:
        print("❌ Data tidak boleh kosong!")
        return

    # Kustomisasi Ukuran (Box Size)
    print("\n[Pengaturan Ukuran]")
    try:
        box_size = input("Masukkan ukuran box (Rekomendasi: 10): ")
        box_size = int(box_size) if box_size else 10
    except ValueError:
        print("⚠️ Input tidak valid, menggunakan ukuran default (10).")
        box_size = 10

    # Kustomisasi Warna
    print("\n[Pengaturan Warna] (Gunakan nama warna bahasa Inggris, misal: black, white, red, blue)")
    warna_qr = input("Warna QR Code (Default: black): ").strip() or "black"
    warna_bg = input("Warna Background (Default: white): ").strip() or "white"

    nama_file = input("\nMasukkan nama file hasil (contoh: custom_qr): ").strip()
    if not nama_file:
        nama_file = "custom_qrcode"
    if not nama_file.endswith('.png'):
        nama_file += '.png'

    print("⏳ Sedang merakit QR Code kustom kamu...")
    try:
        # Menggunakan fitur QRCode advanced untuk customisasi
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Bikin gambarnya dengan warna kustom
        img = qr.make_image(fill_color=warna_qr, back_color=warna_bg)
        img.save(nama_file)
        print(f"🎨 Keren! QR Code Kustom berhasil disimpan sebagai: {nama_file}")
    except Exception as e:
        print(f"❌ Gagal membuat QR kustom. Pastikan nama warna benar! Error: {e}")

def main():
    while True:
        cetak_header()
        print("1. Generate QR Code (Standar)")
        print("2. Customize QR Code (Warna & Ukuran)")
        print("3. Exit / Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (1-3): ").strip()

        if pilihan == "1":
            generate_basic_qr()
        elif pilihan == "2":
            generate_custom_qr()
        elif pilihan == "3":
            print("\nThank you sudah pakai QR Generator ini. Sampai jumpa di project berikutnya! 🚀")
            sys.exit()
        else:
            print("❌ Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
        
        # Biar menu gak langsung ke-refresh, kasih jeda enter
        input("\nTekan [ENTER] untuk kembali ke menu utama...")

if __name__ == "__main__":
    main()