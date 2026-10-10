# Tugas 3: Tabel Perkalian dan Statistik
# Pertemuan 06 - Algoritma dan Pemrograman

print("Tabel Perkalian dan Statistik")

n = int(input("Masukkan n: "))

# Validasi agar n harus positif.
while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

# Akumulator dan counter keseluruhan.
total_semua = 0
count_genap = 0

# Loop luar mengatur baris tabel.
for i in range(1, n + 1):
    total_baris = 0

    # Loop dalam mengatur kolom tabel.
    for j in range(1, n + 1):
        hasil = i * j

        # Menampilkan hasil perkalian.
        print(f"{hasil:4}", end="")

        # Akumulasi jumlah baris dan keseluruhan.
        total_baris += hasil
        total_semua += hasil

        # Pencacahan hasil perkalian genap.
        if hasil % 2 == 0:
            count_genap += 1

    # Ditampilkan setelah satu baris selesai.
    print(f"   | jumlah baris = {total_baris}")

# Statistik keseluruhan.
print(f"\nTotal seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
