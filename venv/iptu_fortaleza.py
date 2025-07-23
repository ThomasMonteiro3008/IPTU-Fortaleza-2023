import pandas as pd
import matplotlib as plt

#Importação de dados
df_iptu_fortaleza  = pd.read_csv('br_ce_fortaleza_sefin_iptu_face_quadra.csv', encoding='latin1')
#print(df_iptu_fortaleza.columns)

# Tratamento de dados
## Criando uma coluna categórica para definir o tipo de logradouro.
def tipo_logradouro(logradouro):
    logradouro = str(logradouro)
    if logradouro.startswith('RUA') or logradouro.startswith('AVENIDA'):
        return "RUA/AVENIDA"
    elif logradouro.startswith('ALAMEDA'):
        return "ALAMEDA"
    elif logradouro.startswith("TRAVESSA") or logradouro.startswith("BECO"):
        return "BECO/TRAVESSA"
    elif logradouro.startswith('VILA'):
        return "VILA"
    elif logradouro.startswith('LARGO') or logradouro.startswith('GALERIA') or logradouro.startswith('PRA'):
        return "LARGO/GALERIA/PRACA"
    elif logradouro.startswith('VIA') or logradouro.startswith('ESTRADA'):
        return "VIA/ESTRADA"
    elif logradouro.startswith('VIADUTO'):
        return "VIADUTO"
    else:
        return None
df_iptu_fortaleza['tipo_de_logradouro'] = df_iptu_fortaleza['logradouro'].apply(tipo_logradouro)

## Alterar os valores das colunas de True e False para Sim e Não
colunas_alterar = df_iptu_fortaleza[['indicador_agua', 'indicador_esgoto', 'indicador_galeria_pluvial', 'indicador_sarjeta', 
                   'indicador_iluminacao_publica', 'indicador_arborizacao']]
for coluna in colunas_alterar:
    df_iptu_fortaleza[coluna] = df_iptu_fortaleza[coluna].replace({'True': True, 'False': False})
    df_iptu_fortaleza[coluna] = df_iptu_fortaleza[coluna].replace({True: 'Sim', False: 'Não'})

## Correção de nomes
df_iptu_fortaleza['pavimentacao'] = df_iptu_fortaleza['pavimentacao'].replace({'Pedra rust': 'Pedra Rústica', 
                                                                               'ParalelepÃ\xadpedo': 'Paralelpípedo',
                                                                               'Sem PavimentaÃ§Ã£o': 'Sem Pavimentação'})
## Valores ausentes
missing_data = pd.DataFrame({
    'Total Ausentes': df_iptu_fortaleza.isnull().sum(),
    'Porcentagem %': (df_iptu_fortaleza.isnull().sum()/len(df_iptu_fortaleza) * 100).round(1)
})
#print(missing_data)

missing_data_total = df_iptu_fortaleza.isnull().sum().sum()
total_ausentes = df_iptu_fortaleza.shape[0] * df_iptu_fortaleza.shape[1]
porcentagem_total = (missing_data_total / total_ausentes)*100
#print(porcentagem_total)

df_iptu_fortaleza = df_iptu_fortaleza.dropna()
#print(df_iptu_fortaleza)
#df_iptu_fortaleza.to_excel('iptu_fortaleza.xlsx', index=False)


## Medidas
pavimentacao_valores = df_iptu_fortaleza['pavimentacao'].value_counts()
pct_sem_pavimentacao = ((df_iptu_fortaleza[df_iptu_fortaleza['pavimentacao'] == 'Sem Pavimentação']).count()) / (df_iptu_fortaleza.count()) *100
#print(df_iptu_fortaleza)

logradouros = df_iptu_fortaleza['tipo_de_logradouro'].value_counts()
print(logradouros)

i_agua = (df_iptu_fortaleza['indicador_agua'].value_counts(normalize=True)*100).round(1) ## Existência de rede de água
i_esgoto = (df_iptu_fortaleza['indicador_esgoto'].value_counts(normalize=True)*100).round(1) ## Existência de rede de coleta de esgoto
i_pluvial = (df_iptu_fortaleza['indicador_galeria_pluvial'].value_counts(normalize=True)*100).round(1)  ## Existência de rede de drenagem pluvial
i_sarjeta = (df_iptu_fortaleza['indicador_sarjeta'].value_counts(normalize=True)*100).round(1) ## Existencia de meio-fio
i_iluminacao = (df_iptu_fortaleza['indicador_iluminacao_publica'].value_counts(normalize=True)*100).round(1) ## Exitencia de iluminção pública
i_arbo = (df_iptu_fortaleza['indicador_arborizacao'].value_counts(normalize=True)*100).round(1) ## Existencia de arborização planejada no canteiro central de vias duplas

#print(f"% de rede de Água: {i_agua}, % de rede de Esgoto: {i_esgoto}, % de rede de Pluvial: {i_pluvial}")