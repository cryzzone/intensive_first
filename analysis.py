import pandas as pd
from pathlib import Path

data_dir = Path("")

df = pd.concat([pd.read_csv(f) for f in data_dir.glob("*.csv")], ignore_index=True)
df.to_csv("result.csv", index=False)