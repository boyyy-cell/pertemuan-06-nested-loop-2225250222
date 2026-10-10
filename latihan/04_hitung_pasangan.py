# Latihan 4: Menghitung Pasangan
# Counter bertambah jika i + j <= n.

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

count = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")
