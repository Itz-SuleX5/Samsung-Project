import requests
import matplotlib.pyplot as plt
from team_data import TeamData
from get_market_value import get_player_market_value

def show_players():
    team_data = TeamData()
    if not team_data.players_dict:
        return None
        
    print("\nLista de jugadores disponibles:")
    for idx, name in enumerate(team_data.players_dict.keys()):
        print(f"{idx}: {name}")
    
    while True:
        try:
            selected = int(input("\nSeleccione el número del jugador: "))
            if 0 <= selected < len(team_data.players_dict):
                return list(team_data.players_dict.values())[selected]
            else:
                print("Número inválido. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def get_performance_detail():
    team_data = TeamData()
    if team_data.id is None:
        print("Primero debe buscar un equipo (opción 1)")
        return
    
    if not team_data.players_dict:
        print("Primero debe obtener la plantilla del equipo (opción 2)")
        return
        
    player_id = show_players()
    if player_id is None:
        return
        
    season_id = input("Ingrese el ID de la temporada (ejemplo: 2022): ")
    competition_id = input("Ingrese el ID de la competición (ejemplo: ES1): ")
    
    url = "https://transfermarket.p.rapidapi.com/players/get-performance-detail"
    
    querystring = {
        "id": str(player_id),
        "seasonID": season_id,
        "competitionID": competition_id,
        "domain": "de"
    }
    
    headers = {
        "x-rapidapi-key": "bb18653d4dmsh9763ddd8e0a6f76p1896cejsnb2c4604c6ecc",
        "x-rapidapi-host": "transfermarket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    # Inicializar contadores
    total_stats = {
        'Goles': 0,
        'Asistencias': 0,
        'Goles en Propia': 0,
        'Tarjetas Amarillas': 0,
        'Tarjetas Rojas': 0,
        'Minutos Jugados': 0
    }
    
    # Sumar estadísticas de todos los partidos
    if 'matchPerformance' in data:
        for match in data['matchPerformance']:
            if 'performance' in match:
                perf = match['performance']
                total_stats['Goles'] += int(perf.get('goals', 0) or 0)
                total_stats['Asistencias'] += int(perf.get('assists', 0) or 0)
                total_stats['Goles en Propia'] += int(perf.get('ownGoals', 0) or 0)
                total_stats['Tarjetas Amarillas'] += 1 if perf.get('yellowCardMinute') else 0
                total_stats['Tarjetas Rojas'] += 1 if perf.get('redCardMinute') else 0
                total_stats['Minutos Jugados'] += int(perf.get('minutesPlayed', 0) or 0)
        
        # Obtener el valor de mercado del jugador
        market_value = get_player_market_value(player_id, f"{season_id}/{int(season_id)+1}")
        
        # Crear gráfico de barras
        plt.figure(figsize=(12, 6))
        bars = plt.bar(total_stats.keys(), total_stats.values())
        
        # Personalizar el gráfico con el nombre del jugador y valor de mercado
        player_name = list(team_data.players_dict.keys())[list(team_data.players_dict.values()).index(player_id)]
        plt.title(f'Estadísticas de {player_name} - Temporada {season_id}\nValor de mercado: {market_value}')
        plt.xticks(rotation=45)
        
        # Añadir valores sobre las barras
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()
        
        # Mostrar totales
        print("\nEstadísticas totales:")
        for stat, value in total_stats.items():
            print(f"{stat}: {value}")
    else:
        print("No se encontraron datos de rendimiento para este jugador")
    
    return data

if __name__ == "__main__":
    from search_team import searchTeam
    from get_squad import getSquad
    
    searchTeam()
    getSquad()
    get_performance_detail()
