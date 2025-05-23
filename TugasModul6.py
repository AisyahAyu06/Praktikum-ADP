# Program Input Titik dan Hitung Jarak Kuadrat antar Titik
valid = False
while valid == False:
    n_input = input("Masukkan jumlah titik (n): ")
    angka = True
    if n_input == "":
        angka = False
    else:
        i = 0
        while i < len(n_input):
            if n_input[i] not in "0123456789":
                angka = False
            i = i + 1

    if angka == True:
        n = int(n_input)
        valid = True
    else:
        print("Input tidak valid! Harus angka bulat positif.")

# Input koordinat titik
titik = []
i = 0
while i < n:
    print("\nTitik ke-", i, " (format: x,y)")
    benar = False
    while benar == False:
        data = input("  Masukkan koordinat: ")

        # Cari posisi koma
        posisi_koma = -1
        ada_koma = False
        j = 0
        while j < len(data):
            if data[j] == ",":
                posisi_koma = j
                ada_koma = True
            j = j + 1

        if ada_koma == False:
            print(" Format salah! Harus ada koma (x,y).")
            continue

        x_str = data[:posisi_koma]
        y_str = data[posisi_koma + 1:]

        x_valid = True
        y_valid = True

        if x_str == "" or y_str == "":
            x_valid = False
            y_valid = False
        else:
            for karakter in x_str:
                if karakter not in "0123456789-":
                    x_valid = False
            for karakter in y_str:
                if karakter not in "0123456789-":
                    y_valid = False

        if x_valid == True and y_valid == True:
            x = int(x_str)
            y = int(y_str)
            titik.append([x, y])
            benar = True
        else:
            print("Koordinat harus berupa angka.")

    i = i + 1


print("\n Jarak Kuadrat antar Titik:")
i = 0
while i < n:
    j = i + 1
    while j < n:
        dx = titik[i][0] - titik[j][0]
        dy = titik[i][1] - titik[j][1]
        jarak_kuadrat = dx * dx + dy * dy
        print("  Jarak dari Titik", i, "ke Titik", j, "=", jarak_kuadrat)
        j = j + 1
    i = i + 1
