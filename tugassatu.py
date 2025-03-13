print("==========PEMESANAN ONLINE=========")
print ("==========RESTO JUNKFOOD==========")


print ("===============================================================================================================|")
print ("| Nama Paket  |                                       Isi Paket                                       | Harga  |")
print ("|=============|=======================================================================================|========|")
print ("| Paket Ceria | Beef Burger, French Fries, Fruit Tea                                                  | 50000  |")
print ("| Paket Hemat | chicken Burger, Ice Tea                                                               | 25000  |")
print ("| Paket Kids  | Mini burger, nugget, Ice Milo                                                         | 40000  |")
print ("| Paket Couple| Beef Burger, Spaghetti, French Fries, Ice Tea, Coca-Cola                              | 80000  |")
print ("| Paket Combo | Chicken Burger,Beef Burger, French Fries, Fried Chicken, fruit tea, Ice Tea, Coca-cola| 165000 |")
print ("===============================================================================================================|")

#Tampilan 2
print("=====Masukkan Data=====")
Nama                 = input("Nama                    :" )
No_Telepon           = int(input("No Telepon              :"))
Alamat_Pengiriman    = input("Alamat Pengiriman       :")
Paket_Makanan        = input ("Pesan Paket Menu        :") 
Jumlah_Pesan         = int(input("Jumlah paket yang dibeli: "))

# Daftar paket makanan
if Paket_Makanan == "Paket Ceria":
    Isi_Paket = ("Beef Burger, French Fries, Fruit Tea ")
    Harga     = 50000
elif Paket_Makanan == "Paket Hemat" :
    Isi_Paket = ("chicken Burger, Ice Tea ")
    Harga     = 25000
elif Paket_Makanan  == "Paket Kids" :
    Isi_Paket = ("Mini burger, nugget, Ice Milo")
    Harga     = 40000
elif Paket_Makanan =="Paket Couple" :
    Isi_Paket = ("Beef Burger, Spaghetti, French Fries, Ice Tea, Coca cola")
    Harga     = 80000
elif Paket_Makanan =="Paket Combo":
    Isi_Paket = ("Chicken Burger,Beef Burger, French Fries, Fried Chicken, fruit tea, Ice Tea, Coca-cola")
    Harga     = 165000
else :
    print("Tidak Tersedia")

#Menghitung Total Harga
Harga_Paket =  Harga
Total_Harga =  Jumlah_Pesan  * Harga_Paket 

#Pajak (10%)
Pajak = Total_Harga * 10/100

# Biaya Pengiriman
Biaya_Pengiriman = 25000
if Total_Harga < 150000 :
    Biaya_Pengiriman = 25000
else :
    Biaya_Pengiriman = 0

Total_Akhir = Total_Harga + Pajak + Biaya_Pengiriman 

#menampilkan struk pemesanan
print("========Struk Pemesanan========")
print("Nama             : ", Nama )
print("Nomor Telepon    : ", No_Telepon)
print("Alamat Pengiriman: ", Alamat_Pengiriman)
print("Detail Pesanan   : ", Paket_Makanan )
print(Isi_Paket)
print("Jumlah Pesan     : ", Jumlah_Pesan)
print("=====================================================================================")
print("total Harga      : ", Total_Harga)
print("Pajak (10%)      : ", Pajak )
print("Biaya Pengiriman : ", Biaya_Pengiriman)
print("=====================================================================================")
print("Total Akhir      : ", Total_Akhir)
print("===============================Terimakasih Telah Pesan===============================")
print("===================================Selamat Kembali===================================")