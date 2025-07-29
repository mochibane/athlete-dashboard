from dash import dcc, html
import plotly.graph_objects as go
from data.data_sources import traj_df, n_points



# Placeholder météo dynamiques via API (à connecter via callback réel ultérieurement)
weather_info_box = html.Div([
    html.H6("Conditions météo actuelles", style={"marginBottom": "0.5em"}),
    html.Ul([
        html.Li("🌡️ Température : 18°C"),
        html.Li("💧 Hygrométrie : 75%"),
        html.Li("🌬️ Vitesse du vent : 14 km/h"),
        html.Li("🧭 Cap : 70°"),
        html.Li("🌊 État de la mer : Modérée")
    ], style={"listStyle": "none", "paddingLeft": "1em"})
], style={
    "position": "absolute",
    "top": "10px",
    "right": "20px",
    "background": "rgba(255,255,255,0.9)",
    "padding": "10px",
    "borderRadius": "10px",
    "boxShadow": "0px 0px 10px rgba(0,0,0,0.1)"
})

# Animation de la trajectoire (30 secondes, 1 frame/sec)
frames = [
    go.Frame(
        data=[
            go.Scattermapbox(
                lat=traj_df.Latitude[:k+1],
                lon=traj_df.Longitude[:k+1],
                mode="lines",
                line=dict(width=3, color="royalblue"),
                name="Trajectoire"
            ),
            go.Scattermapbox(
                lat=[traj_df.Latitude[k]],
                lon=[traj_df.Longitude[k]],
                mode="markers",
                marker=dict(
                    size=300,
                    symbol="⛵",  # Remplace par un symbole bateau stylisé
                    color="navy"
                ),
                name="Bateau à voile"
            )
        ],
        name=str(k)
    ) for k in range(n_points)
]

live_tracking_tab = dcc.Tab(label="🌍 Suivi en direct - Voile", children=[
    html.Div([
        html.H3("🧭 Suivi de la trajectoire - Athlète 1", style={"textAlign": "center", "marginBottom": "10px"}),
        dcc.Graph(
            id="boat-track",
            figure=go.Figure(
                data=[
                    go.Scattermapbox(
                        lat=[traj_df.Latitude[0]],
                        lon=[traj_df.Longitude[0]],
                        mode="markers+lines",
                        marker=dict(size=300, symbol="⛵", color="navy"),
                        line=dict(width=3, color="royalblue"),
                        name="Trajectoire initiale"
                    )
                ],
                layout=go.Layout(
                    mapbox=dict(
                        style="open-street-map",
                        center=dict(lat=47.505, lon=-3.085),
                        zoom=11
                    ),
                    updatemenus=[dict(
                        type="buttons",
                        showactive=False,
                        buttons=[dict(label="▶️ Lancer", method="animate", args=[[str(k) for k in range(n_points)], {"frame": {"duration": 1000}, "fromcurrent": True}])]
                    )],
                    height=600,
                    margin={"r":0,"t":0,"l":0,"b":0},
                    showlegend=False
                ),
                frames=frames
            )
        ),
        weather_info_box
    ], style={"position": "relative"})
])