import re
import requests

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

def get_temperature(text):
    
    city = extract_city_from_text(text)
    if city == None:
        city = get_city_from_ip()

    url = f"http://wttr.in/{city}?format=%t"
    response = requests.get(url)
    temperature = response.text.strip()
    
    return f"Está {temperature} em {city}" 