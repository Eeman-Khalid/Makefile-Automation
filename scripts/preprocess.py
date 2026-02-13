import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

os.makedirs("data/processed", exist_ok=True)
df = pd.read_csv("data/raw/titanic.csv")

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna('S', inplace=True)

le_sex = LabelEncoder()
df['Sex'] = le_sex.fit_transform(df['Sex'])

le_emb = LabelEncoder()
df['Embarked'] = le_emb.fit_transform(df['Embarked'])

df.to_csv("data/processed/titanic_processed.csv", index=False)
print("Preprocessed dataset saved to data/processed/titanic_processed.csv")
