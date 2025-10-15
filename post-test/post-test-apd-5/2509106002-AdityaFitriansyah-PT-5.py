import os

# ---------------------------
#          Data Awal
# ---------------------------
users = [
    ["admin", "admin123", "admin"],
    ["user", "user123", "user"]
]

produk = [
    ["001", "Sabun", 15, 3000],
    ["002", "Shampoo", 10, 7000],
    ["003", "Sikat Gigi", 20, 4000]
]

# ---------------------------
#       Pilihan Menu
# ---------------------------
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENGELOLAAN STOK RETAIL KECIL ===")
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
        username = input("Masukkan username baru : ")
        password = input("Masukkan password baru : ")

        sudah_ada = False
        for u in users:
            if u[0] == username:
                sudah_ada = True

        if sudah_ada:
            print("❌ Username sudah terdaftar!")
        else:
            users.append([username, password, "user"])
            print("✅ Akun berhasil dibuat!")

        input("\nTekan Enter untuk kembali...")

    # ---------------------------
    #            LOGIN
    # ---------------------------
    elif pilihan == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN SISTEM ===")
        username = input("Username : ")
        password = input("Password : ")
        role = None

        for u in users:
            if u[0] == username and u[1] == password:
                role = u[2]

        if role == None:
            print("❌ Username atau password salah!")
            input("\nTekan Enter untuk kembali...")
        else:
            print(f"✅ Login berhasil! Selamat datang, {username}")
            input("\nTekan Enter untuk melanjutkan...")

            # ---------------------------
            #         MENU ADMIN
            # ---------------------------
            if role == "admin":
                selesai_admin = False
                while not selesai_admin:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU ADMIN ===")
                    print("1. Tambah Produk (Create)")
                    print("2. Lihat Produk (Read)")
                    print("3. Update Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    pilih_admin = input("Pilih menu: ")

                    # Create
                    if pilih_admin == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH PRODUK BARU ===")
                        idp = input("ID Produk: ")
                        nama = input("Nama Produk: ")
                        stok = input("Stok Awal: ")
                        harga = input("Harga: ")

                        if (not stok.isdigit()) or (not harga.isdigit()):
                            print("❌ Stok dan harga harus angka!")
                        else:
                            produk.append([idp, nama, int(stok), int(harga)])
                            print("✅ Produk berhasil ditambahkan!")
                        input("\nTekan Enter untuk kembali...")

                    # Read
                    elif pilih_admin == "2":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PRODUK ===")
                        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Nama", "Stok", "Harga"))
                        print("-"*45)
                        for p in produk:
                            print("{:<5} {:<15} {:<10} {:<10}".format(p[0], p[1], p[2], p[3]))
                        print("-"*45)
                        input("\nTekan Enter untuk kembali...")

                    # Update
                    elif pilih_admin == "3":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UPDATE PRODUK ===")
                        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Nama", "Stok", "Harga"))
                        print("-"*45)
                        for p in produk:
                            print("{:<5} {:<15} {:<10} {:<10}".format(p[0], p[1], p[2], p[3]))
                        print("-"*45)

                        idp = input("Masukkan ID produk yang ingin diupdate: ")
                        index = -1
                        for i in range(len(produk)):
                            if produk[i][0] == idp:
                                index = i

                        if index == -1:
                            print("❌ ID produk tidak ditemukan!")
                        else:
                            nama_baru = input("Nama baru: ")
                            stok_baru = input("Stok baru: ")
                            harga_baru = input("Harga baru: ")

                            if (not stok_baru.isdigit()) or (not harga_baru.isdigit()):
                                print("❌ Stok dan harga harus angka!")
                            else:
                                produk[index][1] = nama_baru
                                produk[index][2] = int(stok_baru)
                                produk[index][3] = int(harga_baru)
                                print("✅ Data produk berhasil diperbarui!")
                        input("\nTekan Enter untuk kembali...")

                    # Delete
                    elif pilih_admin == "4":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS PRODUK ===")
                        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Nama", "Stok", "Harga"))
                        print("-"*45)
                        for p in produk:
                            print("{:<5} {:<15} {:<10} {:<10}".format(p[0], p[1], p[2], p[3]))
                        print("-"*45)

                        idp = input("Masukkan ID produk yang ingin dihapus: ")
                        ditemukan = False

                        for p in produk:
                            if p[0] == idp:
                                produk.remove(p)
                                ditemukan = True
                                print("✅ Produk berhasil dihapus!")
                                break
                        if not ditemukan:
                            print("❌ ID produk tidak ditemukan!")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_admin == "5":
                        selesai_admin = True
                    else:
                        print("❌ Pilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")

            # ---------------------------
            #      MENU UNTUK USER
            # ---------------------------
            elif role == "user":
                selesai_user = False
                while not selesai_user:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU PENGGUNA ===")
                    print("1. Lihat Produk")
                    print("2. Logout")
                    pilih_user = input("Pilih menu: ")

                    if pilih_user == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== DAFTAR PRODUK ===")
                        print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Nama", "Stok", "Harga"))
                        print("-"*45)
                        for p in produk:
                            print("{:<5} {:<15} {:<10} {:<10}".format(p[0], p[1], p[2], p[3]))
                        print("-"*45)
                        input("\nTekan Enter untuk kembali...")

                    elif pilih_user == "2":
                        selesai_user = True
                    else:
                        print("❌ Pilihan tidak valid!")
                        input("\nTekan Enter untuk kembali...")

    # ---------------------------
    #           KELUAR
    # ---------------------------
    elif pilihan == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("👋 Terima kasih telah menggunakan sistem ini!")
        break

    else:
        print("❌ Pilihan tidak valid!")
        input("\nTekan Enter untuk kembali...")