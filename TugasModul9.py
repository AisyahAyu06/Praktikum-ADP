from termcolor import cprint
import time
import os

# Ukuran bendera dan tiang
tinggi_bendera = 6
lebar_bendera = 20
tinggi_tiang = 10 
tiang = " "

# Pola gelombang untuk efek berkibar
pola_gelombang = [
    [0, 1, 2, 1, 0, 1],
    [1, 2, 1, 0, 1, 2],
    [2, 1, 0, 1, 2, 1],
    [1, 0, 1, 2, 1, 0],
]

def bersihkan_layar():
    os.system('clear')

def gambar_bendera(gelombang):
    for i in range(tinggi_bendera):
        warna = 'red' if i < tinggi_bendera // 2 else 'white'
        panjang = lebar_bendera - gelombang[i]
        cprint(" " * (len(tiang)), 'blue', 'on_blue', end="")
        cprint(" " * panjang, warna, f'on_{warna}')

def gambar_tiang():
    for _ in range(tinggi_tiang):
        cprint(tiang, 'blue', 'on_blue')

# Animasi bendera berkibar dengan tiang di bawah bendera
for frame in range(20):
    bersihkan_layar()
    gelombang = pola_gelombang[frame % len(pola_gelombang)]
    gambar_bendera(gelombang)  
    gambar_tiang()            
    time.sleep(0.2)
