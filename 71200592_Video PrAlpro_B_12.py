# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Sets
'''
Input :
    1. User menentukan pilihan yang mencari Union, Intersection, Difference, atau Symmetric Difference
Proses :
    1. Mencari Union
    2. Mencari Intersection
    3. Mencari Difference
    4. Mencari Symmetric Difference
Output :
    1. Hasil akhir apakah itu Union, Intersection, Difference, atau Symmetric Difference
'''

print("Selamat datang di Operasi pada Set")     
print("Ketik 1 untuk mencari Union:")
print("Ketik 2 untuk mencari Intersection:")
print("Ketik 3 untuk mencari Difference:")
print("Ketik 4 untuk mencari Symmetric Difference:\n")
inp = int(input("Masukkan pilihan Anda : "))

if inp == 1 :
    color = {'Yellow', 'Red', 'Blue', 'Green', 'Black', 'White'}
    banding = {'Red', 'Violet', 'Blue', 'Yellow', 'Tiffani', 'Orange'}
    hasil = color | banding
    print("Hasilnya adalah :\n",hasil)

elif inp == 2:
    color = {'Yellow', 'Red', 'Blue', 'Green', 'Black', 'White'}
    banding = {'Red', 'Violet', 'Blue', 'Yellow', 'Tiffani', 'Orange'}
    hasil = color & banding
    print("Hasilnya adalah :\n",hasil)

elif inp == 3 :
    color = {'Yellow', 'Red', 'Blue', 'Green', 'Black', 'White'}
    banding = {'Red', 'Violet', 'Blue', 'Yellow', 'Tiffani', 'Orange'}
    hasil = color - banding
    print("Hasilnya adalah :\n",hasil)

elif inp == 4 :
    color = {'Yellow', 'Red', 'Blue', 'Green', 'Black', 'White'}
    banding = {'Red', 'Violet', 'Blue', 'Yellow', 'Tiffani', 'Orange'}
    hasil = color ^ banding
    print("Hasilnya adalah :\n",hasil)

else:
    print("Input yang anda masukkan tidak valid")