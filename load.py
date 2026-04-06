from sqlalchemy import create_engine
import urllib.parse

def load_to_postgresql(df, db_user, db_password, db_host, db_port, db_name):
    "charge le DataFrame dans postgreSQL"

    if df is None:
        print("Aucune donnée a charger.")
        return
    try:
        encoder_password = urllib.parse.quote_plus(db_password)

        engine_url = f"postgresql+psycopg2://{db_user}:{encoder_password}@{db_host}:{db_port}/{db_name}"
        engine = create_engine(engine_url)

        df.to_sql('historique_meteo', engine, if_exists='append', index=False)

        print(f"[{df['data_heure'].iloc[0]}] données insérées dans PostgreSQL pour {df['ville'].iloc[0]}.")

        except Exception as e: 
            print ( f"Erreur lors du chargement dans PostgreSQL : {e}")
