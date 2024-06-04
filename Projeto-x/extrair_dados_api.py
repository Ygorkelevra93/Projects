## ETAPA 1 DE 2 AIR FLOW
## DAG CRIADA PARA FAZER A LEITURA DOS DADOS NA API
## TRANSFORMAR EM PARQUET 
## E JOGAR NUM BANCO POSTGRES
## PROJETO_X - LEVAR DADOS DE UMA API - AIR FLOW - POSTGRES
## 
## AUTOR: YGOR LEÃO 31/05/2024

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import requests
import pyarrow as pa
import pyarrow.parquet as pq
from sqlalchemy import create_engine

DATABASE_USERNAME = 'admin'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'postgresql-174110-0.cloudclusters.net'
DATABASE_PORT = '10025'
DATABASE_NAME = 'teste-airflow-db'
DATABASE_URL = f'postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def create_table_and_populate(url):
    table_name = url.split('=')[-1]

    # Fetch data from API
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data[table_name])
    
    # Explode the 'products' column if the table name is 'orders'
    if table_name == 'orders':
        df = df.explode('products')

    # GERAR TABELA PARA ITERAÇÃO SOBRE OS CAMPOS DA TABELA BAIXADA
    schema = pa.Schema.from_pandas(df)
    
    # CRIAÇÃO DA QUERY DE CRIAÇÃO DE TABELAS
    sql_statement = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
    for i, field in enumerate(schema.names):
        field_type = "VARCHAR"
        sql_statement += f"    {field} {field_type},\n" if i < len(schema.names) - 1 else f"    {field} {field_type}\n"
    sql_statement += ")"

    # EXECUÇÃO QUERY DE CRIAÇÃO DA TABELA E SEUS TIPOS DE COLUNAS
    sql_statement = f"""{sql_statement}"""

    # ABERTURA DA ENGINE DE CONEXÃO COM POSTGRES 
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        # CRIAÇÃO DA TABELA NO POSTGRES
        connection.execute(sql_statement)
        # INSERÇÃO DE DADOS NA TABELA CRIADA
        headers = df.columns.tolist()
        insert_sql = f"""
            INSERT INTO {table_name} ({', '.join(headers)})
            VALUES ({', '.join(['%s'] * len(headers))})
        """
        for _, row in df.iterrows():
            connection.execute(insert_sql, list(row))

# Código para definir a DAG e as tasks
with DAG(
    'abc_teste3',
    default_args=default_args,
    description='A DAG to fetch JSON data from API, convert to Parquet, and save to PostgreSQL',
    schedule_interval='@daily',
    start_date=datetime(2024, 5, 30),
    catchup=False
) as dag:
    urls = [
        "https://6p5nb1ghed.execute-api.us-east-1.amazonaws.com/default/origemapp?api=orders",
        "https://6p5nb1ghed.execute-api.us-east-1.amazonaws.com/default/origemapp?api=leads",
        "https://6p5nb1ghed.execute-api.us-east-1.amazonaws.com/default/origemapp?api=customers",
        "https://6p5nb1ghed.execute-api.us-east-1.amazonaws.com/default/origemapp?api=products"
    ]

    for url in urls:
        table_name = url.split('=')[-1]

        fetch_task = PythonOperator(
            task_id=f'fetch_and_save_{table_name}',
            python_callable=create_table_and_populate,
            op_args=[url],
        )

        fetch_task
