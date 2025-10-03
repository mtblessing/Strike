# src/strike_model.py
import numpy as np

def spread_to_prob(spread: float) -> float:
    """Convert point spread to win probability using logistic curve."""
    return 1 / (1 + np.exp(-(spread / 6)))

def expected_spread(net_rating_a, net_rating_b, home_court=3, injury_adj=0, h2h_adj=0):
    """Calculate expected spread (Team A - Team B)."""
    return (net_rating_a - net_rating_b) + home_court + injury_adj + h2h_adj

if __name__ == "__main__":
    # Example: Knicks vs 76ers
    net_knicks = 4.5
    net_sixers = 1.5
    home_court = 3
    injury_adj = 0
    h2h_adj = 2

    spread = expected_spread(net_knicks, net_sixers, home_court, injury_adj, h2h_adj)
    prob = spread_to_prob(spread)

    print(f"Expected Spread: {spread:.2f} points")
    print(f"Win Probability Knicks: {prob*100:.1f}%")
    print(f"Win Probability 76ers: {(1-prob)*100:.1f}%")
