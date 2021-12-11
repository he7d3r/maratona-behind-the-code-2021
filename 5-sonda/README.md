# Desafio

## Proposta

A proposta do desafio da SONDA encontra-se no submódulo "desafio".

## Solução

Para a solução deste desafio de ciência de dados na plataforma da *IBM Cloud*,
foi utilizado um *Jupyter Notebook*, hospedado no *Watson Studio*
(ver [notebook.ipynb](solução/notebook.ipynb)), para analisar dados de clientes
de uma empresa de telecomunicações (ver [dataset.csv](desafio/assets/data/dataset.csv))
e desenvolver modelos de aprendizagem de máquina para predizer se haverá ou
não a perda de um cliente (_churn_). Os modelos serão comparados, e o que tiver
o melhor desempenho em termos do _F1 score_ será utilizado para fazer previsões
para novos clientes e indicar na coluna `CHURN` do arquivo de respostas
(ver [answers.csv](desafio/assets/answers.csv)) quais deles serão perdidos.
