# Assistente Virtual para domicílios utilizando TVBox

Este projeto tem como objetivo criar um assistente virtual inteligente, acessível e open source, para domicílios, utilizando para isso uma TVBox.

## Inicialização

### Configuração do ambiente
Para a primeira inicialização, recomendamos utilizar o `git bash` e criar um ambiente virtual para conter todos os pacotes necessários

1) Crie o ambiente virtual

```bash
python -m venv tvbox
```

2) inicialize o ambiente

```bash
source tvbox/Scripts/activate
```
3) Instale as dependências

```bash
python -m pip install -r requirements.txt
```

> Para sair do ambiente virtual, basta executar o comando `deactivate`.

### Inicialização do assistente virtual
Basta executar o comando abaixo

```bash
bash start-assistant.sh
```

O assistente virtual será iniciado, esperando por um comando de voz.
Tente perguntar "Box, que horas são?"

#### Skills e Comandos

| Skill      | Funcionalidade | Descrição                                        | Palavras de ativação                                       | Exemplo                                                                            |
| ---------- | -------------- | ------------------------------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Assistente | Desligar       | Desliga                                          | `Desligar`<br>`Tchau`<br>`Até logo`<br>`Adeus`             | *Box, até logo*                                                                    |
| Assistente | Saudações      | Responde saudações, como "Olá" ou "Tudo bem?"    | `Olá`<br>`Oi`<br>`Tudo bem?`<br>`Como vai?`                | *Box, tudo bem?*<br>*olá, Box*                                                     |
| Clock      | Horário atual  | Informa o horário atual                          | `Que horas são`                                            | *Box, Que horas são?*                                                              |
| Clock      | Temporizador   | Inicia um temporizador para o período escolhido. | `Timer`<br>`Temporizador`<br>`Cronometrar`<br>`Cronometro` | *Box, inicar timer para 5 segundos*<br>*Box, cronometrar 1 hora e 10 segundos* |



## Instalação de novas bibliotecas
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