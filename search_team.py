import requests
import json
from team_data import TeamData

def searchTeam():
    team_data = TeamData()
    
    team_name = input("Ingrese el nombre del equipo a buscar: ")
    
    url = "https://transfermarket.p.rapidapi.com/search"
    
    querystring = {"query": team_name, "domain":"de"}
    
    headers = {
        'x-rapidapi-key': "bb18653d4dmsh9763ddd8e0a6f76p1896cejsnb2c4604c6ecc",
        'x-rapidapi-host': "transfermarket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    json_data = response.json()
    
    if 'clubs' in json_data and len(json_data['clubs']) > 0:
        team_data.id = json_data['clubs'][0]['id']
        print(f"ID del equipo encontrado: {team_data.id}")
        return team_data.id
    else:
        print("Error de busqueda")
        team_data.id = None
        return None

if __name__ == "__main__":
    searchTeam()
