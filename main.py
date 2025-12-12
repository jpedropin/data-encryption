import kagglehub
import pandas as pd
import os
import hashlib
from faker import Faker 

import config 
from gbq_connector import bigquery #Importando de config.py aqui pra main

# Configuração do faker - para criar um ID falso para cada paciente (Afim de adicionar mais complexidade no projeto)
fake = Faker('en_US')
SALT = "Hospit@l_Segur0!"

# Baixando o dataset de Saúde
path = kagglehub.dataset_download("prasad22/healthcare-dataset")
import os
csv_path = os.path.join(path, "healthcare_dataset.csv")
df_saude = pd.read_csv(csv_path)

df_saude['SSN_Real'] = [fake.ssn() for _ in range(len(df_saude))]

# Aplicando o Hash
def aplicar_hash(valor_real):
    valor_com_sal = str(valor_real) + SALT
    return hashlib.sha256(valor_com_sal.encode()).hexdigest()

# Cria a coluna blindada (Hash)
df_saude['Patient_ID_Hashed'] = df_saude['SSN_Real'].apply(aplicar_hash)

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

#Removendo a coluna "AGE" e ajeitando a ordem de exibição
df_saude = df_saude.drop(columns=['Age'])
nova_ordem = [
    'Patient_ID_Hashed',
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
df_saude.columns = df_saude.columns.str.replace(' ', '_') #Pra nao dar problema no looker

print("\n--- REGRAS DE ANONIMIZAÇÃO APLICADAS ---")
print("✅ Coluna 'Name': Mascarada (3 primeiros caracteres + ***)")
print("✅ Coluna 'Room Number': Generalizada (1º dígito + **)")
print("✅ Coluna 'Age': Substituída por 'Age Range'")
print("✅ Valores financeiros arredondados")
print(f"ℹ️  Total de registros processados: {len(df_saude)}")

print(" Enviando para o BigQuery...")
bigquery(df_saude)
