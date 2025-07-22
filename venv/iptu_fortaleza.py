import pandas as pd

df_iptu_fortaleza  = pd.read_csv('br_ce_fortaleza_sefin_iptu_face_quadra.csv', encoding='latin1')
#print(df_iptu_fortaleza.columns)

#Criando uma coluna categórica para definir o tipo de logradouro.
def tipo_logradouro(logradouro):
    logradouro = str(logradouro)
    if logradouro.startswith('RUA'):
        return "RUA"
    elif logradouro.startswith('ALAMEDA'):
        return "ALAMEDA"
    elif logradouro.startswith("TRAVESSA"):
        return "TRAVESSA"
    elif logradouro.startswith('VILA'):
        return "VILA"
    else:
        return None
    
df_iptu_fortaleza['tipo_de_logradouro'] = df_iptu_fortaleza['logradouro'].apply(tipo_logradouro)

#print(df_iptu_fortaleza.columns)
#Alterar os valores das colunas de True e False para Sim e Não
colunas_alterar = df_iptu_fortaleza[['indicador_agua', 'indicador_esgoto', 'indicador_galeria_pluvial', 'indicador_sarjeta', 
                   'indicador_iluminacao_publica', 'indicador_arborizacao']]
for coluna in colunas_alterar:
    df_iptu_fortaleza[coluna] = df_iptu_fortaleza[coluna].replace({'True': True, 'False': False})
    df_iptu_fortaleza[coluna] = df_iptu_fortaleza[coluna].replace({True: 'Sim', False: 'Não'})

print(df_iptu_fortaleza['indicador_agua'].unique())