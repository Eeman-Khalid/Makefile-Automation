import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

os.makedirs("models", exist_ok=True)
df = pd.read_csv("features/titanic_features.csv")

X = df[['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'IsAlone']]
y = df['Survived']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "models/random_forest.pkl")
print("Model trained and saved to models/random_forest.pkl")
