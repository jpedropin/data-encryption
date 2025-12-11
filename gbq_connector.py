# gbq_connector.py
from google.oauth2 import service_account
from pandas_gbq import to_gbq
import os
import config

def bigquery(df_saude):
    print(f"--- Conectando ao BigQuery: {config.FULL_TABLE_ID} ---")
    
    if not os.path.exists(config.KEY_PATH):
        raise FileNotFoundError(f"ERRO: Chave não encontrada em: {config.KEY_PATH}")

    try:
        credenciais = service_account.Credentials.from_service_account_file(config.KEY_PATH)
        
        to_gbq(
            df_saude,
            destination_table=config.FULL_TABLE_ID,
            project_id=config.PROJECT_ID,
            credentials=credenciais,
            location=config.REGION,
            if_exists='replace',
            progress_bar=True
        )
        print("✅ Upload realizado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no processo: {e}")