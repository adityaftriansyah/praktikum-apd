import os

# ---------------------------
#       VARIABEL GLOBAL
# ---------------------------
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

produk = {
    "001": {"nama": "Sabun", "stok": 15, "harga": 3000},
    "002": {"nama": "Shampoo", "stok": 10, "harga": 7000},
    "003": {"nama": "Sikat Gigi", "stok": 20, "harga": 4000}
}

status_login = False

# Prosedur 1
def tampilkan_produk():
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Nama", "Stok", "Harga"))
    print("-" * 45)
    for idp, data in produk.items():
        print("{:<5} {:<15} {:<10} {:<10}".format(idp, data["nama"], data["stok"], data["harga"]))
    print("-" * 45)

# Prosedur 2
def pesan(teks):
    print(f"📢 {teks}")

# ---------------------------
#   FUNGSI DENGAN PARAMETER
# ---------------------------

def tambah_stok(idp, jumlah):
    # variabel lokal
    if idp in produk:
        produk[idp]["stok"] += jumlah
        return f"✅ Stok {produk[idp]['nama']} bertambah {jumlah}."
    else:
        return "❌ Produk tidak ditemukan."

# ---------------------------
#   FUNGSI TANPA PARAMETER
# ---------------------------

def total_produk():
    total = len(produk)
    return total

# ---------------------------
#      FUNGSI REKURSIF
# ---------------------------

def konfirmasi_keluar():
    pilihan = input("Yakin ingin keluar? (y/n): ").lower()
    if pilihan == "y":
        print("👋 Terima kasih telah menggunakan sistem ini!")
        exit()
    elif pilihan == "n":
        return
    else:
        print("❌ Input tidak valid!")
        # rekursif: memanggil dirinya sendiri
        konfirmasi_keluar()

# ---------------------------
#       PROGRAM UTAMA
# ---------------------------

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENGELOLAAN STOK (LANJUTAN) ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    # ---------------------------
    #          REGISTER
    # ---------------------------
    if pilihan == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")

        try:
            username = input("Masukkan username baru: ").strip()
            password = input("Masukkan password baru: ").strip()

            if not username or not password:
                raise ValueError("❌ Username dan password tidak boleh kosong!")
            elif username in users:
                raise KeyError("❌ Username sudah digunakan!")
            elif len(password) < 5:
                raise ValueError("❌ Password minimal 5 karakter!")

        except (ValueError, KeyError) as e:
            print(e)
        else:
            users[username] = {"password": password, "role": "user"}
            print("✅ Akun berhasil dibuat!")
        finally:
            input("\nTekan Enter untuk kembali...")

    # ---------------------------
    #           LOGIN
    # ---------------------------
    elif pilihan == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN SISTEM ===")

        try:
            username = input("Username : ").strip()
            password = input("Password : ").strip()
            if not username or not password:
                raise ValueError("❌ Username dan password wajib diisi!")

            user = users.get(username)
            if not user:
                raise KeyError("❌ Username tidak ditemukan!")
            elif user["password"] != password:
                raise ValueError("❌ Password salah!")

        except (ValueError, KeyError) as e:
            print(e)
            input("\nTekan Enter untuk kembali...")
            continue
        else:
            role = user["role"]
            print(f"✅ Login berhasil sebagai {role.upper()}")
            input("\nTekan Enter untuk melanjutkan...")

        # ---------------------------
        #         MENU ADMIN
        # ---------------------------
        if role == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Lihat Produk")
                print("2. Tambah Stok")
                print("3. Total Produk")
                print("4. Logout")

                pilih = input("Pilih menu: ")

                if pilih == "1":
                    tampilkan_produk()
                    input("\nTekan Enter...")

                elif pilih == "2":
                    tampilkan_produk()
                    idp = input("Masukkan ID produk: ").strip()
                    try:
                        jml = int(input("Jumlah tambah stok: "))
                        pesan(tambah_stok(idp, jml))
                    except ValueError:
                        print("❌ Input stok harus berupa angka!")
                    input("\nTekan Enter...")

                elif pilih == "3":
                    print(f"📦 Total produk: {total_produk()}")
                    input("\nTekan Enter...")

                elif pilih == "4":
                    break
                else:
                    print("❌ Pilihan tidak valid!")
                    input("\nTekan Enter...")

        # ---------------------------
        #         MENU USER
        # ---------------------------
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU USER ===")
                print("1. Lihat Produk")
                print("2. Logout")
                pilih = input("Pilih menu: ")

                if pilih == "1":
                    tampilkan_produk()
                    input("\nTekan Enter...")
                elif pilih == "2":
                    break
                else:
                    print("❌ Pilihan tidak valid!")
                    input("\nTekan Enter...")

    # ---------------------------
    #         KELUAR
    # ---------------------------
    elif pilihan == "3":
        konfirmasi_keluar()

    else:
        print("❌ Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")