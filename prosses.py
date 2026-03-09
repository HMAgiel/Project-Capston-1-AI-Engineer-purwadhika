import pandas as pd

#Mengambil data
def ambil_data(input_user, pengarah):
    if input_user == 1:
        query = '''
            SELECT 
                head_name, head_age, education_level, marital_status, num_children, house_size_m2, monthly_expense_estimate
            FROM 
                households;'''
        df = pd.read_sql(query, pengarah)
        return df
    elif input_user == 2:
        query = '''
            SELECT
                main_job, monthly_income, monthly_expense, savings, debt
            FROM 
                financial_records;'''
        df = pd.read_sql(query, pengarah)
        return df
    elif input_user == 3:
        query = '''
            SELECT
                h.head_name, h.head_age, h.education_level, h.marital_status, h.num_children, h.house_size_m2, h.monthly_expense_estimate,
                f.main_job, f.monthly_income, f.monthly_expense, f.savings, f.debt
            FROM
                households as h
            LEFT JOIN
                financial_records as f 
                ON h.id = f.household_id;'''
        df = pd.read_sql(query, pengarah)
        return df

def ambil_numerik(df):
        df_numerik = df.apply(pd.to_numeric, errors='coerce').dropna(axis=1)
        print("\nKolom numerik yang tersedia:")
        for i, kolom in enumerate(list(df.apply(pd.to_numeric, errors='coerce').dropna(axis=1).columns), 1):
            print(f"{i}. {kolom}")
        return df_numerik