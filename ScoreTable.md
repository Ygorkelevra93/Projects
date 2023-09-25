# ScoreTable - SQL 

Escopo do projeto:
O sistema que a empresa utiliza para análise de crédito e aprovação de pedidos possui uma tela de diagnóstico para cada cliente com informações e pontuações.
Ao todo mais de pontos de informação relevantes para o processo.
O solicitante gostaria que fosse extraído do banco um relatório que trouxesse a informação no formato de tabela, já que o sistema original não tinha esse relatório em sua versão standard.

Ferramentas utilizadas: 
SQL Server + QLIKSENSE


Tela de diagnóstico com as informações solicitadas em formato de tabela:  (+3000 clientes)
![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/e1da57f6-813c-4e95-a1d0-cf294f121294)


O ponto de dificuldade aqui foi, que como a política da empresa é complexa, muitos dos parâmetros como políticas, classificações, e as próprias métricas foram adicionadas
sob demanda às tabelas do sistema terceiro, então foram feitos os estudos e validações sobre o relacionamento. 
E quando precisou extrair a informação das pontuações de cada métrica e essa informação se repetia-se muitas vezes para cada cliente, conforme todas as métricas.
 ![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/018dafa1-479a-4927-afe1-70e42f90ee61)

A solução foi usar uma função de agregação "Min" e "Case" para onde cada vez que aquele 
texto da métrica fosse encontrado, ele trouxesse o valor da pontuação e nomear isso como uma nova coluna.
![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/825c9f30-d1e1-4b3c-8208-ffe314656b6a)


A partir dali adicionamos algumas validações que o usuário também solicitou e uma coluna para colocarmos a data, assim poderá ser feito até uma análise evolutiva daquele comportamento.

O resultado final é uma tabela onde o solicitante pode filtrar e comparar comportamento VS inadimplência, valor de limite concedido, valor de títulos pagos. 
![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/a1978320-ce38-4f6e-a128-42647b81b450)


