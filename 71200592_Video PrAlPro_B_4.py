# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Struktur Kontrol Perulangan

'''
Input :
      1. User memasukkan angka yang akan dimasukkan
Proses :
      1. Mencari Perulangan
Output:
      1. Menghasilkan jawaban yang dicari
'''
x = int(input("Masukkan Bilangan Pertama : "))
y = int(input("Masukkan Bilangan Kedua : "))
while x <= y :
      print(x, end=" ") #end=" " agar outpunya kesamping
      x = x + 1
      print(y, end=" ")
      y = y - 1