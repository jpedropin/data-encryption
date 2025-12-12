# 🛡️ Secure Healthcare Data Pipeline (LGPD & HIPAA Compliant)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![GCP](https://img.shields.io/badge/Google_Cloud-BigQuery-yellow)
![Security](https://img.shields.io/badge/Security-HIPAA%20%2F%20LGPD-green)

> **Uma arquitetura de Engenharia de Dados focada em Privacidade.**
> Este projeto simula um ambiente hospitalar real para demonstrar como ingerir, tratar e visualizar dados sensíveis de saúde sem violar leis de proteção de dados.

---

## 🏗️ Arquitetura da Solução

![Diagrama da Arquitetura](arquitetura.png)

O fluxo de dados segue os princípios de **Privacy by Design**: o dado sensível é tratado em memória e jamais é persistido no Data Warehouse em sua forma original.

---

## 💻 Exemplo de Código (Pseudonimização)

O diferencial técnico é o uso de **Hashing com Salt** para evitar ataques de *Rainbow Table*:

```python
import hashlib
import os

def aplicar_hash_seguro(dado_sensivel):
    # O SALT impede ataques de força bruta e Rainbow Tables
    dado_com_sal = dado_sensivel + os.getenv("PROJECT_SALT_KEY")
    return hashlib.sha256(dado_com_sal.encode()).hexdigest()
🛠️ Tech Stack
Linguagem: Python 3.10

Manipulação de Dados: Pandas, Faker (para geração de dados sintéticos PII)

Segurança: Hashlib, Dotenv

Cloud (GCP):

BigQuery: Data Warehouse Serverless.

IAM: Gestão de acesso via Service Account (Princípio do Privilégio Mínimo).

Visualização: Looker Studio.

📊 Resultados e Analytics
Mesmo após a anonimização rigorosa, a utilidade dos dados foi preservada. O Dashboard final permite responder:

✅ Qual a taxa de reincidência de pacientes? (Via Hash ID consistente)

✅ Qual o faturamento médio por Operadora de Seguro?

✅ Quais as condições médicas mais comuns por faixa etária?

🚀 Como Executar Localmente
Pré-requisitos
Python 3.x

Conta no Google Cloud Platform (com API do BigQuery habilitada)

Arquivo de credenciais JSON (Service Account)

Instalação
Clone o repositório

Bash

git clone https://github.com/jpedropin/data-encryption.git
cd data-encryption
Instale as dependências

Snippet de código

GOOGLE_APPLICATION_CREDENTIALS="caminho/para/sua-chave-gcp.json"
PROJECT_SALT_KEY="SuaChaveSecreta"
GCP_PROJECT_ID="seu-id-do-projeto-gcp"
Execute o Pipeline

📄 Artigo Detalhado
Escrevi um artigo completo no Medium explicando a lógica por trás da decisão de usar Hashing com Sal e como configurei o IAM no GCP.

👉 Leia o Artigo Completo Aqui