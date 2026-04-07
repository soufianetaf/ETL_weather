# 🌤️ Pipeline ETL Météo (Python & PostgreSQL)

Un projet de Data Engineering simple illustrant la création d'un pipeline ETL (Extract, Transform, Load) automatisé en Python. Le script récupère les données météorologiques en temps réel depuis une API, les nettoie, et les stocke dans une base de données relationnelle.

## 🚀 Fonctionnalités

* **Extract :** Récupération des données météo brutes au format JSON via l'API [OpenWeatherMap](https://openweathermap.org/).
* **Transform :** Nettoyage, sélection et formatage des données (conversion des timestamps, gestion des types) à l'aide de `pandas`.
* **Load :** Insertion sécurisée des données propres dans une base de données **PostgreSQL** locale via `SQLAlchemy`.
* **Orchestration :** Exécution planifiée et automatisée à l'aide de la bibliothèque `schedule`.

## 🛠️ Technologies utilisées

* **Langage :** Python 3.x
* **Manipulation de données :** Pandas
* **Base de données :** PostgreSQL, SQLAlchemy, psycopg2
* **Requêtes HTTP :** Requests
* **Gestion des secrets :** python-dotenv

## 📁 Structure du projet

```text
ETL_weather/
│
├── .env                 # Variables d'environnement (Non inclus sur Git)
├── .gitignore           # Fichiers ignorés par Git
├── extract.py           # Module d'extraction (Appel API)
├── transform.py         # Module de transformation (Pandas)
├── load.py              # Module de chargement (PostgreSQL)
├── main.py              # Script principal et orchestrateur
└── README.md            # Documentation du projet