import os
import time
import schedule
from dotenv import load_dotenv


dossier_actuel = os.path.dirname(os.path.abspath(__file__))
chemin_env = os.path.join(dossier_actuel, '.env')

print("\n--- 🔍 TEST DU FICHIER .ENV ---")
print(f"Je cherche le fichier ici : {chemin_env}")
print(f"Le fichier existe-t-il vraiment ? : {os.path.exists(chemin_env)}")
print("-------------------------------\n")

# On force Python à lire ce fichier précis
load_dotenv(chemin_env)


from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_postgresql

# charger les variable du fichier .env

load_dotenv

def run_etl():

    API_KEY = os.getenv("APIKEY")
    CITY = os.getenv("CITY")

    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # 1 E

    donnes_brutes = extract_weather_data(CITY, API_KEY)

    #2 T 

    donnes_propres = transform_weather_data(donnes_brutes)

    #3 L
    load_to_postgresqll = load_to_postgresql(donnes_propres, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)


if __name__ == "__main__":

    run_etl()

    schedule.every(1).hours.do(run_etl)

    print(" Le pipline ETL est actif ")

    while True:
        schedule.run_pending()
        time.sleep(1)
