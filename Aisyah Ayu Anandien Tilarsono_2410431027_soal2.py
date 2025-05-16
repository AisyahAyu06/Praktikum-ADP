# Tiga array satu dimensi
daftar_nim = []
daftar_nama = []
daftar_nilai = []

while True:
    print("=======================================")
    print("||  MENU MANAJEMEN NILAI MAHASISWA   ||")
    print("||===||==============================||")
    print("||1. ||          Tambah Data         ||")
    print("||===||==============================||")
    print("||2. ||          Hapus  Data         ||")
    print("||===||==============================||")
    print("||3. ||        Tampilkan Data        ||")
    print("||===||==============================||")
    print("||4. ||             Keluar           ||")
    print("=======================================")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        nilai = float(input("Masukkan Nilai: "))

        daftar_nim.append(nim)
        daftar_nama.append(nama)
        daftar_nilai.append(nilai)
        print("Data berhasil ditambahkan.\n")

    elif pilihan == "2":
        nim_hapus = input("Masukkan NIM yang akan dihapus: ")
        posisi = 0
        ketemu = False
        for nim in daftar_nim:
            if nim == nim_hapus:
                del daftar_nim[posisi]
                del daftar_nama[posisi]
                del daftar_nilai[posisi]
                print("Data berhasil dihapus.\n")
                ketemu = True
                break
            else:
                posisi += 1
        if not ketemu:
            print("Data tidak ditemukan.\n")

    elif pilihan == "3":
        print("=======================================================")
        print("||                  Data Mahasiswa                   ||")
        print("=====================================================||")
        print("||   NIM                 Nama                Nilai   ||")
        jumlah = len(daftar_nim)
        hitung = 0
        while hitung < jumlah:
            nim = daftar_nim.pop(0)
            nama = daftar_nama.pop(0)
            nilai = daftar_nilai.pop(0)

            # Cetak data dengan spasi biasa, bukan \t
            print("||", nim, "       ", nama, "  ", nilai, "    ||")

            daftar_nim.append(nim)
            daftar_nama.append(nama)
            daftar_nilai.append(nilai)
            hitung += 1
        print()

    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih antara 1–4.\n")
