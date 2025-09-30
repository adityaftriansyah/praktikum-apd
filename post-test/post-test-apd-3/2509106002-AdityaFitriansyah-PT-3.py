# Sistem Belanja Toko Sederhana by Adit

# login sebagai member
username_db = "member"
password_db = "12345"

total = 0

print("=== Menu Produk Toko ===")
print("1. Buku Tulis  - Rp5000")
print("2. Pensil      - Rp3000")
print("3. Penghapus   - Rp2000")
print("4. Penggaris   - Rp4000")
print("5. Spidol      - Rp7000")

print("\nSelamat datang di Toko Sederhana!")
status = input("Apakah Anda member? (y/n): ").lower()

if status == "y":
    # login dengan ternary operator
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    login = True if (username == username_db and password == password_db) else False

    if login:
        print("Login berhasil! Silakan belanja.")
        while True:
            pilih = int(input("Pilih produk (0 untuk selesai): "))
            if pilih == 0:
                break
            elif pilih == 1:
                qty = int(input("Jumlah Buku Tulis: "))
                total += 5000 * qty
            elif pilih == 2:
                qty = int(input("Jumlah Pensil: "))
                total += 3000 * qty
            elif pilih == 3:
                qty = int(input("Jumlah Penghapus: "))
                total += 2000 * qty
            elif pilih == 4:
                qty = int(input("Jumlah Penggaris: "))
                total += 4000 * qty
            elif pilih == 5:
                qty = int(input("Jumlah Spidol: "))
                total += 7000 * qty
            else:
                print("Produk tidak tersedia.")

        # menghitung diskon
        diskon = total * 0.15
        total_setelah_diskon = total - diskon
        print("\n=== Rincian Pembayaran (Member) ===")
        print(f"Total sebelum diskon : Rp{total:,}")
        print(f"Diskon 15%           : Rp{diskon:,}")
        print(f"Total setelah diskon : Rp{total_setelah_diskon:,}")
    else:
        print("Login gagal! Akses ditolak.")

else:
    print("Anda belanja sebagai Non-Member.")
    while True:
        pilih = int(input("Pilih produk (0 untuk selesai): "))
        if pilih == 0:
            break
        elif pilih == 1:
            qty = int(input("Jumlah Buku Tulis: "))
            total += 5000 * qty
        elif pilih == 2:
            qty = int(input("Jumlah Pensil: "))
            total += 3000 * qty
        elif pilih == 3:
            qty = int(input("Jumlah Penghapus: "))
            total += 2000 * qty
        elif pilih == 4:
            qty = int(input("Jumlah Penggaris: "))
            total += 4000 * qty
        elif pilih == 5:
            qty = int(input("Jumlah Spidol: "))
            total += 7000 * qty
        else:
            print("Produk tidak tersedia.")

    print("\n=== Rincian Pembayaran (Non-Member) ===")
    print(f"Total belanja : Rp{total:,}")