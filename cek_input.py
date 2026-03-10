import pandas as pd

def cek_input_angka(pesan, jenis):
        if jenis == 'integer':
            while True:
                try:
                    return int(input(pesan))
                except ValueError:
                    print("Data ini harus berupa angka")
        elif jenis == 'float':
            while True:
                try:
                    return float(input(pesan))
                except ValueError:
                    print("Data ini harus berupa angka")

def cek_nama(tabel):
    while True:
        input_nama = input("Masukkan nama kepala keluarga: ").strip().title()
        if input_nama.lower() in tabel['head_name'].str.strip().str.lower().values:
            return input_nama
        else:
            print("Nama tidak ditemukan, masukkan nama yang sesuai")

def cek_input_kolom(tabel):
    while True:
        try:
            input_kolom = int(input("Masukan nomor kolom yang tersedia: "))
            if input_kolom <= len(tabel.columns):
                return input_kolom
            else:
                print("Masukkan nomor kolom sesuai dengan yang tersedia")
        except ValueError:
            print("input harus berupa angka")

def cek_keyword_nama(tabel):
    while True:
        keywords = input("Masukkan keyword nama (dapat berupa huruf pertama atau sebagian nama): ").strip()
        if tabel['head_name'].str.contains(keywords, case=False, na=False).any():
            list_nama = tabel[tabel['head_name'].str.strip().str.contains(keywords, case=False, na=False)]
            return list_nama['head_name']
        else:
            print("Nama tidak ditemukan")
            
def cek_jenis_kolom(tabel, masuk, pesan):
        if tabel[tabel.columns[masuk-1]].dtype == int:
            perubahan = cek_input_angka(pesan, 'integer')
        elif tabel[tabel.columns[masuk-1]].dtype == float:
            perubahan = cek_input_angka(pesan, 'float')
        else:
            perubahan = input(pesan)
        return perubahan