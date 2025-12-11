import kagglehub
import pandas as pd
import os

import config 
from gbq_connector import bigquery #Importando de config.py

# Configura visualização no VSCode
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 1000)

# Baixa o dataset de Saúde
path = kagglehub.dataset_download("prasad22/healthcare-dataset")
import os
csv_path = os.path.join(path, "healthcare_dataset.csv")
df_saude = pd.read_csv(csv_path)

#Regras de Anonimização

#1 - NOME
df_saude['Name'] = df_saude['Name'].str.title()
df_saude['Name'] = df_saude['Name'].str[:3] + '***'

#2 - NÚMERO DO QUARTO
df_saude['Room Number'] = df_saude['Room Number'].astype(str).str[0] + '**'

#3 - IDADE - FAIXA ETÁRIA AO INVÉS DE IDADE ESPECIFICA.
df_saude['Age Range'] = df_saude['Age'].apply(lambda x: f"{int(x)//10*10}-{int(x)//10*10 + 9}")

#4 - DINHEIRO - ARREDONDANDO VALORES GRANDES 
df_saude['Billing Amount'] = df_saude['Billing Amount'].round(0).astype(int)

#Removendo a coluna "AGE" e ajeitando a ordem
df_saude = df_saude.drop(columns=['Age'])
nova_ordem = [
    'Name', 
    'Age Range',      
    'Gender', 
    'Blood Type', 
    'Medical Condition', 
    'Date of Admission', 
    'Doctor', 
    'Hospital', 
    'Insurance Provider', 
    'Billing Amount', 
    'Room Number', 
    'Admission Type', 
    'Discharge Date', 
    'Medication', 
    'Test Results'
]
df_saude = df_saude[nova_ordem]

# print("--- DADOS ORIGINAIS (COM RISCO DE PRIVACIDADE) ---")
# print(df_saude.head())
# print("\n--- Informações das Colunas ---")
# print(df_saude.info())

print("\n--- REGRAS DE ANONIMIZAÇÃO APLICADAS ---")
print("✅ Coluna 'Name': Mascarada (3 primeiros caracteres + ***)")
print("✅ Coluna 'Room Number': Generalizada (1º dígito + **)")
print("✅ Coluna 'Age': Substituída por 'Age Range'")
print("✅ Valores financeiros arredondados")
print(f"ℹ️  Total de registros processados: {len(df_saude)}")

print(" Enviando para o BigQuery...")
bigquery(df_saude)
