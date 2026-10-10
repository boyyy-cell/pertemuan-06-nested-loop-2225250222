# Latihan 2: Pola Segitiga
# Loop luar mengatur baris, sedangkan loop dalam mencetak bintang.

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("Masukkan n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()