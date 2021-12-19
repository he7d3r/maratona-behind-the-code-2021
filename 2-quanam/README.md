# Desafio

## Proposta

A proposta do desafio da Quanam encontra-se no submódulo "desafio".

## Solução

Para a solução do desafio na plataforma da *IBM Cloud*:

1. Foi utilizado o *Cloud Functions* para criar uma API *serverless* que recebe
dados de sensores e retorna uma lista de alertas quando as medições de um ou
mais destes sensores alcançam valores diferentes do esperado.
2. Com o *Node-RED* (ver [node-red-flows.json](solução/node-red-flows.json)),
foram coletados documentos em formato JSON de um dispositivo IOT da Quanam, via
protocolo MQTT, para posterior armazenamento em um banco de dados *NoSQL*
(o *Cloudant*):<div align="center"><img width="50%" src="./solução/node-red-screenshot.png" alt='Screenshot do fluxo do Node-RED'></div>
  Depois, esses dados foram salvos em um arquivo [iot.csv](solução/iot.csv) e
explorados em um *Jupyter notebook* (ver [notebook.ipynb](solução/notebook.ipynb)),
hospedado no *Watson Studio*, com o qual também foram treinados modelos de
*machine learning* para uma comparação de seu desempenho. O melhor modelo foi
então utilizado para fazer previsões do ritmo cardíaco de pacientes, e preencher
a coluna `RYTHM` do arquivo [answers.csv](desafio/assets/answers.csv),
garantindo o 17º lugar no
[ranking do 2º desafio](https://maratona.dev/ranking/2).

No conjunto, as soluções submetidas para os cinco desafios garantiram o 53º
lugar no [TOP 100 da América Latina](https://maratona.dev/ranking),
e a oportunidade de participar da final da Maratona.
