# Latihan 3: Jumlah per Baris
# total_baris direset setiap kali loop luar berpindah baris.

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        hasil = i * j
        total_baris += hasil

    print(f"Jumlah baris {i} = {total_baris}")
