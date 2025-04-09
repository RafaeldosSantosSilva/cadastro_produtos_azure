# 🚀 Product Management Platform

Uma solução web moderna para cadastro e gerenciamento de produtos, com upload de imagens para o Azure Blob Storage e persistência de dados em banco MySQL. Desenvolvido com **Streamlit**, essa aplicação fornece uma interface intuitiva e eficiente para inserir, armazenar e visualizar produtos com facilidade.

---

## 📌 Visão Geral

Este projeto foi desenvolvido com o objetivo de integrar tecnologias modernas da nuvem e bancos de dados relacionais em uma interface simples de utilizar. A plataforma permite:

- Cadastro completo de produtos com nome, preço, descrição e imagem.
- Armazenamento seguro de imagens em **Azure Blob Storage**.
- Persistência de dados em **MySQL**.
- Interface amigável para visualização dos produtos cadastrados.

---

## 🧰 Tecnologias Utilizadas

| Tecnologia            | Descrição                                    |
|-----------------------|----------------------------------------------|
| [Python 3.8+](https://www.python.org/) | Linguagem principal do projeto            |
| [Streamlit](https://streamlit.io/)     | Framework para criação de aplicações web  |
| [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) | Armazenamento de arquivos em nuvem       |
| [PyMySQL](https://pypi.org/project/PyMySQL/) | Conexão com banco de dados MySQL         |
| [dotenv](https://pypi.org/project/python-dotenv/) | Gerenciamento de variáveis sensíveis     |

---

## 📁 Estrutura do Projeto

├── main.py # Código principal da aplicação Streamlit ├── .env # Arquivo de variáveis de ambiente (não comitar) ├── requirements.txt # Dependências Python ├── README.md # Documentação do projeto


---

## ⚙️ Configuração do Ambiente

## Crie e configure o arquivo .env com suas credenciais:

    BLOB_CONNECTION_STRING=your_azure_blob_connection_string
    BLOB_CONTAINER_NAME=your_container_name
    BLOB_ACCOUNT_NAME=your_account_name

    SQL_SERVER=your_mysql_host
    SQL_DATABASE=your_database_name
    SQL_NAME=your_username
    SQL_PASSWORD=your_password
## Instale as dependências:


    pip install -r requirements.txt
    Execute a aplicação:

    bash
    Copiar
    Editar
    streamlit run app.py
📦 Funcionalidades
    ✅ Formulário para cadastro de produtos

    ☁️ Upload automático da imagem no Azure Blob Storage

    🗃️ Gravação dos dados no banco MySQL

    🔍 Visualização completa dos produtos cadastrados (com imagem)

    💡 Interface simplificada, rápida e responsiva com Streamlit


