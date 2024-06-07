import random


def get_question(index: int):
    """
    Define a pergunta a ser feita.

    Args:
        int: index da pergunta no dicionário.

    Returns:
        string: contém a frase da pergunta a ser feita.
    """

    questions = {
        1: "Qual o livro mais vendido no mundo após a Bíblia?",
        2: "Atualmente, quantos elementos químicos a tabela periódica possui?",
        3: "Em que período da pré-história o fogo foi descoberto?",
        4: "Qual a montanha mais alta do Brasil?",
        5: "Em qual local da Ásia o português é língua oficial?",
        6: "Júpiter e Plutão são os correlatos romanos de quais deuses gregos?",
        7: "As pessoas de qual tipo sanguíneo são consideradas doadoras universais?",
        8: "Qual é o maior arquipélago da Terra?",
        9: "Que animal gruguleja?",
        10: "Em que país nasceu Clarice Lispector?",
    }
    return questions[index]


def get_items(index: int):
    """
    Define as alternativas da pergunta.

    Args:
        int: index das alterativas no dicionário.

    Returns:
        string: contém a frase das alternativas da pergunta.
    """

    items = {
        1: "A, O Senhor dos Anéis. \n B, Dom Quixote. \n C, O Pequeno Príncipe. \n D, Um Conto de Duas Cidades.",
        2: "A, 113. \n B, 109. \n C, 108. \n, D, 118.",
        3: "A, Neolítico. \n B, Paleolítico. \n C, Idade dos Metais. \n D, Período da Pedra Polida.",
        4: "A, Pico da Neblina. \n B, Pico Paraná. \n C, Monte Roraima. \n D, Pico da Bandeira.",
        5: "A, Índia. \n B, Filipinas. \n C, Moçambique. \n D, Macau.",
        6: "A, Ares e Hermes. \n B, Cronos e Apolo. \n C, Zeus e Hades. \n D, Dionísio e Deméter.",
        7: "A, Tipo A. \n B, Tipo B. \n C, Tipo O. \n D, Tipo AB.",
        8: "A, Filipinas. \n B, Indonésia. \n C, Bahamas. \n D, Maldivas.",
        9: "A,  o pavão. \n B, a garça. \n C, a cacatua. \n D, o peru.",
        10: "A, Portugal. \n B, Rússia. \n C, Brasil. \n D, Ucrânia.",
    }
    return items[index]


def get_answer(index: int):
    """
    Define a resposta correta da pergunta.

    Args:
        int: index da pergunta no dicionário.

    Returns:
        string: contém a frase da resposta correta.
    """
    answers = {
        1: [
            "B, Dom Quixote",
            "Sendo um clássico da literatura espanhola, Miguel de Cervantes escreveu sua obra em duas partes, uma em 1605 e a outra em 1615.",
        ],
        2: [
            "D, 118",
            "Os últimos elementos descobertos foram adicionados a tabela periódica em 2016.",
        ],
        3: [
            "B, Paleolítico",
            "Através do atrito entre pedaços de madeira e pedra, os humanos aprenderam a produzir fogo.",
        ],
        4: [
            "A, Pico da Neblina",
            "Localizado no Amazonas, O Pico da Neblina é o ponto mais elevado do Brasil, contando com 2995 metros de altura.",
        ],
        5: [
            "D, Macau",
            "Macau foi território de Portugal até 1999 e possui duas línguas oficiais, mandarim e português.",
        ],
        6: [
            "C, Zeus e Hades",
            "Na mitologia romana, Zeus é considerado o pai dos deuses e tem Júpiter como seu correlato grego, enquanto Hades possui Plutão como seu correlato grego.",
        ],
        7: [
            "C, Tipo O",
            "O sangue O pode ser doado para todos os outros tipos sanguíneos, entretanto, somente recebe doações de outra pessoa com sangue O.",
        ],
        8: [
            "B, Indonésia",
            "Considerado o maior arquipélago do mundo, a Indonésia reúne um conjunto de 17508 ilhas.",
        ],
        9: [
            "D, o peru",
            "Grugulejar é o som emitido por essa ave nativa das florestas da América do Norte.",
        ],
        10: [
            "D, Ucrânia",
            "Clarice Lispector nasceu na Ucrânia, mas chegou ao Brasil ainda bebê.",
        ],
    }

    answer = f"Se você disse a alternativa {answers[index][0]}, você acertou! {answers[index][1]}"
    return answer


def select_questions():
    """
    Seleciona 3 perguntas aleatoriamente para serem respondidas.

    Args:
        None

    Returns:
        array: lista de números referentes a pergunta a ser feita.
    """
    question_indexes = random.sample(range(1, 11), 3)
    return question_indexes
