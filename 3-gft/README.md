# Desafio

## Proposta

A proposta do desafio da GFT encontra-se no submódulo "desafio".

## Solução

Para a solução deste desafio de aprendizagem não-supervisionada na plataforma
da *IBM Cloud*, foi utilizado um *Jupyter Notebook* (ver
[notebook.ipynb](solução/notebook.ipynb)), hospedado no
*Watson Studio*, para:

- Agregar as bases de dados de clientes de um banco de varejo, um banco de
  investimentos e uma seguradora
- Tratar os dados, removendo itens duplicados, e transformando os demais para
  um formato adequado para o uso em um modelo de recomendação de produtos
- Gerar regras de associação com um nível adequado de confiabilidade, por meio
  do algotimo [Apriori](https://github.com/tommyod/Efficient-Apriori)
- Preencher o arquivo de respostas, [ANSWERS.csv](solução/ANSWERS.csv), com até
  três produtos por cliente
