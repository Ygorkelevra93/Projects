import pandas as pd
import datetime
import holidays
from holidays import countries
import shutil


# Crie uma lista com todas as datas dos feriados nacionais do Brasil para o período de tempo que você está analisando
feriados = holidays.CountryHoliday('BR', years=[2021, 2022, 2023, 2024, 2025, 2026])

# Defina uma função para ajustar a data de vencimento para um dia útil seguinte
def ajustar_vencimento(data_x):
    
    set_loop = False  
    
    while not set_loop :
        no = data_x.weekday()
        fer = feriados.get(data_x)
        if fer is None:
            if no == 5:
                data_x = data_x + datetime.timedelta(days=2)
            elif no == 6:
                data_x = data_x + datetime.timedelta(days=1)
            else:
                set_loop = True        
        else:
            data_x = data_x + datetime.timedelta(days=1)
   
    return data_x
    
    
    
# Abra o arquivo CSV e leia os dados em um DataFrame
df = pd.read_csv('//erpapp/spool/yg055943/ygor123.csv',sep = ';', encoding='cp1252', low_memory=False)

# Exclua as linhas em que a coluna 'Vencto' está vazia
df = df[df['Vencto'].notnull()]

# Adicione a nova coluna "vencimento2" com datas de vencimento ajustadas
df['vencimento2'] = df['Vencto'].apply(lambda x: ajustar_vencimento(datetime.datetime.strptime(x, '%d/%m/%Y').date()).strftime('%d/%m/%Y'))

# Remova o ".0" do final dos valores na coluna "Cart"
df['Cart'] = df['Cart'].astype(str).str.replace('.0', '')

# Converta a coluna "Cart" para object
df['Cart'] = df['Cart'].astype(object)


# Escreva os dados atualizados em um novo arquivo CSV
df.to_csv('//erpapp/spool/yg055943/ygor123.csv', sep=';', encoding='cp1252' , index=False)
print ('Correção da coluna vencimento - Final de Semana - OK')

##################################################################################################
##################################################################################################



ESPDP029_origem = '//erpapp/spool/yg055943/ESPDP029.csv'
ESPDP029_destino = '//erpapp/spool/is057488/ESPDP029.csv'

ESPDP015origem = '//erpapp/spool/yg055943/ESPDP015.csv'
ESPDP015_destino = '//erpapp/spool/is057488/ESPDP015.csv'

PlanACR_origem = '//erpapp/spool/yg055943/ygor123.csv'
PlanACR_destino = '//erpapp/spool/is057488/Plan-acr.csv'


shutil.copy(ESPDP029_origem, ESPDP029_destino)
print(f'Arquivo ESPDP029 copiado de {ESPDP029_origem} para {ESPDP029_destino}')

shutil.copy(ESPDP015origem, ESPDP015_destino)
print(f'Arquivo ESPDP015 copiado de {ESPDP015origem} para {ESPDP015_destino}')

shutil.copy(PlanACR_origem, PlanACR_destino)
print(f'Arquivo PLANACR copiado de {PlanACR_origem} para {PlanACR_destino}')

