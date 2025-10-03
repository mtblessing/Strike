# src/strike_data.py

def load_team_stats():
    """Example team stats. Replace with live data later."""
    return {
        "Knicks": {"ORTG": 115.0, "DRTG": 110.5, "Net Rating": 4.5},
        "76ers": {"ORTG": 113.5, "DRTG": 112.0, "Net Rating": 1.5},
    }

if __name__ == "__main__":
    stats = load_team_stats()
    print("Team stats loaded:")
    for team, vals in stats.items():
        print(f"{team}: {vals}")
