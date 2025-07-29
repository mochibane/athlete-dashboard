
import dash
from dash import html, dcc, Output, Input
import plotly.express as px
import plotly.graph_objects as go
from data.data_sources import performance_df
from data.data_sources import indicators_df, weeks, player_risk_df
from tabs.performance_tab import performance_tab
from tabs.player_load_tab import player_load_tab
from tabs.live_tracking_tab import live_tracking_tab


app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Interface de Suivi Athlètes"

app.layout = html.Div([
    html.H1("Interface de Visualisation - Suivi des Athlètes", style={"textAlign": "center"}),
    dcc.Tabs([
        performance_tab,
        player_load_tab,
        live_tracking_tab
    ])
])

@app.callback(
    Output("line-vitesse", "figure"),
    Output("line-endurance", "figure"),
    Output("line-erreur", "figure"),
    Output("radar-performance", "figure"),
    Input("athlete-selector", "value")
)
def update_graphs(selected_athletes):
    filtered = performance_df[performance_df["Athlète"].isin(selected_athletes)]

    common_line_style = {
        "template": "plotly_white",
        "height": 250,
        "margin": dict(l=40, r=40, t=40, b=40),
        "legend": dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    }
    fig_vitesse = px.line(
        filtered, x="Semaine", y="Vitesse moyenne", color="Athlète",
        title="🚀 Vitesse Moyenne (km/h)", markers=True
    )
    fig_vitesse.update_traces(mode="lines+markers", line=dict(width=2))
    fig_vitesse.update_layout(**common_line_style)

    fig_endurance = px.line(
        filtered, x="Semaine", y="Endurance", color="Athlète",
        title="💪 Endurance (score / 10)", markers=True
    )
    fig_endurance.update_traces(mode="lines+markers", line=dict(width=2, dash="dot"))
    fig_endurance.update_layout(**common_line_style)

    fig_erreur = px.line(
        filtered, x="Semaine", y="Taux d'erreur", color="Athlète",
        title="⚠️ Taux d'Erreur (%)", markers=True
    )
    fig_erreur.update_traces(mode="lines+markers", line=dict(width=2, dash="dash"))
    fig_erreur.update_layout(**common_line_style)

    # Radar chart
    import plotly.graph_objects as go
    radar_fig = go.Figure()
    for athlete in selected_athletes:
        sub = filtered[filtered["Athlète"] == athlete]
        radar_fig.add_trace(go.Scatterpolar(
            r=[
                sub["Vitesse moyenne"].mean(),
                sub["Endurance"].mean(),
                sub["Taux d'erreur"].mean()
            ],
            theta=["Vitesse", "Endurance", "Taux d'erreur"],
            fill="toself",
            name=athlete
        ))

    radar_fig.update_layout(
        title="📊 Radar – Moyennes de performance",
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        template="plotly_white",
        height=500,
        margin=dict(l=30, r=30, t=50, b=30),
        showlegend=True
    )

    return fig_vitesse, fig_endurance, fig_erreur, radar_fig

@app.callback(
    Output("risk-table", "data"),
    Output("indicator-table", "data"),
    Input("filter-week", "value")
)
def update_tables(selected_week):
    latest_week = max(weeks)
    df_risk_filtered = player_risk_df[
        player_risk_df["Semaine"] == latest_week
    ][["Athlète", "Risque de blessure (%)"]]

    df_indic_filtered = indicators_df[
        indicators_df["Semaine"] == selected_week
    ]

    return df_risk_filtered.to_dict("records"), df_indic_filtered.to_dict("records")

if __name__ == '__main__':
    app.run(debug=True)


