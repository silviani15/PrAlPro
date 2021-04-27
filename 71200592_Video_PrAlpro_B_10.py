# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Dictionaries

#Silvi pergi ke dealer motor untuk membeli beberapa motor dengan merk yang berbeda-beda 
#dimana kode di setiap motor itu ada KW001,YM002,SZ003,dll
#Silvi ingin membeli Motor Yamaha(3),Kawasaki(5),dan Suzuki(7)
#Buatlah daftarnya!

'''
Input :
    1. User menentukan brapa merk yang akan dicari
    2. User menginput kode barang dan jumlahnya
Proses :
    1. Mencari kode barang dan jumlah barang
Output :
    1. Hasil akhir adalah menyatukan semua apa yang sudah diinput oleh User
'''

print("==========WELCOME TO LIST MOTOR==========")
inp = int(input("Mau masukkan brapa kode motor? "))
My_Dict = {}
data_Key = []
Nilai = []
for i in range(0, inp):
    kode = input("Masukkan kode motor: ")
    data_Key.append(kode)
    jumlah = int(input("Masukkan jumlah motor: "))
    Nilai.append(jumlah)

for i in range(len(data_Key)):
    My_Dict[data_Key[i]] = Nilai[i]
print(My_Dict)
