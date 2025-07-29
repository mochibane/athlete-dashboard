import pandas as pd
import numpy as np

# Performances (Onglet 1)
weeks = [f"Semaine {i}" for i in range(1, 11)]
athletes = ["athlète_01", "athlète_02", "athlète_03", "athlète_04"]

np.random.seed(42)  # pour reproductibilité

performance_data = []
for athlete in athletes:
    base_speed = np.random.uniform(4.5, 6.0)
    base_endurance = np.random.uniform(6.0, 8.0)
    base_error = np.random.uniform(2.5, 4.5)

    for i, week in enumerate(weeks):
        performance_data.append({
            "Semaine": week,
            "Athlète": athlete,
            "Vitesse moyenne": round(base_speed + np.random.normal(0, 0.2) + i * 0.05, 2),
            "Endurance": round(base_endurance + np.random.normal(0, 0.2) + i * 0.05, 2),
            "Taux d'erreur": round(max(0.5, base_error - np.random.normal(0, 0.1)), 2)
        })

performance_df = pd.DataFrame(performance_data)


#Player Load & Risques (Onglet 2)
# Risque de blessure : % aléatoire entre 10 et 70
# Générer des données hebdomadaires pour chaque athlète – risque de blessure
player_risk_data = []
for athlete in athletes:
    for week in weeks:
        player_risk_data.append({
            "Athlète": athlete,
            "Semaine": week,
            "Risque de blessure (%)": np.random.randint(10, 80)
        })

player_risk_df = pd.DataFrame(player_risk_data)

# Indicateurs : cohérents et variés
# Générer des données hebdomadaires pour chaque athlète
indicators_data = []
for athlete in athletes:
    for week in weeks:
        indicators_data.append({
            "Athlète": athlete,
            "Semaine": week,
            "Séances/Semaine": np.random.randint(3, 7),
            "Sommeil (h/nuit)": round(np.random.uniform(6.0, 8.5), 1),
            "Séances muscu": np.random.randint(2, 5),
            "Charge 3 sem": np.random.randint(200, 350),
            "Fatigue": np.random.randint(4, 9),
            "Heures de voyage": np.random.randint(1, 10)
        })

indicators_df = pd.DataFrame(indicators_data)

# (Onglet 3) Trajectoire simulée : ligne droite avec 30 points (1 par seconde)
n_points = 30
traj_df = pd.DataFrame({
    "Latitude": [47.5 + i * 0.0015 for i in range(n_points)],
    "Longitude": [-3.1 + i * 0.002 for i in range(n_points)],
    "Temps (s)": list(range(n_points)),
    "Vitesse (nds)": [8 + 0.2*np.sin(i/4) for i in range(n_points)],
    "Cap": [70 for _ in range(n_points)]
})
