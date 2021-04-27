# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Tuples
'''
Input :
    1. User menentukan nilai per hurufnya dan menginput banyaknya nilai max yang diinginkan
Proses :
    1. Mencari nilai maximum
Output :
    1. Hasil akhir nilai max yang diinginkan User
'''

def test(my_dict, S):
    hasil = sorted(my_dict, key=my_dict.get, reverse=True)[:S]
    return hasil
my_dict = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
print("\nDictionary:")
print(my_dict)
S = int(input("\nJumlah Max yang diinginkan : "))
print("\n",S,"Jumlah maksimum ada :",end=' ')
print(test(my_dict, S))

