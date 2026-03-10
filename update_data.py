import mysql.connector
import pandas as pd
from prosses import ambil_data
from cek_input import cek_input_angka, cek_keyword_nama, cek_nama, cek_input_kolom, cek_jenis_kolom

#Update data
def update_data(pengarah):
    def update(tabel, nama_kolom):
        if tabel == 'households':
            query_up = f"""
            UPDATE
                households
            SET 
                {nama_kolom} = %s
            WHERE
                id = %s;"""
        else:
            query_up = f"""
            UPDATE
                financial_records
            SET 
                {nama_kolom} = %s
            WHERE
                id = %s;"""
        return query_up
                
    mycursor = pengarah.cursor()
    df1 = ambil_data(1, pengarah)
    df2 = ambil_data(2, pengarah)
    df3 = ambil_data(3, pengarah)
    
    print("\n===================================")
    print("Data tersedia untuk diubah")
    print("====================================")
    
    for i, kolom in enumerate(df3, 1):
        print(f"{i}. {kolom}")
    
    print("Ingin mengubah data pada kolom apa?")
    input_kolom = cek_input_kolom(df3)
    nama_kolom = df3.columns[input_kolom-1]
    
    print("Ubah kolom sesuai nama")
    list_nama = cek_keyword_nama(df1)
    print("\n===================================")
    print("Berikut nama tersedia")
    print("====================================")
    for i, kolom in enumerate(list_nama, 1):
        print(f"{i}. {kolom}")
    nama = cek_nama(df1)
    
    query = f"""
        SELECT
            id
        FROM
            households
        WHERE
            head_name = '{nama}';"""
    id = int((pd.read_sql(query, pengarah)).squeeze())
    pesan = (f"Masukan yang diubah dari kolom {nama_kolom}: ")
    if nama_kolom in df1.columns:
        perubahan = cek_jenis_kolom(df1, input_kolom, pesan)
        query_up = update('households', nama_kolom)
    else:
        perubahan = cek_jenis_kolom(df2, (input_kolom-7), pesan)
        query_up = update('financial_records', nama_kolom) 
    
    mycursor.execute(query_up, (perubahan, id))
    pengarah.commit()
    mycursor.close()
    print(f"perubahan kolom {nama_kolom} pada data dengan nama {nama} berhasil diubah")        


#Memasukkan data baru        
def tambah_data(pengarah):
    mycursor = pengarah.cursor()
    while True: 
        try:
                #input tabel 1
                nama = (input("Masukkan nama kepala keluarga: ")).title()
                umur = cek_input_angka("Masukan umur kepala keluarga: ", 'integer')
                pendidikan = input("Masukkan pendidikan terakhir kepala keluarga: ")
                pernikahan = input("Masukkan status pernikahan: ")
                anak = cek_input_angka("Masukkan jumlah anak: ", 'integer')
                luas = cek_input_angka("Masukkan luar rumah dalam m2: ", 'integer')
                pengeluaran = cek_input_angka("Masukkan estimasi pengeluaran bulanan: ", 'integer')
                
                #input tabel 2
                pekerjaan = input("Masukkan pekerjaan kepala keluarga: ")
                pendapatan = cek_input_angka("Masukkan pendapatan bulanan: ", 'float')
                keluar = cek_input_angka("Masukkan pengeluaran bulanan aktual: ", 'float')
                simpanan = cek_input_angka("Masukkan uang dalam tabungan: ", 'float')
                hutang = cek_input_angka("Masukkan jumlah hutang: ", 'float')
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
    
    input_nama = cek_nama(df)
    query = f"""
    DELETE FROM 
        households
    WHERE
        head_name = %s;"""
    mycursor.execute(query, (input_nama,))
    pengarah.commit()
    print(f"{input_nama} berhasil dihapus dari database")
    mycursor.close()