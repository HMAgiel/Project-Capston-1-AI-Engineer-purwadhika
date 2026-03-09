import pandas as pd
from prosses import ambil_data, ambil_numerik

#Statistik
def statistik(pengarah):
    df = ambil_data(3, pengarah)
    print("""
          ============================================
          berikut perhitungan statistik yang tersedia
          ============================================
          1. Rata-rata
          2. median
          3. modus
          """)
    while True:
        try:
            input_user = int(input("Masukkan angka ingin statistik yang mana (1-3): "))
            while True:
                    try:
                        if input_user == 1:
                            df_numerik = ambil_numerik(df)
                            input_angka = int(input("Masukan angka kolom mana yang mau dibuat statistik: "))
                            rata = df_numerik[df_numerik.columns[input_angka-1]].mean()
                            print(f"Nilai rata-rata dari {df_numerik.columns[input_angka-1]} adalah: {rata}")
                            break 
                        
                        elif input_user == 2:
                            df_numerik = ambil_numerik(df)
                            input_angka = int(input("Masukan angka kolom mana yang mau dibuat statistik: "))
                            med = df_numerik[df_numerik.columns[input_angka-1]].median()
                            print(f"Nilai median dari {df_numerik.columns[input_angka-1]} adalah: {med}")
                            break 
                        
                        elif input_user == 3:
                            print("\nKolom numerik yang tersedia:")
                            df2 = df.drop(columns=['head_name'])
                            for i, kolom in enumerate(df2, 1):
                                print(f"{i}. {kolom}")
                            input_angka = int(input("Masukan angka kolom mana yang mau dibuat statistik: "))
                            modus = df2[df2.columns[input_angka-1]].mode()
                            print(f"Nilai modus dari {df2.columns[input_angka-1]} adalah: {modus}")
                            break
                    except (IndexError, ValueError):
                        print("Masukan angka sesuai nomor kolom")
                        continue
            break
        except (IndexError, ValueError):
            print("Masukkan angka sesuai pilihan (1 - 3)")
            continue 

#memilih sesuai grup agregat
def pilihan_grup(pengarah):
    df = ambil_data(3, pengarah)
    df_numerik = df.apply(pd.to_numeric, errors='coerce').dropna(axis=1)
    numerik_kolom = df_numerik.columns
    df_tanpa_nama = df.drop(columns=['head_name'])
    df_kategori = df_tanpa_nama.select_dtypes(include=['category', 'object'])
    print("""
          =====================================================================
          Berikut adalah kolom yang tersedia untuk di grup berdasarkan kategori
          =====================================================================
          """)
    for i, kolom in enumerate(df_kategori, 1):
        print(f"{i}. {kolom}")
    
    while True:
          try:
                input_kategori = int(input("Masukkan angka kolom yang ingin dijadikan kategori: "))
                if 1 <= input_kategori <= len(df_kategori.columns):
                    break
                else:
                    print("Masukkan angka sesaui nomor kolom")
          except ValueError:
                print("Input harus berupa angka")
      
    print("""
          =====================================================================
          Berikut adalah kolom yang tersedia untuk di agregasi
          =====================================================================
          """)
    
    for i, kolom in enumerate(df_numerik, 1):
          print(f"{i}. {kolom}")
     
    pilihan = []
    
    while True:
            try:     
                input_num = input('Masukkan angka kolom yang ingin diagregasi (tulis "stop" untuk berhenti): ')
                if input_num.lower() == 'stop':
                    break
                elif int(input_num) >=1 and int(input_num) <= len(df_numerik.columns):
                    pilihan.append(int(input_num))
                else:
                    raise ValueError
            except ValueError:
                print("Masukkan angka sesuai nomor kolom")
          
    kolom_terpilih = [numerik_kolom[i-1] for i in pilihan]
    
    agregat = {
          f"Rata-rata_{kol}": (kol, "mean")
          for kol in kolom_terpilih
    }
    
    hasil = df.groupby(df_kategori.columns[input_kategori-1], as_index=False).agg(**agregat)
    print("Berikut adalah hasil dari hasil kategori")
    print(hasil)