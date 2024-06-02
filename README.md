# Box - Assistente Virtual utilizando TVBox

Este projeto tem como objetivo criar um assistente virtual inteligente, acessível e open source, utilizando como hardware uma TVBox. O assistente virtual está disponível apenas em português (Brasil) e recebe comandos a partir da palavra de ativação `Box`.

## Inicialização

### Configuração do ambiente
Os passos a seguir são necessários apenas para a configuração inicial do assistente virtual. Após instalar as dependências não será mais necessário executar os códigos nesta seção.

Como a TVBox utiliza Armbian, supomos a execução dos comandos utilizando o bash. Caso esteja tentando utilizar o Windows para programar/executar o assistente virtual, recomendamos utilizar o [git bash](https://git-scm.com/downloads) como terminal.


1) Crie o ambiente virtual para instalação das dependências

```bash
python -m venv tvbox
```

2) Inicialize o ambiente virtual

```bash
source tvbox/Scripts/activate
```
3) Instale as dependências

```bash
python -m pip install -r requirements.txt
```

> Para sair do ambiente virtual, basta executar o comando `deactivate`.

### Inicialização do assistente virtual
Estando no ambiente virtual criado, basta executar o comando abaixo

```bash
python main.py
```

Ou então, caso não esteja no ambiente virtual, use o comando abaixo

```bash
bash start-assistant.sh
```

O assistente virtual será iniciado, esperando por um comando de voz.
Tente perguntar "Box, que horas são?"

#### Skills e Comandos

| Skill      | Funcionalidade | Descrição                                        | Palavras de ativação                                       | Exemplo                                                                            |
| :---------- | :-------------- | :------------------------------------------------ | :---------------------------------------------------------- | :---------------------------------------------------------------------------------- |
| Assistente | Desligar       | Desliga                                          | `Desligar`<br>`Tchau`<br>`Até logo`<br>`Adeus`             | *Box, até logo*                                                                    |
| Assistente | Saudações      | Responde saudações, como "Olá" ou "Tudo bem?"    | `Olá`<br>`Oi`<br>`Tudo bem?`<br>`Como vai?`                | *Box, tudo bem?*<br>*Olá, Box*                                                     |
| Clock      | Horário atual  | Informa o horário atual                          | `Que horas são`                                            | *Box, Que horas são?*                                                              |
| Clock      | Temporizador   | Inicia um temporizador para o período escolhido. | `Timer`<br>`Temporizador`<br>`Cronometrar`<br>`Cronômetro` | *Box, iniciar timer para 5 segundos*<br>*Box, cronometrar 1 hora e 10 segundos* |
| Piadocas      | Piadocas    | Diz uma piada aleatória | `Piada`<br>`Charada` | *Box, me conte uma piada* |
| Temperature      | Temperatura    | Diz a temperatura na cidade em que o usuário está | `Temperatura` | *Box, qual a temperatura agora?* |
| Temperature      | Temperatura    | Diz a temperatura na cidade pedida pelo usuário | `Temperatura em <cidade>` | *Box, qual a temperatura agora em Campinas?* |



## Instalação de novas bibliotecas
Qualquer instalação de novas biblioteca precisa ser realizada no ambiente `tvbox`:
1. Inicializar o ambiente

```bash
source tvbox/Scripts/activate
```

2. Instalar a biblioteca

```bash
python -m pip install <lib_name>
```
