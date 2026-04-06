import pandas as pandasimp
from datetime import datetime


def transform_weather_data(raw_data):
    "Transforme le Json Brut en DataFrame Pandas."

    if not raw_data:
        return None
    
    weather_dict = {
        'ville' : raw_data['name'],
        'temperature_celsius' : raw_data['main']['temp'],
        'humidite_pourcentage' : raw_data['main'][humidity]
        'description': raw_data['weather'][0]['description'],
        'date_heure': datetime.fromtimestamp(raw_data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    }

    return pd.DataFrame(weather_dict)