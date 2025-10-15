import os
username_db = "member"
password_db = "12345"

produk = {
    1: ["Buku Tulis", 5000],
    2: ["Pensil", 3000],
    3: ["Penghapus", 2000],
    4: ["Penggaris", 4000],
    5: ["Spidol", 7000]
}

while True:  
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Selamat Datang di Toko Sederhana ===")
    status = input("Apakah Anda member? (y/n): ").lower()
    keranjang = []
    total = 0
    is_member = False

    if status == 'y':
        kesempatan = 3
        while kesempatan > 0:
            username = input("Masukkan username: ").strip()
            password = input("Masukkan password: ").strip()

            if not username or not password:
                print("Username dan password tidak boleh kosong!\n")
                continue

            if username == username_db and password == password_db:
                print("Login berhasil! Silakan belanja.")
                is_member = True
                break
            else:
                kesempatan -= 1
                print(f"Login gagal! Sisa percobaan: {kesempatan}\n")

        if not is_member:
            print("Anda dianggap sebagai Non-Member (gagal login 3 kali).\n")

    elif status == 'n':
        print("Anda belanja sebagai Non-Member.\n")
    else:
        print("Input tidak valid. Anda dianggap Non-Member.\n")

    while True:
        print("\n=== Menu Produk Toko ===")
        for i, (nama, harga) in produk.items():
            print(f"{i}. {nama:<12} - Rp{harga:,}")
        print("6. Checkout")

        try:
            pilih = int(input("Pilih produk: "))
        except ValueError:
            print("Masukkan angka yang benar!")
            continue

        if pilih == 6:
            break
        elif pilih in produk:
            try:
                qty = int(input(f"Masukkan jumlah {produk[pilih][0]}: "))
                if qty <= 0:
                    print("Jumlah tidak boleh nol atau negatif!")
                    continue
            except ValueError:
                print("Masukkan angka yang benar untuk jumlah!")
                continue

            subtotal = produk[pilih][1] * qty
            keranjang.append((produk[pilih][0], qty, subtotal))
            total += subtotal
            print(f"{produk[pilih][0]} berhasil ditambahkan! Total sementara: Rp{total:,}")
        else:
            print("Produk tidak tersedia!")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n===== STRUK BELANJA =====")
    for item, qty, subtotal in keranjang:
        print(f"{item:<12} x{qty:<3} = Rp{subtotal:,}")
    print("----------------------------")

    if is_member:
        diskon = total * 0.15
        total_bayar = total - diskon
        print(f"Total Sebelum Diskon : Rp{total:,}")
        print(f"Diskon 15%           : Rp{diskon:,}")
        print(f"Total Bayar          : Rp{total_bayar:,}")
    else:
        print(f"Total Bayar          : Rp{total:,}")
    print("============================\n")

    ulang = input("Apakah ingin memulai transaksi baru? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah berbelanja di Toko Sederhana!")
        break


