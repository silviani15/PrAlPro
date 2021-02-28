# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Modular Programming (fungsi)
# Sumber : https://rumuspintar.com/fibonacci/

'''
Input :
    1. User ingin mencari suku ke berapa
Proses :
    1. Mencari Bilangan Fibonancci
Output :
    1. Menghasilkan jawaban yang dicari (suku ke-n)
'''

def fibon(n) :
    a=1
    b=1
    if n == 1 :
        print("0")
    elif n == 2 :
        print("0","1")
    else :
        print("Barisan_Bilangan: ", end=" ")
        print("0",a,b,end=" ")
        for n in range(n-3) :
            total = a + b
            b = a
            a = total
            print(total,end=" ")
        print()
        return b
n = int(input("n = "))
fibon(n+1)
print("*Note : Barisan Bilangan suku ke -",n,"terdapat dibarisan paling akhir!")