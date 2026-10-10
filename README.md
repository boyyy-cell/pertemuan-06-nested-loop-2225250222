# Pertemuan 06 — Nested Loop Python

**Nama:** Farid Syahputra
**NIM:** 2225250222
**Kelas:** 3F
**Program Studi:** S1 Pendidikan Matematika
**Fakultas:** FKIP
**Universitas:** Universitas Sultan Ageng Tirtayasa
**Mata Kuliah:** Algoritma dan Pemrograman
**Tahun Ajaran:** 2026/2027 Ganjil

## Tujuan

Mempelajari nested loop, pembentukan pola, akumulasi, pencacahan, dan pengujian program Python.

## Struktur Program

* `latihan/01_pasangan_indeks.py`: menampilkan pasangan indeks dan menghitung jumlah pasangan.
* `latihan/02_pola_segitiga.py`: membuat pola segitiga menggunakan bintang.
* `latihan/03_jumlah_per_baris.py`: menghitung jumlah hasil perkalian setiap baris.
* `latihan/04_hitung_pasangan.py`: menghitung pasangan yang memenuhi kondisi `i + j <= n`.
* `tugas/tabel_perkalian_dan_statistik.py`: membuat tabel perkalian dan menghitung statistik.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek.

```bash
python latihan/01_pasangan_indeks.py
python latihan/02_pola_segitiga.py
python latihan/03_jumlah_per_baris.py
python latihan/04_hitung_pasangan.py
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

1. Memasukkan bilangan bulat positif `n`.
2. Memvalidasi input menggunakan `while`.
3. Menginisialisasi `total_semua` dan `count_genap`.
4. Menggunakan nested loop untuk menghasilkan tabel perkalian.
5. Menghitung jumlah hasil perkalian setiap baris dan keseluruhan.
6. Menghitung banyak hasil perkalian genap menggunakan kondisi `if`.
7. Menampilkan tabel dan statistik setelah proses selesai.

## Hasil Pengujian

| Input n | Total keseluruhan | Banyak hasil genap | Status |
| ------: | ----------------: | -----------------: | ------ |
|       1 |                 1 |                  0 | Sesuai |
|       2 |                 9 |                  3 | Sesuai |
|       3 |                36 |                  5 | Sesuai |

## Analisis Efisiensi

Untuk nilai `n`, loop luar berjalan sebanyak `n` kali dan loop dalam berjalan sebanyak `n` kali pada setiap iterasi loop luar. Dengan demikian, badan loop dalam dijalankan sebanyak `n × n` atau `n²` kali.

## Refleksi

Akumulator untuk jumlah setiap baris harus diinisialisasi di dalam loop luar agar nilainya tidak tercampur dengan baris sebelumnya. Sebaliknya, akumulator keseluruhan dan counter hasil genap diinisialisasi sebelum kedua loop agar dapat menghitung seluruh tabel.

Kesalahan yang perlu dihindari adalah salah menempatkan indentasi, menginisialisasi akumulator pada posisi yang tidak tepat, dan menambahkan counter tanpa memeriksa kondisi.

## Kesimpulan

Nested loop dapat digunakan untuk mengolah data dalam bentuk baris dan kolom. Akumulasi digunakan untuk menghitung jumlah nilai, sedangkan pencacahan digunakan untuk menghitung banyaknya nilai yang memenuhi kondisi tertentu.

## Referensi

* Modul Bahan Ajar Pertemuan 06: Nested Loop, Pola, Akumulasi, dan Pencacahan dalam Python.
* Python Software Foundation, Python 3 Documentation.
* Visual Studio Code Documentation: Python in Visual Studio Code.
