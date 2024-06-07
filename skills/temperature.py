import re
import requests

#documentação da api wttr https://github.com/chubin/wttr.in

def get_city_from_ip():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    city = data.get("city")
    return city
    
def extract_city_from_text(text):
    match = re.search(r'temperatura(?:\s+em\s+([\w\s]+))?', text, re.IGNORECASE)
    if match and match.group(1):
        return match.group(1).strip()
    return None

def get_city(text):
    city = extract_city_from_text(text)
    if city == None:
        city = get_city_from_ip()
    return city


def get_temperature(text):   
    city = get_city(text)
    
    url = f"http://wttr.in/{city}?format=%t"
    response = requests.get(url)
    temperature = response.text.strip().replace("+", "")
    
    return f"Está {temperature} em {city}" 

#def get_weather_forecast(text):
    city = get_city(text)

    url = f"http://wttr.in/{city}?format=%C"
    response = requests.get(url)
    forecast = response.text.strip()


    return f"Previsão do tempo para {city}: {forecast}"



