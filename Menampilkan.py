import pandas as pd
from prosses import ambil_data

#menapilkan data
def tampilkan_data(pengarah):
    print("""
          =============================================
          Berikut adalah tabel yang ada pada Database
          households
          financial_records
          =============================================
          
          Tabel apa yang mau ditampilkan
          1. households
          2. financial_records
          3. Gabungan
          """)
    while True:
        try:
            tabel_apa = int(input("Masukkan nomor tabel yang akan ditampilkan: "))
            if tabel_apa == 1:
                df = ambil_data(tabel_apa, pengarah)
                print(df)
                break
            elif tabel_apa == 2:
                df = ambil_data(tabel_apa, pengarah)
                print(df)
                break
            elif tabel_apa == 3:
                df = ambil_data(tabel_apa, pengarah)
                print(df)
                break
        except (IndexError, ValueError):
            print("'Masukkan angka berdasarkan tabel")
            continue