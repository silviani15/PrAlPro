# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Fungsi Rekursif

'''
Input :
      1. User menentukan FPB yang akan dicari
Proses :
      1. Mencari FPB
Output:
      1. Menghasilkan jawaban yang dicari
'''

def CariFPB(a,b):
    if(b==0):
        return a
    else:
        hasil = a % b
        return CariFPB(b, hasil)
        
fpb = CariFPB(336, 88)
print(fpb)