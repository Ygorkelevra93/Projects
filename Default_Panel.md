# Default panel

## Escopo do projeto:
Equipe solicitou um painel para que pudessem acompanhar a performance das cobranças realizadas, metas de clientes e obterem de forma rápida informações sobre suas carteiras de clientes, 
desde um nível macro de informações como KPIs de inadimplencia, aging da dívida, até o detalhe da informação de apontar quando foi feita a última cobrança e por qual usuário.

## Esquema do projeto:
![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/9194444b-6249-43a0-b9ad-3c911e400002)


## Feature 1 - Envio de cobrança automática 

### Bases Utilizadas:
- accounts receivable as ACR
- Customers as CRM
- Billing_groups as BG

## Tabela de contas a receber. 
Todos os dias pela manhã e no horario do intervalo, uma rotina do python vai ler o relatório gerado do sistema ACR e fazer o seguinte tratamento:
Vai trazer informações de email de cobrança CRM e informações sobre qual grupo de cobrança aquele cliente pertence BG.
E salvamos em um local compartilhado.

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/c5ad68a0-fcce-4f3b-87b3-336c5a2461b8)


Esta base tratada vai servir para alimentar outra planilha que deixamos para a equipe acessar e fazer a seleção dos clientes que deseja efetuar a cobrança. 
* Projeto também poderia ser atendido de forma automática, sem a equipe entrar para fazer o disparo. Mas foi uma escolha do time,
para acompanhar quais clientes estão sendo feitas as cobranças.

### Worksheet 
A planilha de cobrança possui 3 macros:
1 - A primeira para ser atualizada com as informações tratadas atuais.
2 - A segunda para selecionar os clientes a serem cobrados
3 - Para fazer o disparo dos emails e registro em uma aba que será posteriormente lido pelo QLIK SENSE.

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/5b580315-91ab-42c9-8c11-0af29a80e7ef)

 
 
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

## Feature 2 - Dashboard

O dashboard vai reunir as principais informações para ajudar na gestão das carteiras.
Foi construída com informações das bases CRM, ACR e histórico de cobrança trazida da rotina de cobrança acima.
Como ponto de maior complexidade aqui temos o tratamento da tabela fato ACR, além de adicionarmso colunas calculadas de aging, 
regiões, supervisores de cada cliente, foi feito aqui um procedimento para armazenagem das bases, para que tenhamos o acompanhamento 
de como estava a posição de cobrança em qualquer data selecionada. 
(Rotinas executadas em extratores diferentes da área, que fazem a leitura dessa ACR e concatenam uma sob a outra)

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/4e1519c7-1294-49f7-9d9f-1a11acaa4f74)


### Neste Dashboard:
Acima temos os KPIs com indicadores de inadimplência e contadores de matrizes ativas.

### Nos gráficos temos:
Canto superior esquerdo, gráfico de linha contendo a evolução da inadimplência considerando todas as datas;
Canto superior direito, gráfico de barras com a representação do montante em cada canal de venda, e que 
se selecionar ele habilita o drill down para o subcanal;
Canto inferior esquerdo,  gráfico de barras empilhadas com as evolução do montante em cada periodo e separado por aging;
Canto inferior direito, identico ao de cima porém este mostra a separação por localidade.

E todos tem a opção ao lado de exportar para excel

