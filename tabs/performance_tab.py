from dash import dcc, html
from data.data_sources import performance_df

athletes = performance_df["Athlète"].unique()

performance_tab = dcc.Tab(label="📈 Performance des Athlètes", children=[
    html.Br(),

    html.Div([
        html.Label("🎯 Sélectionner les athlètes :"),
        dcc.Dropdown(
            id="athlete-selector",
            options=[{"label": a, "value": a} for a in athletes],
            value=["athlète_01"],
            multi=True,
            style={"width": "60%"}
        )
    ], style={"padding": "0 30px"}),

    html.Div([
        # 📊 Colonne gauche : Radar (30%)
        html.Div([
            dcc.Graph(id="radar-performance", config={"displayModeBar": False})
        ], style={
            "width": "40%",
            "padding": "10px",
            "minWidth": "300px"
        }),

        # 📈 Colonne droite : 3 lignes (70%)
        html.Div([
            dcc.Graph(id="line-vitesse", config={"displayModeBar": False}),
            dcc.Graph(id="line-endurance", config={"displayModeBar": False}),
            dcc.Graph(id="line-erreur", config={"displayModeBar": False})
        ], style={
            "width": "60%",
            "padding": "10px",
            "display": "flex",
            "flexDirection": "column",
            "gap": "20px"
        })

    ], style={
        "display": "flex",
        "flexWrap": "nowrap",
        "justifyContent": "space-between",
        "padding": "20px",
        "gap": "10px"
    })
])
