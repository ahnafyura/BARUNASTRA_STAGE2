# BARUNASTRA_STAGE2

# Task 1 — Payroll System

## Cara Kerja 

* Program memodelkan karyawan menggunakan sebuah class `Employee` yang mendefinisikan antarmuka umum pada Abstract Base Class (ABC).
* Dua fungsi utamanya meliputi:

  * `Salaried` = menyimpan gaji tahunan. Perhitungan gaji mingguan dilakukan dengan membagi gaji tahunan dengan 52.
  * `Hourly` = menyimpan tarif per jam dan jumlah jam kerja. Perhitungan gaji mingguan dilakukan dengan mengalikan tarif per jam dengan jam kerja.

* Program membaca sejumlah input karyawan, membuat objek yang sesuai (Salaried atau Hourly) dan menyimpan ke daftar.
* Untuk setiap objek, program memanggil metode yang sama `calculate_weekly_pay` sehingga menerapkan **polymorphism**.
* output akan terdisplay sebagai tabel ASCII yang merangkum informasi penting setiap karyawan beserta gaji mingguan para karyawan.

## Aturan Perhitungan

* `Salaried.weekly_pay = annual_salary / 52`
* `Hourly.weekly_pay = rate_per_hour * hours_worked`

## Contoh Input (konseptual)

```
3
Salaried Budi_Speed A001 52000
Hourly Bolang B001 20 40
Hourly Bryan B002 25 30
```

## Output (tabel ASCII)

<table width="100%">
  <tr>
    <td width="50%" align="center" valign="top">
      <h3> Neo4j Graph </h3>
      <img src="img/2.png" alt="Normal Case" width="100%" style="border-radius: 5px;">
    </td>
    <td width="50%" align="center" valign="top">
      <h3> Command-Line Pipeline Orchestrator </h3>
      <img src="img/1.png" alt="CLI Table Interface" width="100%" style="border-radius: 5px;">
    </td>
  </tr>
</table>

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

## Output (daftar produk + ringkasan)

<table width="100%">
  <tr>
    <td width="50%" align="center" valign="top">
      <h3> Neo4j Graph </h3>
      <img src="img/4.png" alt="Normal Case" width="100%" style="border-radius: 5px;">
    </td>
    <td width="50%" align="center" valign="top">
      <h3> Command-Line Pipeline Orchestrator </h3>
      <img src="img/3.png" alt="CLI Table Interface" width="100%" style="border-radius: 5px;">
    </td>
  </tr>
</table>

---

# Penjelasan Singkat Konsep OOP yang Terlihat pada Output

* **Encapsulation** terlihat dari atribut objek yang diakses melalui properti/metode sehingga format output tetap konsisten.
* **Inheritance** memungkinkan `Salaried`/`Hourly` dan `Drink`/`Snack` berbagi perilaku dasar dari kelas induk.
* **Polymorphism** memungkinkan fungsi yang sama (`calculate_weekly_pay`, `get_info`) dipanggil pada objek berbeda tanpa perlu memeriksa tipe secara eksplisit.
* **Abstraction** menjaga antarmuka minimal yang harus diimplementasikan oleh kelas turunan.

---

Dokumentasi ini ditujukan sebagai lampiran penjelasan program untuk laporan tugas Barunastra Stage 2.
