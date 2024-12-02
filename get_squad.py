import requests
from team_data import TeamData

players_dict = {}  

def getSquad():
    team_data = TeamData()
    
    if team_data.id is None:
        print("Primero debes buscar un equipo usando searchTeam()")
        return None
        
    season_id = input("Ingrese el ID de la temporada (ejemplo: 2022): ")
    
    url = "https://transfermarket.p.rapidapi.com/clubs/get-squad"
    
    querystring = {
        "id": str(team_data.id),
        "saison_id": season_id,
        "domain": "de"
    }
    
    headers = {
        "x-rapidapi-key": "bb18653d4dmsh9763ddd8e0a6f76p1896cejsnb2c4604c6ecc",
        "x-rapidapi-host": "transfermarket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    team_data.players_dict.clear()
    
    if 'squad' in data:
        for player in data['squad']:
            if 'name' in player and 'id' in player:
                team_data.players_dict[player['name']] = player['id']
        print(f"\nJugadores encontrados: {len(team_data.players_dict)}")
        for idx, name in enumerate(team_data.players_dict.keys()):
            print(f"{idx}: {name}")
    
    return data

if __name__ == "__main__":
    from search_team import searchTeam
    searchTeam() 
    squad_data = getSquad()
    if squad_data:
        print("\nDiccionario de jugadores:")
        for name, player_id in team_data.players_dict.items():
            print(f"{name}: {player_id}")
