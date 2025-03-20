print("==========Menghitung P(N(t) = n)==========")
lambda_t = float(input("Masukkan nilai lambda * t :"))
M = int(input("Masukkan Nilai M :"))
e = 2.71828
# Iterasi untuk setiap nilai dari 0 hingga M
for n in range (M + 1) :
# menghitung faktorial
    faktorial = 1
    for i in range(1, n + 1):
        faktorial *= i

    # Menghitung P(N(t) = n)    
    P_n = (e**(-lambda_t) )* ((lambda_t**n) / faktorial)
    # Menampilkan hasil
    print(f"P(N(t) = {n}) = {P_n}")