import requests
import json

def get_jobs(domaine : str, access_token : str):
    url = 'https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        'domaine': domaine
    }

    response = requests.get(url, headers=headers, params=params)
    print(response)
    try:
        json_data = response.json()
        print(f"La réponse JSON : {json_data}")
    except json.JSONDecodeError as e:
        print("Erreur de décodage JSON :", e)
        print("Contenu de la réponse :", response.text)

    if response.status_code == 206:
        data = response.json()
        # Traitement des données
        return data
    else:
        print('La requête a échoué avec le code:', response.status_code)