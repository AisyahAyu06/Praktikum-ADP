def input_data():
    n = int(input("Masukkan jumlah praktikan: "))
    data = []
    for i in range(n):
        print(f"Praktikan {i+1}")
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai Pretest: "))
        posttest = float(input("Nilai Posttest: "))
        tugas = float(input("Nilai Tugas: "))
        bonus = float(input("Nilai Bonus: "))
        nilai_akhir = 0.25 * pretest + 0.25 * posttest + 0.5 * tugas + bonus
        data.append([nama, nim, nilai_akhir])
    return data

def hitung_rata2(data):
    total = 0
    for i in range(len(data)):
        total += data[i][2]
    return total / len(data)

def urutkan_praktikan(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n-1-i):
            if data[j][2] < data[j+1][2]:
                data[j], data[j+1] = data[j+1], data[j]

def tampilkan_data(data):
    print("\n+-----------------+-------------+--------------+-----------+")
    print("| {:15} | {:11} | {:12} | {:9} |".format("Nama", "NIM", "Nilai Akhir", "Peringkat"))
    print("+-----------------+-------------+--------------+-----------+")
    for i in range(len(data)):
        print("| {:15} | {:11} | {:12.2f} | {:9} |".format(data[i][0], data[i][1], data[i][2], i+1))
    print("+-----------------+-------------+--------------+-----------+")
    rata2 = hitung_rata2(data)
    print("Rata-rata nilai akhir: {:.2f}".format(rata2))

praktikan = input_data()
urutkan_praktikan(praktikan)
tampilkan_data(praktikan)
