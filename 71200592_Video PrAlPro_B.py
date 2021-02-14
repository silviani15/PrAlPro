# Silviani Vanesha / 71200592
# Universitas Kristen Duta Wacana
# Informatika / 20

# Seorang Pedagang membeli 20 kg salak seharga Rp140.000 
# setengahnya ia jual kembali dengan harga Rp10.000 per kg dan 
# setengahnya lagi ia jual dengan harga Rp6.000 karena sudah mulai rusak 
# jika seluruh salak terjual habis maka Keuntungan yang diperoleh pedagang adalah
        

# Input : 
        # 1. Salak 20 kg 
        # 2. Harga awal Rp. 140.000
harga_awal = int(input('Harga Awal = ')) 
        # 3. Setengahnya Dijual lagi per kilo = 10.000
        # 4. Setengahnya Harga Salak yang Rusak per kilo = 6.000
# Proses :
        # 1. Mencari Jumlah harga jual ke 1
        # 2. Mencari Jumlah harga jual ke 2
        # 3. Menghitung Total Harga dengan Menjumlahkan Harga jual 1 dan 2
# Output : 
        # 1. Keuntungan yang diperoleh dengan mengurangkan Total Harga Terbaru dengan Harga Awal


a = int(input('Masukkan harga jual ke 1 : '))  
b = int(input('Masukkan satuan (kg) : '))       
c = a * b
print('Jumlah Harga Jual ke 1 = ', c)

        # a = Harga jual ke 1
        # b = Harga satuan (dalam bentuk kg)
        # c = Jumlah harga jual ke 1

d = int(input('Masukkan harga jual ke 2 : '))          
e = int(input('Masukkan satuan : '))
f = d * e
print('Jumlah Harga Jual ke 2 = ', f)

        # d = Harga jual ke 2
        # e = Sama dengan program b
        # f = Jumlah harga jual ke 2

g = c + f
print('Total Harga = ', g)

         # g = Total Harga Terbaru

h = g - harga_awal
print('Keuntungan yang diperoleh adalah ', h)

        # h = Keuntungan