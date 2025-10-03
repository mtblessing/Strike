import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Create output folder if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), "../outputs")
os.makedirs(output_dir, exist_ok=True)

# Monte Carlo simulation
spread = 5.5
n_sim = 10000
simulated_margins = np.random.normal(spread, 12, n_sim)

# Timestamp for unique filenames
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Save CSV
csv_file = os.path.join(output_dir, f"simulation_{timestamp}.csv")
pd.DataFrame({"Simulated Margins": simulated_margins}).to_csv(csv_file, index=False)

# Save histogram
plt.hist(simulated_margins, bins=40, edgecolor="black")
plt.title("NBA Simulation")
plt.xlabel("Margin")
plt.ylabel("Frequency")
plt.savefig(os.path.join(output_dir, f"simulation_hist_{timestamp}.png"))
plt.close()

print(f"Saved simulation CSV and PNG to {output_dir}")