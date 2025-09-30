print("=== Variabel & Tipe Data Numerik ===")
# Integer
a = 10
b = 3
c = a + b
print("Hasil Integer:", c)    

# Float
a = 0.13
b = 0.15
c = a + b
print("Hasil Float:", c)      


print("\n=== Tipe Data String ===")
# String sederhana
Nama = 'Sifwah'
Hobi = "ngoding"
print(Nama)
print(Hobi)

# String multiline
print("""Halo,
Saya sedang belajar ngoding
Bahasa Pemrograman python""")

# Menggabungkan string
print("halo""saya""daffa")
print("halo" + "daffa")

# Indexing string
teks = 'saya suka belajar apd'
print("Index ke-3:", teks[3])      
print("Index 0-2 :", teks[0:3])    
print("Mulai index 5:", teks[5:])     
print("Sampai index 7:", teks[:8])     


print("\n=== Boolean ===")
Hujan = False
Panas = True
print("Hujan:", Hujan)
print("Panas:", Panas)


print("\n=== List ===")
prodi = ['Informatika', 'Sistem Informasi', 'Teknik Sipil']
print(prodi[0])
print(prodi[1])
print(prodi[2])

# slicing list
print(prodi[0:1])
print(prodi[1:])
print(prodi[:2])


print("\n=== Tuple ===")
tuple_data = ('Lian', 19, True, 'APD')
print(tuple_data[0])
print(tuple_data[2])


print("\n=== Dictionary ===")
warna = {
    'warna1': 'merah',
    'warna2': 'kuning',
    'warna3': 'hijau'
}
print(warna['warna1'])
print(warna['warna3'])


print("\n=== Input Manual ===")
nama = input("Masukkan Nama Anda : ")
print("Halo,", nama)