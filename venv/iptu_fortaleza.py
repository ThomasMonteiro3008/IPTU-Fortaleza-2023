import pandas as pd

df_iptu_fortaleza  = pd.read_csv('br_ce_fortaleza_sefin_iptu_face_quadra.csv', encoding='latin1')
print(df_iptu_fortaleza.columns)

#print(df_iptu_fortaleza.head())