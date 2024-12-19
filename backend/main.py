from search_team import searchTeam
from get_squad import getSquad
from get_performance import get_performance_detail
from team_data import TeamData

def main():
    print("\n=== Bienvenido al Sistema de Estadísticas de Fútbol ===")
    
    team_data = TeamData()
    
    while True:
        print("\nMenú Principal:")
        print("1. Buscar equipo")
        print("2. Ver plantilla del equipo")
        print("3. Ver estadísticas de jugador")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            print("\n--- Búsqueda de Equipo ---")
            searchTeam()
            
        elif opcion == "2":
            print("\n--- Plantilla del Equipo ---")
            getSquad()
            
        elif opcion == "3":
            print("\n--- Estadísticas de Jugador ---")
            get_performance_detail()
            
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema!")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    finally:
        print("\n¡Hasta luego!")
