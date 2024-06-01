import re
import time
from datetime import datetime, timedelta
import threading
import queue

message_queue = queue.Queue()

def humanize_time(time_str):
    """
    Converte um horário em um texto legível para humanos.
    Exemplo: Recebe "15:01:00" e retorna "São 15 horas e 1 minuto."
    """
    time_list = time_str.split(":")
    hours = int(time_list[0])
    minutes = int(time_list[1])
    return f"São {hours} horas e {minutes} minutos."


def what_time_is_it():
    """
    Verifica o horário atual, torna em um texto legível e retorna para a função que o chamou.
    """
    
    t = time.strftime("%H:%M:%S")
    to_speech = humanize_time(t)
    return to_speech


'''
FUNÇÕES PARA O TEMPORIZADOR
'''

def parse_time(text):
    """
    Recebe um texto qualquer, reconhece o período no texto e retorna o período em segundos 
    """
    
    patterns = {
        "hours": r"(\d+)\s*(horas|hora|h)",
        "minutes": r"(\d+)\s*(minutos|minuto|mins|min|m)",
        "seconds": r"(\d+)\s*(segundos|segundo|secs|sec|s)",
    }

    hours = 0
    minutes = 0
    seconds = 0

    for match in re.findall(patterns["hours"], text, re.IGNORECASE):
        hours += int(match[0])
    for match in re.findall(patterns["minutes"], text, re.IGNORECASE):
        minutes += int(match[0])
    for match in re.findall(patterns["seconds"], text, re.IGNORECASE):
        seconds += int(match[0])

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def timer_thread(future_time, message_queue):
    """
    Executa uma verificação contínua até que o horário atual atinja o horário configurado
    """
    while datetime.now() < future_time:
        time.sleep(1)
    message_queue.put("timer_finished")


def create_timer(text):
    """
    Recebe texto que contenha um tempo e cria um timestamp para agora + o tempo pedido pelo usuário.
    Quando o timestamp for alcançado, retorna aviso ao usuário
    """
    
    seconds = parse_time(text)
    future_time = datetime.now() + timedelta(seconds=seconds)
    print(f"Temporizador iniciado para {future_time}.")

    thread = threading.Thread(target=timer_thread, args=(future_time, message_queue))
    thread.start()


def timer_finished():
    """
    Função chamada quando o timer finaliza
    """
    
    print("Temporizador finalizado!")

# create_timer("timer para 10 segundos")