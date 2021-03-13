# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Struktur Kontrol Kompleks
# Sumber : https://pesonainformatika.com/python/membuat-pola-segitiga-menggunakan-python/
'''
Input :
    1. User menentukan pilihan gambar yang diinginkan
Proses :
    1. Mencari Gambar Segitiga
    2. Mencari Gambar Diamond
    3. Mencari Gambar Model Celana
Output :
    1. Hasil akhir apakah itu Gambar Segitiga, Diamond, Model Celana
'''

print("Pilih Gambar yang Diinginkan!!!")
print("Ketik 1 untuk gambar Segitiga:")
print("Ketik 2 untuk gambar Diamond:")
print("Ketik 3 untuk gambar Model Celana:")
inp = int(input("Masukkan pilihan Anda : "))

if inp == 1 :
    n = int(input("Masukkan Tinggi : "))
    for i in range(n):
        for j in range (n,i,-1):
            print(" ", end = " ")
        for j in range ((2*i)+1):
            print("*", end = " ")
        print()

elif inp == 2:
    n = int(input("Masukkan Tinggi : "))
    for i in range(n):
        for j in range (n,i,-1):
            print(" ",end = "")
        for j in range (2*i+1):
            print("*",end = "")
        print()
    for i in range(n-2,-1,-1):
        for j in range (n,i,-1):
            print(" ",end = "")
        for j in range (2*i+1):
            print("*",end = "")
        print()

elif inp == 3 :
    n = int(input("Masukkan Angka : "))
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            print('*', '' , end = '')
        for l in range(i):
            print('    ', end = '')
        for k in range(i + 1, n):
            print('*', '' , end = '')
        print()

else:
    print("Hayoo, gak baca perintah ya?:) ,\nCoba Input lagi...")