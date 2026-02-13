import os
import pandas as pd
import joblib

os.makedirs("results", exist_ok=True)
df = pd.read_csv("features/titanic_features.csv")
model = joblib.load("models/random_forest.pkl")

X = df[['Pclass', 'Sex', 'Age', 'Fare', 'FamilySize', 'IsAlone']]
df['Prediction'] = model.predict(X)

df[['PassengerId', 'Prediction']].to_csv("results/predictions.csv", index=False)
print("Predictions saved to results/predictions.csv")
