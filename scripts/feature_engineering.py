import os
import pandas as pd

os.makedirs("features", exist_ok=True)
df = pd.read_csv("data/processed/titanic_processed.csv")

df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

df.to_csv("features/titanic_features.csv", index=False)
print("Features saved to features/titanic_features.csv")
