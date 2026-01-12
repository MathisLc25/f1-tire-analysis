import fastf1
import os

CACHE_DIR = 'cache'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

fastf1.Cache.enable_cache(CACHE_DIR)

def get_session_data(year, location, session_type='R'):
    """
    Fonction pour charger une session spécifique (Race, Qualifying, etc.)
    """
    try:
        session = fastf1.get_session(year, location, session_type)
        session.load()
        return session
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return None

if __name__ == "__main__":

    print("Test du chargement des données...")
    test_session = get_session_data(2024, 'Silverstone')
    if test_session:
        print(f"Session chargée : {test_session.event['EventName']} {test_session.event.year}")