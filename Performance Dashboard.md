#QLIKSENSE - Dashboard

#Ferramenta utilizada: QLIKSENSE

#Escopo do projeto:
A ideia do projeto era reunir informações de venda de uma unidade, vindos do sistema principal e informações de acompanhamento sobre projetos que circularam pela 
plataforma web da empresa. Ambas bases bastante grandes e com muitas colunas, trazer isso de forma simples e objetiva para a área ter uma ideia de como está 
desempenhando no período selecionado.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Construção:
Modelo utilizado foi o modelo estrela, com as informações de movimento ao centro de dimensões nas extremidades.

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/c36470de-e10f-4e86-9033-f7f7578a73c1)



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Parte de script:

Os pontos de maiores complexidade deste projeto foram que na base de projetos as informações sobre a forma de pagamento estavam em colunas nesta base, 
mas em linhas na base do sistema principal.

(Fato-A)

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/a8bfa9f0-d420-4d5e-8884-19c807215212)


(Fato-B)
![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/7813a91c-ca2d-48c9-b216-1540ee2d1038)

Então foi necessário estabelecer um comportamento, e o escolhido foi em linhas onde para cada fatura, teriamos uma ou mais linhas de formas de pagamento, 
o motivo foi pois no sistema da empresa (Fato-A) tínhamos muito mais formas de pagamento para classificar, sendo mais fácil utiizar as da plataforma 
(Fato-B), para depois conseguirmos totalizar. 

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/126bc0bc-3dcf-4d4b-aaaa-22ab875d446d)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Visualizações
Definido um escopo com a àrea solicitante, onde foi passado quais eram as perguntas que eles queriam ver as respostas e também algumas informações que já 
vinham construindo manualmente através de relatórios em Excel.

Visão do faturamento x orçamento

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/6701e98b-c799-4695-958e-efc0a1ab0377)


Evolução forma de pagamento: 

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/1ed5331a-d9e3-40c7-9743-326366024e05)



Acompanhamento por instituição financeira escolhida:

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/fcf71590-3e11-47f5-90c3-60e93dcffbb4)



Explorar qual forma de pagamento é a mais popular em cada região:

![image](https://github.com/Ygorkelevra93/Projects/assets/121832957/3141f5c1-f82c-47a8-b0ad-b24f5876e0f1)




 
