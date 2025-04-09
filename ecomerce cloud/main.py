import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymysql
import uuid
import json
from dotenv import load_dotenv

load_dotenv()
blobConnectionString = os.getenv('BLOB_CONNECTION_STRING')
blobConteinerName = os.getenv('BLOB_CONTAINER_NAME')
blobAccountName = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')
SQL_NAME = os.getenv('SQL_NAME')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')


st.title('Cadastro de produto')

#Formulario de cadastro do produto
product_name = st.text_input('Nome do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format='%.2f')
product_descripiton = st.text_area('Descrição do produto')
product_image = st.file_uploader('Imagem do Produto', type=['jpg','png','jpeg'])


#Save image on blob storage
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobConteinerName)
    blob_name = str(uuid.uuid4()) + '.' + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f'https://{blobAccountName}.blob.core.windows.net/{blobConteinerName}/{blob_name}'
    return image_url

#Save product on database
def insert_product(product_name,product_price,product_descripiton,product_image):
   try:
            image_url = upload_blob(product_image) 
            conn = pymysql.connect(host=SQL_SERVER, user=SQL_NAME, password=SQL_PASSWORD, db=SQL_DATABASE)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO Produtos (nome, preco, descricao, imagem_url) VALUES ('{product_name}', '{product_price}','{product_descripiton}','{product_image}')")
            conn.commit()
            conn.close()
            return True
   except Exception as e:
        st.error(f'Erro ao inserir produto')
        return False
   
#List products
def list_products():
    try:
        conn = pymysql.connect(host=SQL_SERVER, user=SQL_NAME, password=SQL_PASSWORD, db=SQL_DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f'Erro ao listar produtos: {e}')
        return []
    
def list_products_screen():
     products = list_products()
     for product in products:
          st.write(f'Nome: {product[1]}')
          st.write(f'Preço: {product[2]}')
          st.write(f'Descrição: {product[3]}')
          st.image( {product[4]}, width=400)


if st.button('Salvar Produto'):
    insert_product(product_name,product_price,product_descripiton,product_image)
    return_message = "Produto Salvo"


st.header("Produtos Cadastrados")

if st.button('Listar Produtos'):
    return_message = ('Produtos listados')
