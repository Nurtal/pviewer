import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



def load_json(data_file:str) -> dict:
    """ """

    # load data
    with open(data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Return data as dictionnary
    return data



def display_timeline(data:dict):
    """ """
    
    # Liste pour stocker tous les événements
    events = []
    
    # Extraction et traitement des événements des actes
    for event in data.get('actes', []):
        # Conversion du timestamp en objet datetime (gestion du "Z" pour UTC)
        dt = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
        label = f"Acte: {event['ccam']}"
        events.append({'datetime': dt, 'label': label, 'type': 'acte'})
    
    # Extraction et traitement des événements du diagnostic
    for event in data.get('diagnostic', []):
        dt = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
        label = f"Diagnostic: {event['cim10']}"
        events.append({'datetime': dt, 'label': label, 'type': 'diagnostic'})
    
    # Tri des événements par date
    events.sort(key=lambda x: x['datetime'])
    
    # Création de la figure pour la frise chronologique
    fig, ax = plt.subplots(figsize=(10, 3))
    
    # Détermination des bornes de la frise (premier et dernier événement)
    start_date = events[0]['datetime']
    end_date = events[-1]['datetime']
    ax.hlines(1, start_date, end_date, colors='gray', linewidth=2)
    
    # Affichage de chaque événement sur la frise
    for event in events:
        # Choix de la couleur en fonction du type d'événement
        color = 'blue' if event['type'] == 'acte' else 'red'
        ax.plot(event['datetime'], 1, "o", markersize=8, color=color)
        # Annotation de l'événement
        ax.text(event['datetime'], 1.05, event['label'], rotation=45,
                ha='left', va='bottom', fontsize=9)
    
    # Configuration de l'axe des x pour un affichage clair des dates
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
    plt.gcf().autofmt_xdate()
    
    # Masquage de l'axe des y
    ax.get_yaxis().set_visible(False)
    
    plt.title("Frise chronologique des événements")
    plt.tight_layout()
    plt.show()




if __name__ == "__main__":

    # load data
    data_file = "data/toy.json"
    data = load_json(data_file)
    sejour_list = data["sejour"]

    # Craft figure
    for sejour in sejour_list:
        display_timeline(sejour)


    

