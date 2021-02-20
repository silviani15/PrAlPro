# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Struktur Kontrol Percabangan

'''Doni adalah Mahasiswa Informatika UKDW Angkatan 2020. Suatu hari Doni mendapatkan
tugas untuk membuat kalkulator sederhana yang dapat menghitung sisa hasil bagi (modulus),
floor division, dan pemangkatan suatu bilangan yang di inputkan user, Bantulah Doni dengan
membuat kalkulator sederhana yang dapat menghitung modulus, floor division, dan
pemangkatan suatu bilangan.

Input :
    1. User menentukan pilihan yang mencari Modulus, Floor Division, atau Pemangkatan
Proses :
    1. Mencari Modulus
    2. Mencari Floor Division
    3. Mencari Pemangkatan
Output :
    1. Hasil akhir apakah itu Modulus, Floor Division, atau Pemangkatan
'''

print("Selamat datang di Kalkulator sederhana")
print("Ketik 1 untuk mencari Modulus:")
print("Ketik 2 untuk mencari Floor Division:")
print("Ketik 3 untuk mencari Pemangkatan:")
inp = int(input("Masukkan pilihan Anda : "))

if inp == 1 :
    a = int(input("Masukkan bilangan pertama : "))
    b = int(input("Masukkan bilangan kedua : "))
    hasil = a%b
    print("Hasil dari %d "%a,"modulus %d adalah: "%b,hasil)

elif inp == 2:
    a = int(input("Masukkan bilangan pertama : "))
    b = int(input("Masukkan bilangan kedua : "))
    hasil = a//b
    print("Hasil dari %d "%a,"floor division %d adalah: "%b,hasil)

elif inp == 3 :
    a = int(input("Masukkan bilangan pertama : "))
    b = int(input("Masukkan bilangan kedua : "))
    hasil = a**b
    print("Hasil dari %d "%a,"Pemangkatan %d adalah: "%b,hasil)

else:
    print("Input yang anda masukkan tidak valid")