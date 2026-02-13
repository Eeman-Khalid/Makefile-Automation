import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

os.makedirs("results", exist_ok=True)
df = pd.read_csv("features/titanic_features.csv")
pred = pd.read_csv("results/predictions.csv")

y_true = df['Survived']
y_pred = pred['Prediction']

metrics = {
    "Accuracy": accuracy_score(y_true, y_pred),
    "Precision": precision_score(y_true, y_pred),
    "Recall": recall_score(y_true, y_pred),
    "F1-score": f1_score(y_true, y_pred)
}

with open("results/metrics.txt", "w") as f:
    for k, v in metrics.items():
        f.write(f"{k}: {v}\n")

print("Evaluation metrics saved to results/metrics.txt")
