# 🛡️ Secure Healthcare Data Pipeline (LGPD & HIPAA Compliant)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![GCP](https://img.shields.io/badge/Google_Cloud-BigQuery-yellow)
![Security](https://img.shields.io/badge/Security-HIPAA%20%2F%20LGPD-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Uma arquitetura de Engenharia de Dados focada em Privacidade.** > Este projeto simula um ambiente hospitalar real para demonstrar como ingerir, tratar e visualizar dados sensíveis de saúde sem violar leis de proteção de dados (LGPD e HIPAA).

---

## 📋 Sobre o Projeto

O maior desafio da análise de dados de saúde hoje é o **Paradoxo da Privacidade**: precisamos de dados detalhados para obter insights clínicos e operacionais, mas não podemos expor a identidade dos pacientes.

Este projeto resolve esse problema criando um pipeline *end-to-end* que:
1.  **Ingere** dados brutos (simulando um banco de dados hospitalar interno).
2.  **Anonimiza** identificadores diretos usando criptografia e mascaramento.
3.  **Carrega** os dados seguros para a nuvem (**Google BigQuery**).
4.  **Visualiza** KPIs de negócio no **Looker Studio**.

### 🎯 Objetivo Principal
Demonstrar a implementação técnica de conceitos de **Engenharia de Privacidade** (*Privacy Engineering*) e **Governança de Dados** na nuvem.

---

## 🏗️ Arquitetura da Solução

![Diagrama da Arquitetura] (arquitetura.png)

O fluxo de dados segue os princípios de **Privacy by Design**: o dado sensível é tratado em memória e jamais é persistido no Data Warehouse em sua forma original.

---

## 🔒 Estratégia de Segurança & Compliance

O diferencial deste projeto é a aplicação técnica de legislações globais de proteção de dados.

| Legislação | Técnica Aplicada | Detalhe Técnico |
| :--- | :--- | :--- |
| **HIPAA (EUA)** | *Safe Harbor (De-identification)* | Remoção de 18 identificadores diretos. Mascaramento de Nomes (`Mar***`) e Generalização de Idades e Locais. |
| **LGPD (Brasil)** | *Pseudonimização (Art. 13)* | Uso de **Hashing com Salt** (SHA256 + Chave Secreta) para transformar o CPF/SSN em um identificador opaco, mantendo a integridade referencial. |
| **Cybersecurity** | *Defesa contra Rainbow Tables* | O uso de um "Sal" (Salt) aleatório impede que hackers revertam os hashes usando tabelas pré-computadas. |

### Exemplo de Código (Pseudonimização)
```python
def aplicar_hash_seguro(dado_sensivel):
    # O SALT impede ataques de força bruta e Rainbow Tables
    dado_com_sal = dado_sensivel + OS.ENV["PROJECT_SALT_KEY"]
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

Qual a taxa de reincidência de pacientes? (Via Hash ID consistente)

Qual o faturamento médio por Operadora de Seguro?

Quais as condições médicas mais comuns por faixa etária?

🚀 Como Executar Localmente
Pré-requisitos
Python 3.x

Conta no Google Cloud Platform (com API do BigQuery habilitada)

Arquivo de credenciais JSON (Service Account)

Instalação
Clone o repositório

Bash

git clone [https://github.com/jpedropin/data-encryption.git)
cd secure-healthcare-pipeline
Instale as dependências

Bash

pip install pandas pandas-gbq faker python-dotenv google-cloud-bigquery
Configure as Variáveis de Ambiente Crie um arquivo .env na raiz e adicione:

Snippet de código

GOOGLE_APPLICATION_CREDENTIALS="caminho/para/sua-chave-gcp.json"
PROJECT_SALT_KEY="SuaChaveSecreta"
GCP_PROJECT_ID="seu-id-do-projeto-gcp"
Execute o Pipeline

Bash

python src/main.py

📄 Artigo Detalhado
Escrevi um artigo completo no Medium explicando a lógica por trás da decisão de usar Hashing com Sal e como configurei o IAM no GCP. 👉 https://medium.com/@joaopedrog.pin/como-constru%C3%AD-um-pipeline-de-dados-de-sa%C3%BAde-%C3%A0-prova-de-lgpd-e-hipaa-usando-python-e-google-cloud-789a93c66ee6?postPublishedType=initial