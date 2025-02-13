import plotly.express as px
import pandas as pd
import json
import pprint



def get_data(json_file):
    """ """

    # load data
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # extract patient ipp
    ipp = data['patient']['ipp']

    parsed = {"Date":[], "Événement":[],"Détails":[]}
    for sejour in data['sejour']:

        # Screen actes
        for acte in sejour['actes']:
            parsed['Date'].append(acte['timestamp'])
            parsed["Événement"].append(acte['ccam'])
            parsed['Détails'].append("Acte CCAM")
            
        # Screen diag
        for acte in sejour['diagnostic']:
            parsed['Date'].append(acte['timestamp'])
            parsed["Événement"].append(acte['cim10'])
            parsed['Détails'].append("Code CIM10")

    # craft dataframe
    df = pd.DataFrame(parsed)
    df["Date"] = pd.to_datetime(df["Date"])

    # return crafted dataframe
    return df



def plot_timeline(df, title:str):
    """ """

    # Création de la frise chronologique avec Plotly
    fig = px.scatter(df, x="Date", y=[1] * len(df), text="Événement",
                     hover_data={"Date": True, "Détails": True, "Événement": False},
                     labels={"Date": "Date", "Détails": "Description"},
                     title=title)

    # Personnalisation de l'affichage
    fig.update_traces(marker=dict(size=15, color="#2d7e8c"), textposition="top center")
    fig.update_layout(
        height=300,
        plot_bgcolor="#edd882",
        xaxis_title="Temps",
        yaxis=dict(visible=False),  # Cache l'axe des Y
        xaxis=dict(showgrid=True),  # Supprime la grille
        hovermode="closest"
    )

    # Affichage
    fig.show()


if __name__ == "__main__":
    
    # get data
    df = get_data("data/toy.json")

    # plot timeline
    plot_timeline(df, "ZBleh")
