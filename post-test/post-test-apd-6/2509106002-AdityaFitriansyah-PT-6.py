import os

# ---------------------------
#        DATA AWAL
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

# ---------------------------
#    FUNGSI TAMBAHAN
# ---------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_produk():
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Nama", "Stok", "Harga"))
    print("-"*45)
    for idp, data in produk.items():
        print("{:<5} {:<15} {:<10} {:<10}".format(idp, data["nama"], data["stok"], data["harga"]))
    print("-"*45)

# ---------------------------
#       MENU UTAMA
# ---------------------------
while True:
    clear()
    print("=== SISTEM PENGELOLAAN STOK ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    # ---------------------------
    #         REGISTER
    # ---------------------------
    if pilihan == "2":
        clear()
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru : ").strip()
        password = input("Masukkan password baru : ").strip()

        if username in users:
            print("❌ Username sudah digunakan.")
        elif username == "" or password == "":
            print("❌ Username dan password tidak boleh kosong.")
        else:
            users.setdefault(username, {"password": password, "role": "user"})
            print("✅ Akun berhasil dibuat.")
        input("\nTekan Enter untuk kembali...")

    # ---------------------------
    #           LOGIN
    # ---------------------------
    elif pilihan == "1":
        clear()
        print("=== LOGIN SISTEM ===")
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        user = users.get(username)
        if user and user["password"] == password:
            role = user["role"]
            print(f"✅ Login berhasil sebagai {role.upper()}!")
            input("\nTekan Enter untuk melanjutkan...")

            # ---------------------------
            #       MENU ADMIN
            # ---------------------------
            if role == "admin":
                keluar_admin = False
                while not keluar_admin:
                    clear()
                    print("=== MENU ADMIN ===")
                    print("1. Tambah Produk")
                    print("2. Lihat Produk")
                    print("3. Update Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    pilih = input("Pilih menu: ")

                    # Tambah produk (Create)
                    if pilih == "1":
                        clear()
                        print("=== TAMBAH PRODUK ===")
                        idp = input("ID Produk : ").strip()
                        nama = input("Nama Produk : ").strip()
                        stok = input("Stok Awal : ").strip()
                        harga = input("Harga : ").strip()

                        if idp in produk:
                            print("❌ ID produk sudah ada.")
                        elif not stok.isdigit() or not harga.isdigit():
                            print("❌ Stok dan harga harus angka.")
                        else:
                            produk.update({
                                idp: {"nama": nama, "stok": int(stok), "harga": int(harga)}
                            })
                            print("✅ Produk berhasil ditambahkan.")
                        input("\nTekan Enter untuk kembali...")

                    # Lihat produk (Read) 
                    elif pilih == "2":
                        clear()
                        print("=== DAFTAR PRODUK ===")
                        tampilkan_produk()
                        input("\nTekan Enter untuk kembali...")

                    # Update produk 
                    elif pilih == "3":
                        clear()
                        print("=== UPDATE PRODUK ===")
                        tampilkan_produk()
                        idp = input("Masukkan ID produk yang akan diupdate: ").strip()

                        if idp not in produk:
                            print("❌ Produk tidak ditemukan.")
                        else:
                            nama_baru = input("Nama baru: ").strip()
                            stok_baru = input("Stok baru: ").strip()
                            harga_baru = input("Harga baru: ").strip()

                            if not stok_baru.isdigit() or not harga_baru.isdigit():
                                print("❌ Stok dan harga harus angka.")
                            else:
                                produk[idp]["nama"] = nama_baru or produk[idp]["nama"]
                                produk[idp]["stok"] = int(stok_baru)
                                produk[idp]["harga"] = int(harga_baru)
                                print("✅ Produk berhasil diperbarui.")
                        input("\nTekan Enter untuk kembali...")

                    # Hapus produk (Delete, menggunakan pop)
                    elif pilih == "4":
                        clear()
                        print("=== HAPUS PRODUK ===")
                        tampilkan_produk()
                        idp = input("Masukkan ID produk yang ingin dihapus: ").strip()

                        if idp in produk:
                            dihapus = produk.pop(idp)
                            print(f"✅ Produk {dihapus['nama']} berhasil dihapus.")
                        else:
                            print("❌ ID produk tidak ditemukan.")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih == "5":
                        keluar_admin = True
                    else:
                        print("❌ Pilihan tidak valid.")
                        input("\nTekan Enter untuk kembali...")

            # ---------------------------
            #       MENU USER
            # ---------------------------
            elif role == "user":
                keluar_user = False
                while not keluar_user:
                    clear()
                    print("=== MENU PENGGUNA ===")
                    print("1. Lihat Produk")
                    print("2. Logout")
                    pilih = input("Pilih menu: ")

                    if pilih == "1":
                        clear()
                        print("=== DAFTAR PRODUK ===")
                        tampilkan_produk()
                        input("\nTekan Enter untuk kembali...")

                    elif pilih == "2":
                        keluar_user = True
                    else:
                        print("❌ Pilihan tidak valid.")
                        input("\nTekan Enter untuk kembali...")

        else:
            print("❌ Username atau password salah!")
            input("\nTekan Enter untuk kembali...")

    # ---------------------------
    #           KELUAR
    # ---------------------------
    elif pilihan == "3":
        clear()
        print("👋 Terima kasih telah menggunakan sistem ini!")
        break

    else:
        print("❌ Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")