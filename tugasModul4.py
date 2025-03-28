#Menentukan jumlah kursi
m = 17
n = 5

total_kursi = m * n
sisa_vvip = 2 * n
sisa_vip  = 3 * n
sisa_reguler = 10 * n if m>10 else(m-5)*n
sisa_ekonomi = (m - 15) * n if m > 15 else 0

kursi_terisi = 0

# tampilan layout kursi
print(" Tampilan layout kursi ")
kursi = 1
while kursi <= total_kursi : 
    baris = 1
    while baris <= n:
        if kursi < 10:
            print("", kursi, end=" ")
        else:
            print(kursi, end =" ")
        kursi += 1
        baris += 1
    print()


#Harga Tiket
print("===============Price List Tiket===============")
print("Harga_vvip    = 1.200.000")
print("Harga_vip     = 1.000.000")
print("Harga_Reguler = 800.000")
print("Harga_ekonomi = 600.000")
print("==============================================")


jumlah_pesan = int(input("Masukkan jumlah yang ingin di pesan:"))

for i in range (jumlah_pesan) :
    print(f"Pemesanan ke-{i + 1}:")
    nama = input("Masukkan nama anda:")
    no_kursi = int(input("Masukkan nomor kursi yang ingin di pesan:"))
    password = input("masukkan pasword untuk tiket:")


    if (kursi_terisi // (10**no_kursi)) % 10 == 1:
        print(f"Kursi {no_kursi} sudah dipesan! Pilih kursi lain.")
    else:
        kursi_terisi += 10**no_kursi  # Tandai kursi sebagai dipesan
        print(f"Kursi {no_kursi} berhasil dipesan!")

    if no_kursi   <= 2 * n and sisa_vvip > 0:
        kategori  = "VVIP" 
        harga     = 1200000
        sisa_vvip -= 1
    elif no_kursi <= 5 * n and sisa_vip > 0: 
        kategori  = "VIP"
        harga     = 1000000
        sisa_vip -= 1
    elif no_kursi <= 15 *n and sisa_reguler > 0:
        kategori  ="Reguler"
        harga     = 800000
        sisa_reguler -= 1
    else :
        kategori  ="Ekonomi"
        harga     = 600000
        sisa_ekonomi -= 1
    kursi_dipesan = no_kursi
    print("===============STRUK PEMESANAN TIKET KONSER===============")
    print("Nama         :", nama )
    print("Nomor Kursi  :", no_kursi)
    print("Kategori     :", kategori)
    print("Harga        :", harga)
    print("Password     :", password)
    print("==========================================================")

print("Tampilan layout kursi setelah Pemesanan")
kursi = 1
baris = 1

while baris <= m:
    kolom = 1
    while kolom <= n:
        if (kursi_terisi // (10**kursi)) % 10 == 1:  # Cek apakah kursi dipesan
            print(" x", end=" ")
        else:
            if kursi < 10:
                print('', kursi, end=" ")
            else:
                print(kursi, end=" ")
        kursi += 1
        kolom += 1
    print()
    baris += 1

# Menampilkan sisa kursi
print("========================Sisa Kursi=========================")
print("VVIP     :", sisa_vvip)
print("VIP      :", sisa_vip)
print("Reguler  :", sisa_reguler)
print("Ekonomi  :", sisa_ekonomi)
print("===============Terimakasih Telah Pesan Tiket===============")