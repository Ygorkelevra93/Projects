## ETAPA 2 DE 2 AIR FLOW
## DAG CRIADA PARA FAZER A LEITURA DOS DADOS QUE ESTAO CHEGANDO NA LANDING ZONE
## E LEVANDO PARA UMA SEGUNDA CAMADA ONDE FAZEMOS SOMENTE A INSERÇÃO DO QUE É DADO NOVO
## 
## PROJETO_X - LEVAR DADOS DE UMA API - AIR FLOW - POSTGRES
## 
## AUTOR: YGOR LEÃO 31/05/2024
##

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sqlalchemy as sql
import pandas as pd
import psycopg2
import logging

DATABASE_USERNAME = 'admin'
DATABASE_PASSWORD = '%password'
DATABASE_HOST = 'postgresql-174110-0.cloudclusters.net'
DATABASE_PORT = '10025'
DATABASE_NAME = 'teste-airflow-db'
DATABASE_URL = f'postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
db_url = 'postgresql+psycopg2://admin:%password@postgresql-174110-0.cloudclusters.net:10025/teste-airflow-db'

tables = ['products', 'orders', 'leads', 'customers']
conn_id = 'postgres-airflow'

def transform_and_load_table(table_name):
    # Connect to the database
    engine = sql.create_engine('postgresql+psycopg2://admin:%password@postgresql-174110-0.cloudclusters.net:10025/teste-airflow-db')
    connection = engine.connect()
    print('engine criada banco postgres')
    # Connect to the database and create a cursor    
        
    # Read data from the original table  # atenção para que a abertura da engine de conexão nao se feche, durante as funçoes que precisem dela, atenção para IDENTAR corretamente
    result_proxy = connection.execute(sql_query)
    sql_query = f""" SELECT * FROM public.{table_name}"""
    with engine.connect() as connection:                                       
        df = pd.DataFrame(result_proxy.fetchall(), columns=result_proxy.keys()) # https://stackoverflow.com/questions/12047193/how-to-convert-sql-query-result-to-pandas-data-structure
        print('leu a tabela no postgres')
    
    
        
        # ADICIONAR PREFIXO T_ AO NOME DA TABELA - INDICANDO QUE É A CAMADA DE TRATAMENTO 
        transformed_table_name = 't_' + table_name
        print('adicionou prefixo')
        
        # Gerar instrução SQL para criação da nova tabela
        schema = df.columns
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {transformed_table_name} (\n"
        for i, field in enumerate(schema):
            if i < len(schema) - 1:
                create_table_sql += f"    {field} VARCHAR,\n"
            else:
                create_table_sql += f"    {field} VARCHAR\n"
                create_table_sql += ")"
    
            print('Criou query para criar tabela:')
            print(create_table_sql) 
            
        # INSERIR A NOVA TABELA T_ NO POSTGRES
        connection.execute(create_table_sql)
        print('criou tabela')
        
        
        ######################################################################################
        ## ESPAÇO PARA COLOCAR O IF DE TRAVAR O QUE FOR INFORMAÇÃO NOVA APENAS              ##
        ## MINHA IDEIA É CHAMAR O QUE TEM NO BANCO PRINCIPAL DO INÍCIO ATÉ  TODAY()-30      ##
        ## E APPENDAR O QUE VIER DA LANDINGZONE DALI ATÉ A DATA MAIS RECENTE                ##
        ##                                                                                  ##
        ######################################################################################
        
        # INSERIR DADOS A ESTA TABELA T
        headers = df.columns.tolist()
        insert_sql = f"""
            INSERT INTO {transformed_table_name} ({', '.join(headers)})
            VALUES ({', '.join(['%s'] * len(headers))})
            """
        for _, row in df.iterrows():
            connection.execute(insert_sql, list(row))
    
        # Log the completion of transformation
        print(f'Transformation completed for table {transformed_table_name}. New table: t_{table_name}')

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'aaa_t_dados',
    default_args=default_args,
    description='DAG to move data from landing zone to processing layer',
    schedule_interval='@daily',
    start_date=datetime(2024, 5, 31)
)

# Create tasks for each table transformation
for table_name in tables:
    task_id = f'transform_and_load_table_{table_name}'
    task = PythonOperator(
        task_id=task_id,
        python_callable=transform_and_load_table,
        op_kwargs={'table_name': table_name},
        dag=dag
    )
# Adicionando o nome da tarefa
globals()[task_id] = task