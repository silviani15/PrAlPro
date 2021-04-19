# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Lists
'''
Input :
    1. User menginput list babru yang akan ditambahakan
Proses :
    1. Memasukkan list baru ke dalam daftar menu
    2. Memasukkan list baru ke urutan berapa
Output :
    1. Menghasilnya apa yang akan ditambahkan oleh user
'''


list1 = ["Sate","Opor Ayam","Bakso","Soto","Lesah"]
list2 = ["Jus","Susu","Kopi","Sup Buah","Esteler"]
print("List Makanan :",list1)
print("List Minuman :",list2)
print()

tambah_list_makan = input("Tambahkan jenis makanan : ")
di_indeks_makan = int(input("Di indeks ke : "))

tambah_list_minum = input("Tambahkan jenis minuman : ")
di_indeks_minum = int(input("Di indeks ke : "))
list1.insert(di_indeks_makan,tambah_list_makan)
list2.insert(di_indeks_minum,tambah_list_minum)
print("Hasil list makanan baru adalah :\n",list1)
print("Hasil list minuman baru adalah :\n",list2)