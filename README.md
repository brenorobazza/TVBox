# Assistente Virtual para domicílios utilizando TVBox

Este projeto tem como objetivo criar um assistente virtual inteligente, acessível e open source, para domicílios, utilizando para isso uma TVBox.

## Inicialização
Basta executar o comando abaixo

```bash
./start-assistant.sh
```
O assistente virtual será iniciado, esperando por um comando de voz.
Tente perguntar "que horas são?"

## Instalação de bibliotecas
Qualquer instalação de novas biblioteca precisa ser realizada no ambiente `tvbox`:
1. Inicializar o ambiente

```bash
source tvbox/Scripts/activate
```

2. Instalar a biblioteca

```bash
py -m pip install <lib_name>
```
No ambiente, você pode também testar o assistente virtual diretamente. Basta executar
```bash
py main.py
```

3. Sair do ambiente

```bash
deactivate
```