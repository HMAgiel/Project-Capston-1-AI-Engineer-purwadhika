from koneksi import database
from Menampilkan import tampilkan_data
from statistik import statistik, pilihan_grup
from update_data import update_data, tambah_data, hapus_data
from visualisasi import buat_grafik
import warnings

def main():
    koneksi = database()
    warnings.filterwarnings("ignore")
    if not koneksi:
        return

    try:
        while True:
            print("\n=== MENU UTAMA ===")
            print("1. Tampilkan Data kependudukan")
            print("2. Statistik Kependudukan")
            print("3. Tampilkan berdasarkan grup")
            print("4. Mengubah data")
            print("5. Tambahkan data baru")
            print("6. Hapus Data")
            print("7. Membuat grafik statistik")
            print("8. Keluar dari aplikasi")

            pilihan = input("Masukkan pilihan Anda (1-8): ")

            if pilihan == "1":
                tampilkan_data(koneksi)
            elif pilihan == "2":
                statistik(koneksi)
            elif pilihan == "3":
                pilihan_grup(koneksi)
            elif pilihan == "4":
                update_data(koneksi)
            elif pilihan == "5":
                tambah_data(koneksi)
            elif pilihan == "6":
                hapus_data(koneksi)
            elif pilihan == "7":
                buat_grafik(koneksi)
            elif pilihan == "8":
                print("Terima kasih, program dihentikan.")
                break  
            else:
                print("Pilihan tidak valid. Silakan masukkan angka 1-7.")

    finally:
        koneksi.close()
        print("Koneksi database ditutup")
        

if __name__ == "__main__":
    main()