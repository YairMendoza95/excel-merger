import pandas as pd


def fill_empty_fields(df):
    for index, row in df.iterrows():
        if pd.isna(row["FECHA"]):
            if index > 0:
                previous_row = df.iloc[index - 1]
                for col in df.columns:
                    if pd.isna(row[col]):
                        df.at[index, col] = previous_row[col]
    return df


def columns_renamer(df):
    columns_mapping = {
        'FECHA': 'fecha',
        'FOLIO': 'folio',
        'JAULAS': 'jaulas',
        'CLIENTE': 'cliente',
        'CHOFER': 'chofer',
        "P. POLLOS": 'pollos_programados',
        'P. PROMEDIO': 'promedio_programado',
        'POLLOS': 'pollos',
        'SEXO': 'sexo',
        'P. BRUTO': 'peso_bruto',
        'P. TARA': 'peso_tara',
        'P. NETO': 'peso_neto',
        'PROMEDIO': 'promedio',
        'DIFERENCIA PESOS P.': 'diferencia_pesos',
        'C1': 'caseta_1',
        'C2': 'caseta_2',
        'C3': 'caseta_3',
        'C4': 'caseta_4',
        'C5': 'caseta_5',
        'C6': 'caseta_6',
        'C7': 'caseta_7',
        'C8': 'caseta_8',
        'C9': 'caseta_9',
        'C10': 'caseta_10',
        'C11': 'caseta_11',
        'C12': 'caseta_12',
        'C19': 'caseta_19',
        'C20': 'caseta_20',
        'C21': 'caseta_21',
        'C22': 'caseta_22',
        'C23': 'caseta_23',
        'C24': 'caseta_24',
        'C25': 'caseta_25',
        'C26': 'caseta_26',
        'C27': 'caseta_27',
        'GRANJA': 'granja',
        'PLACAS': 'placas'
    }

    df = df.rename(columns=columns_mapping)

    return df