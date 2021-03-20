# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Strings

'''
Input : 
    1. User memasukkan kalimat yang akan dihitung
Proses : 
    1. Mencari Jumlah kata
    2. Mencari Jumlah Karakter
Output : 
    1. Menghasilkan jawaban yang dicari yaitu menentukan jumlah kata dan jumlah karakter
'''

inp = str(input("Masukkan Kalimat : "))
def penghitungan_kata():
    hitung_karakter = inp.split()
    print("Jumlah Karakter : ",len(inp))
    hitung_kata = len(hitung_karakter)
    print("Jumlah Kata : ",hitung_kata)
penghitungan_kata()