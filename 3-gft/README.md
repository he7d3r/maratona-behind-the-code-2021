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

A solução proposta ficou em 79º lugar no
[ranking do 3º desafio](https://maratona.dev/ranking/3).

No conjunto, as soluções submetidas para os cinco desafios garantiram o 53º
lugar no [TOP 100 da América Latina](https://maratona.dev/ranking),
e a oportunidade de participar da final da Maratona.
