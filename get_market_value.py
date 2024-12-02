import requests
from team_data import TeamData

def get_player_market_value(player_id, season):
    url = "https://transfermarket.p.rapidapi.com/players/get-market-value"
    
    headers = {
        "x-rapidapi-key": "bb18653d4dmsh9763ddd8e0a6f76p1896cejsnb2c4604c6ecc",
        "x-rapidapi-host": "transfermarket.p.rapidapi.com"
    }
    
    querystring = {"id": str(player_id), "domain": "de"}
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        
        if "marketValueDevelopment" in data:
            # Obtener el año anterior al inicio de la temporada
            season_start_year = int(season.split('/')[0])
            target_date = f"12.{season_start_year-1}"
            
            # Buscar el valor de mercado más cercano a diciembre del año anterior
            for value_data in data["marketValueDevelopment"]:
                if value_data["date"].startswith(target_date):
                    return f"{value_data['marketValue']} {value_data['marketValueCurrency']}"
            
            # Si no se encuentra el valor exacto, buscar el más cercano a esa fecha
            closest_value = None
            closest_diff = float('inf')
            
            for value_data in data["marketValueDevelopment"]:
                date_parts = value_data["date"].split('.')
                if len(date_parts) == 2:
                    month, year = map(int, date_parts)
                    current_date = year * 12 + month
                    target_date_value = (season_start_year-1) * 12 + 12
                    diff = abs(current_date - target_date_value)
                    
                    if diff < closest_diff:
                        closest_diff = diff
                        closest_value = value_data
            
            if closest_value:
                return f"{closest_value['marketValue']} {closest_value['marketValueCurrency']}"
        
        return "Valor no disponible"
        
    except Exception as e:
        print(f"Error al obtener el valor de mercado: {e}")
        return "Valor no disponible"
