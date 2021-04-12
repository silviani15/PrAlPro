# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Files

'''
Input : 
    1. User menentukan kode Biner yang akan diubah ke Desimal di note
Proses : 
    1. Mengubah Biner ke Desimal
Output : 
    1. Menghasilkan jawaban yang dicari yaitu menentukan passwordnya
'''

handle = open("D:\\tanggalku.txt","r")
handle1 = handle.read ()
rank = len(handle1) - 1
des = 0
for i in range (len(handle1)):
    Biner = int(handle1[i])
    Desimal = Biner * (2 ** rank)
    des = des + Desimal
    rank = rank - 1
print('Passwordnya adalah', des)

handle.close()