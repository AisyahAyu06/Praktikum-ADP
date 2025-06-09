import json

FILENAME = "data_keuangan.txt"

open(FILENAME, "a").close()  
if open(FILENAME).read().strip() == "":
    open(FILENAME, "w").write("[]")


# Fungsi untuk membaca data
def baca_data():
    with open(FILENAME, "r") as file:
        return json.load(file)

# Fungsi untuk menyimpan data 
def simpan_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk menambah data keuangan
def tambah_data():
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    keterangan = input("Keterangan: ")
    jumlah = input("Jumlah uang: ")
    tipe = input("Tipe (pemasukan/pengeluaran): ")

    entry = {
        "tanggal": tanggal,
        "keterangan": keterangan,
        "jumlah": jumlah,
        "tipe": tipe
    }

    data = baca_data()
    data.append(entry)
    simpan_data(data)
    print("Data berhasil ditambahkan.")

# Fungsi untuk menampilkan semua data
def tampilkan_data():
    data = baca_data()
    if not data:
        print("Belum ada data.")
        return
    print("\nData Keuangan:")
    print("-" * 60)

    i = 1
    for entry in data:
        print(f"{i}. {entry['tanggal']} | {entry['keterangan']} | {entry['jumlah']} | {entry['tipe']}")
        i += 1

    print("-" * 60)

# Fungsi untuk menghapus data berdasarkan keterangan
def hapus_data():
    nama = input("Keterangan yang ingin dihapus: ")
    data = baca_data()
    data = [m for m in data if m["keterangan"] != nama]
    simpan_data(data)
    print("Data berhasil dihapus (jika ditemukan).")

# Menu utama
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah data keuangan")
        print("2. Hapus data keuangan")
        print("3. Tampilkan semua data")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            hapus_data()
        elif pilihan == "3":
            tampilkan_data()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

menu()
