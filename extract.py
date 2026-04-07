import requests

def extract_weather_data(city, api_key):
    " recupere les données météo brutes depuis l'API OpenWeatherMap. "
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


    try :
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Erreur d'ectraction : {e}")
        return None