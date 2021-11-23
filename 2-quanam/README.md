# Desafio

## Proposta

A proposta do desafio da Quanam encontra-se no submódulo "desafio".

## Solução

Para a solução do desafio na plataforma da *IBM Cloud*, foi utilizado o
*Node-RED* (ver [node-red-flows.json](solução/node-red-flows.json)) para
coletar documentos em formato JSON de um dispositivo IOT da Quanam via
protocolo MQTT e armazená-los em um banco de dados *NoSQL* (o *Cloudant*):

<div align="center">
<img width="50%" src="./solução/node-red-screenshot.png" alt='Screenshot do fluxo do Node-RED'>
</div>

Depois, esses dados serão explorados em um *Jupyter notebook* (ver
[notebook.ipynb](solução/notebook.ipynb)), hospedado no *Watson Studio*, com o
qual também serão treinados modelos de *machine learning* para uma
comparação de seu desempenho. O melhor modelo será então utilizado para fazer
previsões do ritmo cardíaco de pacientes.