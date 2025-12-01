# BARUNASTRA_STAGE2

# Task 1 — Payroll System

## Cara Kerja (Ringkas)

* Program memodelkan karyawan menggunakan sebuah **Abstract Base Class** `Employee` yang mendefinisikan antarmuka umum.
* Dua turunan utama:

  * `Salaried` — menyimpan gaji tahunan. Perhitungan gaji mingguan dilakukan dengan membagi gaji tahunan dengan 52.
  * `Hourly` — menyimpan tarif per jam dan jumlah jam kerja. Perhitungan gaji mingguan dilakukan dengan mengalikan tarif per jam dengan jam kerja.
* Program membaca sejumlah entri karyawan, membuat objek yang sesuai (Salaried atau Hourly) dan menyimpan ke daftar.
* Untuk setiap objek, program memanggil metode yang sama (misalnya `calculate_weekly_pay`) sehingga menerapkan **polymorphism**.
* Hasil akhir dirender sebagai tabel ASCII yang merangkum informasi penting setiap karyawan beserta gaji mingguan mereka.

## Aturan Perhitungan (Ringkas)

* `Salaried.weekly_pay = annual_salary / 52`
* `Hourly.weekly_pay = rate_per_hour * hours_worked`
* (Program melewatkan entri dengan tipe yang tidak dikenali untuk mencegah crash dan menjaga integritas data.)

## Contoh Input (konseptual)

```
3
Salaried Budi A001 52000
Hourly Felix B001 20 40
Hourly Leon B002 25 30
```

## Contoh Output (tabel ASCII)

```
+-------+-------+--------+--------------+
| ID    | Name  | Type   | Weekly Pay   |
+-------+-------+--------+--------------+
| A001  | Budi  | Salaried | Rp 1,000    |
| B001  | Felix | Hourly   | Rp   800    |
| B002  | Leon  | Hourly   | Rp   750    |
+-------+-------+--------+--------------+
|                    Total Payroll | Rp 2,550    |
+----------------------------------+--------------+
```

Keterangan: kolom menunjukkan ID, nama, tipe kontrak, dan gaji mingguan yang sudah diformat secara sederhana. Baris total menunjukkan jumlah gaji mingguan seluruh karyawan.

---

# Task 2 — Vending Machine System

## Cara Kerja (Ringkas)

* Program memodelkan produk menggunakan **Abstract Base Class** `Product` yang menyimpan atribut dasar seperti nama.
* Dua turunan utama:

  * `Drink` — atribut tambahan `volume` (dalam ml).
  * `Snack` — atribut tambahan `calories` (dalam kcal).
* Program membaca daftar produk, mengabaikan baris dengan tipe yang tidak dikenali (typo protection), lalu menyimpan objek yang valid.
* Program menampilkan daftar produk yang terdaftar dan menghitung agregat:

  * Total volume minuman (ml)
  * Total kalori semua snack (kcal)

## Contoh Input (konseptual)

```
3
Drink Water 500
Snack Chips 300
Drink Soda 350
```

## Contoh Output (daftar produk + ringkasan)

```
Products
1. Drink  - Water  - 500 ml
2. Snack  - Chips  - 300 kcal
3. Drink  - Soda   - 350 ml

Summary
- Total drink volume  : 850 ml
- Total snack calories : 300 kcal
```

Keterangan: daftar menunjukkan setiap item dengan tipe, nama, dan nilai atribut spesifik. Ringkasan memberikan total agregat yang relevan.

---

# Penjelasan Singkat Konsep OOP yang Terlihat pada Output

* **Encapsulation** terlihat dari atribut objek yang diakses melalui properti/metode sehingga format output tetap konsisten.
* **Inheritance** memungkinkan `Salaried`/`Hourly` dan `Drink`/`Snack` berbagi perilaku dasar dari kelas induk.
* **Polymorphism** memungkinkan fungsi yang sama (`calculate_weekly_pay`, `get_info`) dipanggil pada objek berbeda tanpa perlu memeriksa tipe secara eksplisit.
* **Abstraction** menjaga antarmuka minimal yang harus diimplementasikan oleh kelas turunan.

---

Dokumentasi ini ditujukan sebagai lampiran penjelasan program untuk laporan tugas Barunastra Stage 2. Jika ingin, saya bisa menyesuaikan gaya bahasa (lebih teknis atau lebih ringkas), menambah contoh kasus tepi (misal jam lembur, entri invalid) atau menambahkan contoh keluaran dalam format CSV/JSON sebagai lampiran.

