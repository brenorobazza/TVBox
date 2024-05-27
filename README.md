# Assistente Virtual para domicílios utilizando TVBox

Este projeto tem como objetivo criar um assistente virtual inteligente, acessível e open source, para domicílios, utilizando para isso uma TVBox.

## Inicialização

### Configuração do ambiente
Para a primeira inicialização, recomendamos criar um ambiente virtual para conter todos os pacotes necessários

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

### Inicialização do assistente virtual
Basta executar o comando abaixo

```bash
python main.py
```

O assistente virtual será iniciado, esperando por um comando de voz.
Tente perguntar "que horas são?"

Para sair do ambiente virtual, basta executar o comando `deactivate`.

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