# 🏘️ Sistem Informasi Kependudukan Indonesia

Aplikasi berbasis Python untuk mengelola dan menganalisis data kependudukan Indonesia, terhubung dengan database MySQL. Aplikasi ini memungkinkan pengguna untuk melihat, mengelola, menganalisis secara statistik, dan memvisualisasikan data rumah tangga beserta rekam finansialnya.

---

## 📋 Daftar Isi

- [Fitur](#-fitur)
- [Struktur Proyek](#-struktur-proyek)
- [Struktur Database](#️-struktur-database)
- [Prasyarat](#-prasyarat)
- [Instalasi](#-instalasi)
- [Konfigurasi](#-konfigurasi)
- [Cara Penggunaan](#-cara-penggunaan)
- [Penjelasan Modul](#-penjelasan-modul)

---

## ✨ Fitur

- **Tampilkan Data** — Lihat tabel `households`, `financial_records`, atau keduanya (gabungan JOIN)
- **Statistik** — Hitung rata-rata, median, dan modus dari kolom numerik
- **Grup & Agregasi** — Kelompokkan data berdasarkan kategori dan agregasi kolom numerik pilihan
- **Update Data** — Ubah nilai pada kolom tertentu berdasarkan nama kepala keluarga
- **Tambah Data** — Masukkan data rumah tangga baru beserta data finansialnya
- **Hapus Data** — Hapus data berdasarkan nama kepala keluarga (cascade ke `financial_records`)
- **Visualisasi** — Buat grafik histogram, boxplot, dan barplot menggunakan Matplotlib & Seaborn

---

## 📁 Struktur Proyek

```
├── main.py              # Entry point — menu utama aplikasi
├── koneksi.py           # Konfigurasi koneksi database MySQL
├── prosses.py           # Fungsi pengambilan data (query SQL → DataFrame)
├── Menampilkan.py       # Logika tampilkan data ke layar
├── statistik.py         # Perhitungan statistik & pengelompokan (grup)
├── update_data.py       # Operasi CRUD: update, tambah, hapus data
├── visualisasi.py       # Pembuatan grafik (histogram, boxplot, barplot)
├── cek_input.py         # Validasi dan sanitasi input pengguna
├── Kependudukan.sql     # Script SQL: buat database, tabel, dan data awal (40 baris)
└── pake_funtion.ipynb   # Notebook eksplorasi fungsi-fungsi yang digunakan
```

---

## 🗄️ Struktur Database

Database: `data_kependudukan_indonesia`

### Tabel `households`

| Kolom                     | Tipe            | Keterangan                        |
|---------------------------|-----------------|-----------------------------------|
| `id`                      | INT (PK, Auto)  | ID unik rumah tangga              |
| `head_name`               | VARCHAR(100)    | Nama kepala keluarga              |
| `head_age`                | INT             | Usia kepala keluarga              |
| `education_level`         | VARCHAR(50)     | Tingkat pendidikan                |
| `marital_status`          | VARCHAR(20)     | Status pernikahan                 |
| `num_children`            | INT             | Jumlah anak                       |
| `house_size_m2`           | INT             | Luas rumah (m²)                   |
| `monthly_expense_estimate`| DECIMAL(12,2)   | Estimasi pengeluaran bulanan (Rp) |

### Tabel `financial_records`

| Kolom             | Tipe           | Keterangan                              |
|-------------------|----------------|-----------------------------------------|
| `id`              | INT (PK, Auto) | ID unik catatan finansial               |
| `household_id`    | INT (FK)       | Referensi ke `households.id`            |
| `main_job`        | VARCHAR(100)   | Pekerjaan utama                         |
| `monthly_income`  | DECIMAL(12,2)  | Pendapatan bulanan (Rp)                 |
| `monthly_expense` | DECIMAL(12,2)  | Pengeluaran bulanan aktual (Rp)         |
| `savings`         | DECIMAL(12,2)  | Jumlah tabungan (Rp)                    |
| `debt`            | DECIMAL(12,2)  | Jumlah hutang (Rp)                      |

> Relasi: `financial_records.household_id` → `households.id` dengan `ON DELETE CASCADE` dan `ON UPDATE CASCADE`

---

## 🔧 Prasyarat

Pastikan sistem Anda memiliki:

- Python **3.8+**
- MySQL Server **5.7+** atau **8.0+**
- pip (Python package manager)

### Library Python yang dibutuhkan

```
mysql-connector-python
pandas
matplotlib
seaborn
```

---

## 🚀 Instalasi

**1. Clone repository ini**

```bash
git clone https://github.com/username/sistem-kependudukan.git
cd sistem-kependudukan
```

**2. Install dependensi Python**

```bash
pip install mysql-connector-python pandas matplotlib seaborn
```

**3. Buat database dan isi data awal**

Login ke MySQL dan jalankan script SQL:

```bash
mysql -u root -p < Kependudukan.sql
```

Atau jalankan isi file `Kependudukan.sql` langsung melalui MySQL Workbench / DBeaver / tool lainnya.

---

## ⚙️ Konfigurasi

Edit file `koneksi.py` dan sesuaikan kredensial database Anda:

```python
# koneksi.py
import mysql.connector

def database():
    DATA = mysql.connector.connect(
        host     = "localhost",   # Ganti jika host berbeda
        user     = "root",        # Username MySQL Anda
        password = "password",    # Password MySQL Anda
        database = "data_kependudukan_indonesia"
    )
    return DATA
```

---

## 🖥️ Cara Penggunaan

Jalankan aplikasi dari terminal:

```bash
python main.py
```

Anda akan disambut dengan menu utama:

```
=== MENU UTAMA ===
1. Tampilkan Data kependudukan
2. Statistik Kependudukan
3. Tampilkan berdasarkan grup
4. Mengubah data
5. Tambahkan data baru
6. Hapus Data
7. Membuat grafik statistik
8. Keluar dari aplikasi

Masukkan pilihan Anda (1-8):
```

Ikuti petunjuk yang muncul di layar untuk setiap menu.

---

## 📦 Penjelasan Modul

### `main.py`
Entry point aplikasi. Menginisialisasi koneksi database, menampilkan menu utama, dan mendistribusikan pilihan pengguna ke modul yang sesuai. Koneksi database selalu ditutup setelah program selesai (blok `finally`).

### `koneksi.py`
Berisi satu fungsi `database()` yang mengembalikan objek koneksi MySQL menggunakan `mysql.connector`.

### `prosses.py`
Menyediakan fungsi inti pengambilan data:
- `ambil_data(input_user, pengarah)` — menjalankan query SQL dan mengembalikan DataFrame pandas. Mendukung 3 pilihan: tabel `households` (1), `financial_records` (2), atau gabungan keduanya via LEFT JOIN (3).
- `ambil_numerik(df)` — menyaring kolom-kolom numerik dari DataFrame dan menampilkan daftarnya.

### `Menampilkan.py`
Menangani pilihan tabel yang akan ditampilkan ke layar, memanggil `ambil_data()` dari `prosses.py`, lalu mencetak hasilnya sebagai tabel pandas.

### `statistik.py`
- `statistik(pengarah)` — menghitung rata-rata, median, atau modus dari kolom numerik pilihan pengguna.
- `pilihan_grup(pengarah)` — mengelompokkan data berdasarkan kolom kategori (misalnya: `education_level`, `marital_status`) dan mengagregasi kolom numerik yang dipilih dengan fungsi rata-rata.

### `update_data.py`
Berisi tiga fungsi CRUD:
- `update_data(pengarah)` — mengubah nilai pada kolom tertentu untuk data yang diidentifikasi berdasarkan nama kepala keluarga.
- `tambah_data(pengarah)` — menambahkan baris baru ke kedua tabel (`households` dan `financial_records`) secara transaksional.
- `hapus_data(pengarah)` — menghapus data rumah tangga berdasarkan nama; data di `financial_records` ikut terhapus otomatis karena relasi CASCADE.

### `visualisasi.py`
Menyediakan tiga jenis grafik menggunakan Matplotlib dan Seaborn:
- **Histogram** — distribusi frekuensi kolom numerik/kategori dengan kurva KDE
- **Boxplot** — sebaran dan outlier dari kolom pilihan
- **Barplot** — rata-rata nilai numerik dikelompokkan berdasarkan kolom kategori

### `cek_input.py`
Kumpulan fungsi validasi input untuk memastikan data yang dimasukkan pengguna valid:
- `cek_input_angka()` — memastikan input berupa angka (integer atau float)
- `cek_nama()` — memvalidasi nama kepala keluarga ada di database
- `cek_keyword_nama()` — mencari nama berdasarkan kata kunci (case-insensitive)
- `cek_input_kolom()` — memvalidasi nomor kolom yang dipilih tidak melebihi jumlah kolom
- `cek_jenis_kolom()` — menyesuaikan tipe input (int/float/string) dengan tipe data kolom

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan analisis data kependudukan. Bebas digunakan dan dimodifikasi.
