import mysql.connector
import pandas as pd
from prosses import ambil_data, cek_keyword_nama

#Memasukkan data baru        
def tambah_data(pengarah):
    def input_angka(pesan, jenis):
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
                    
    mycursor = pengarah.cursor()
    while True: 
        try:
                #input tabel 1
                nama = (input("Masukkan nama kepala keluarga: ")).title()
                umur = input_angka("Masukan umur kepala keluarga: ", 'integer')
                pendidikan = input("Masukkan pendidikan terakhir kepala keluarga: ")
                pernikahan = input("Masukkan status pernikahan: ")
                anak = input_angka("Masukkan jumlah anak: ", 'integer')
                luas = input_angka("Masukkan luar rumah dalam m2: ", 'integer')
                pengeluaran = input_angka("Masukkan estimasi pengeluaran bulanan: ", 'integer')
                
                #input tabel 2
                pekerjaan = input("Masukkan pekerjaan kepala keluarga: ")
                pendapatan = input_angka("Masukkan pendapatan bulanan: ", 'float')
                keluar = input_angka("Masukkan pengeluaran bulanan aktual: ", 'float')
                simpanan = input_angka("Masukkan uang dalam tabungan: ", 'float')
                hutang = input_angka("Masukkan jumlah hutang: ", 'float')
                break
        except ValueError:
            print("Masukan data yang sesuai")
            continue
    
    query_input_tabel1 = """
    INSERT INTO households (head_name, head_age, education_level, marital_status, num_children, house_size_m2, monthly_expense_estimate)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    input_tabel1 = (nama, umur, pendidikan, pernikahan, anak, luas, pengeluaran)
    mycursor.execute(query_input_tabel1, input_tabel1)
    househodl_id = mycursor.lastrowid
    
    query_input_tabel2 = """
    INSERT INTO financial_records (household_id, main_job, monthly_income, monthly_expense, savings, debt)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    input_tabel2 = (househodl_id, pekerjaan, pendapatan, keluar, simpanan, hutang)
    mycursor.execute(query_input_tabel2, input_tabel2)
    pengarah.commit()
    mycursor.close()
    
    
#Menghapus data
def hapus_data(pengarah):
    df = ambil_data(1, pengarah)
    mycursor = pengarah.cursor()
    
    list_nama = cek_keyword_nama(df)
    print("""\n 
          ==========================================
          Berikut adalah nama-nama yang tersedia
          ==========================================""")
    for i, kolom in enumerate(list_nama, 1):
        print(f"{i}. {kolom}")
    
    while True:
        input_nama = input("Masukkan nama kepala keluarga: ").strip().title()
        if input_nama in df['head_name'].str.strip().values:
            query = f"""
            DELETE FROM 
                households
            WHERE
                head_name = %s;"""
            mycursor.execute(query, (input_nama,))
            pengarah.commit()
            print(f"{input_nama} berhasil dihapus dari database")
            break
        else:
            print("Nama tidak ditemukan, masukkan nama yang sesuai")
    mycursor.close()