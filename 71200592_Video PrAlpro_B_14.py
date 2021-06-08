# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20
# Regular Expression

# Hari ini hari Minggu, pas banget waktunya si Bambank buat belanja kebutuhannya.
# Dia mau pergi ke supermarket buat beli 3 odol, 5 roti, dan 8 fanta
# Bambang nda sendiri dia ditemani Sri dan Ucok yang sekalian mau belanja juga
# Sri mau beli 4 lipstik, 9 telur, 1 beras, 7 susu
# sedangkan Ucok akan membeli 6 masker, 2 parfum, 5 sereal, 3 cimory, 7 kecap 

'''
Input :
    1. User menentukan kalimat yang akan dikerjakan
Proses :
    1. Mencari sebuah list sesuai daftar belanjaan
Output :
    1. Menghasilkan daftar belanjaan dan mengambil kata pertama list belanjaan
'''

import re

def belanja(kal):

    cari = re.findall('\d+\s\w+',kal)
    print(cari)

belanja('Bambank membeli 3 odol, 5 roti, dan 8 fanta')
belanja('Sri membeli 4 lipstik, 9 telur, 1 beras, 7 susu')
belanja('Ucok membeli 6 masker, 2 parfum, 5 sereal, 3 cimory, 7 kecap')