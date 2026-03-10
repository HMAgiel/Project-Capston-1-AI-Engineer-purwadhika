import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prosses import ambil_data, ambil_numerik

#Plot grafik    
def buat_grafik(pengarah):
      def input_dan_cek(df, jenis):
            if jenis == 'numerik':
                  df_pilih = ambil_numerik(df)
            elif jenis == 'semua':
                  df_pilih = df.drop(columns=['head_name'])
                  for i, kolom in enumerate(df_pilih, 1):
                        print(f"{i}. {kolom}")
            while True:
                  try:
                      input_kolom = int(input("Masukkan nomor kolom yang ingin di plot: "))
                      if input_kolom >=1 and input_kolom <= len(df_pilih.columns):
                            break
                      else:
                            raise ValueError
                  except:
                        print("Masukan nomor sesuai nomor kolom yang tersedia")
            return df_pilih, input_kolom
      
      df = ambil_data(3,pengarah)
      print("""
            =====================================================================
            Berikut adalah Jenis plot yang tersedia untuk di plot
            =====================================================================
            1. Histogram
            2. Boxplot
            3. Barplot
            """)
      
      while True:
            try:
                  input_user = int(input("Mau plot apa (masukkan angka sesuai nomor plot)?: "))
                  if input_user == 1:
                        df_tanpa_nama, input_kolom = input_dan_cek(df, 'semua')
                        kolom = df_tanpa_nama.columns[input_kolom-1]
                        plt.figure(figsize=(10,10))
                        sns.set_style("whitegrid")
                        sns.displot(df_tanpa_nama, x=kolom, kde=True)
                        plt.title(f"plot histogram data {kolom}")
                        plt.xticks(rotation=45)
                        plt.show()
                        break
                  
                  elif input_user == 2:
                        df_tanpa_nama, input_kolom = input_dan_cek(df, 'semua')
                        kolom = df_tanpa_nama.columns[input_kolom-1]
                        plt.figure(figsize=(10,10))
                        sns.set_style("whitegrid")
                        sns.boxplot(x=df_tanpa_nama[kolom])
                        plt.title(f"plot histogram data {kolom}")
                        plt.xticks(rotation=45)
                        plt.show()
                        break
                  
                  elif input_user == 3:
                        df_kat = df.select_dtypes(include=['category', 'object'])
                        print("""
                        ====================================================================
                        Berikut adalah kolom kategori yang tersedia
                        ====================================================================
                        """)
                        df_kategori, input_kolom_kategori = input_dan_cek(df_kat, 'semua')
                        df_numerik, input_numerik = input_dan_cek(df, 'numerik')
                        x=df_kategori.columns[input_kolom_kategori-1]
                        y=df_numerik.columns[input_numerik-1]
                        plt.figure(figsize=(10,10)) 
                        sns.set_style('whitegrid')
                        sns.barplot(data=df, x=y, y=x, palette="viridis")
                        plt.title(f"Plot bar rata-rata {x} terhadap {y}")
                        plt.show()
                        break
                  else:
                        raise ValueError
            except ValueError:
                  print("Pilih angka sesuai pilihan plot yang tersedia")