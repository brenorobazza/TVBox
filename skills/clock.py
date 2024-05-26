import time


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

