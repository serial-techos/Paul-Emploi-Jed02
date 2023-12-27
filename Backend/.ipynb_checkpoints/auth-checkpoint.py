import requests


def get_token(client_id : str, client_secret : str):
    """ Fetch a token from Pole Emploi API 

    Parameters
    ----------
    client_id : str
        
    client_secret : str
      
    Returns
    -------
    str
        a token 
    """
    url = "https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "api_offresdemploiv2 o2dsoffre"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        print("Access Token:", access_token)
        return access_token 
    else:
        print("Error:", response.status_code, response.text)
        return None
   