from dash import dcc, html, dash_table
from data.data_sources import weeks

player_load_tab = dcc.Tab(label="📊 Player Load & Risques", children=[
    html.Br(),

    html.H4("Risque de blessure - Dernière semaine disponible"),
    dash_table.DataTable(
        id="risk-table",
        columns=[
            {"name": "Athlète", "id": "Athlète"},
            {"name": "Risque de blessure (%)", "id": "Risque de blessure (%)"}
        ],
        style_table={"overflowX": "auto", "width": "50%"},
        style_cell={"textAlign": "center"},
        style_data_conditional=[
            {
                "if": {
                    "filter_query": "{Risque de blessure (%)} >= 0 && {Risque de blessure (%)} < 30",
                    "column_id": "Risque de blessure (%)"
                },
                "backgroundColor": "#D4EDDA",
                "color": "#155724"
            },
            {
                "if": {
                    "filter_query": "{Risque de blessure (%)} >= 30 && {Risque de blessure (%)} < 50",
                    "column_id": "Risque de blessure (%)"
                },
                "backgroundColor": "#FFF3CD",
                "color": "#856404"
            },
            {
                "if": {
                    "filter_query": "{Risque de blessure (%)} >= 50",
                    "column_id": "Risque de blessure (%)"
                },
                "backgroundColor": "#F8D7DA",
                "color": "#721C24"
            }
        ]
    ),

    html.Br(),
    html.Div([
        html.Label("Filtrer par semaine :"),
        dcc.Dropdown(
            id='filter-week',
            options=[{"label": week, "value": week} for week in weeks],
            value=weeks[-1],
            multi=False
        )
    ], style={"width": "40%"}),

    html.Br(),
    html.H4("Indicateurs complémentaires"),
    dash_table.DataTable(
        id="indicator-table",
        columns=[
            {"name": "Date", "id": "Date"},
            {"name": "Athlète", "id": "Athlète"},
            {"name": "Semaine", "id": "Semaine"},
            {"name": "Séances/Semaine (nb)", "id": "Séances/Semaine"},
            {"name": "Sommeil (h/nuit)", "id": "Sommeil (h/nuit)"},
            {"name": "Séances muscu (nb)", "id": "Séances muscu"},
            {"name": "Charge 3 sem (u.a)", "id": "Charge 3 sem"},
            {"name": "Fatigue (score)", "id": "Fatigue"},
            {"name": "Heures de voyage (h)", "id": "Heures de voyage"}
        ],
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "center"}
    )
])