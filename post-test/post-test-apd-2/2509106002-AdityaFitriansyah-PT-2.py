# update: testing commit rename

# input dari user
nama = input("Masukkan nama pasien: ")
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))

# rumus berat ideal
beratIdeal = tinggi - 100

# status menggunakan list
statusList = ["Berat Badan Kurang Ideal", "Berat Badan Ideal", "Kelebihan Berat Badan"]
statusIndex = (berat > beratIdeal) - (berat < beratIdeal)
status = statusList[statusIndex + 1]

# data untuk tabel
data = [
    ("Nama Pasien", nama),
    ("Tinggi Badan", f"{tinggi:.0f} cm"),
    ("Berat Badan", f"{berat:.0f} kg"),
    ("Berat Ideal", f"{beratIdeal:.0f} kg"),
    ("Status", status),
]

lebar_kiri = max(len(baris[0]) for baris in data) + 2
lebar_kanan = max(len(baris[1]) for baris in data) + 2
lebar_total = lebar_kiri + lebar_kanan + 5

print("-" * lebar_total)
print("|{:^{}}|".format("HASIL CEK BERAT BADAN", lebar_total - 2))
print("-" * lebar_total)

for kiri, kanan in data:
    print(f"| {kiri:<{lebar_kiri}}: {kanan:<{lebar_kanan}}|")

print("-" * lebar_total)