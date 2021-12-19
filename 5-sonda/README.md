# Desafio

## Proposta

A proposta do desafio da SONDA encontra-se no submódulo "desafio".

## Solução

Para a solução deste desafio de ciência de dados na plataforma da *IBM Cloud*,
foi utilizado um *Jupyter Notebook*, hospedado no *Watson Studio*
(ver [notebook.ipynb](solução/notebook.ipynb)), para analisar dados de clientes
de uma empresa de telecomunicações (ver [dataset.csv](desafio/assets/data/dataset.csv))
e desenvolver modelos de aprendizagem de máquina para predizer se haverá ou
não a perda de um cliente (_churn_). Os modelos foram comparados, e o que teve
o melhor desempenho em termos do _F1 score_ foi utilizado para fazer previsões
para novos clientes e indicar na coluna `CHURN` do arquivo de respostas
(ver [answers.csv](desafio/assets/answers.csv)) quais deles serão perdidos.

A solução enviada ficou em 96º lugar no
[ranking do 5º desafio](https://maratona.dev/ranking/5).

No conjunto, as soluções submetidas para os cinco desafios garantiram o 53º
lugar no [TOP 100 da América Latina](https://maratona.dev/ranking),
e a oportunidade de participar da final da Maratona.
