import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("data/matches.csv")

# Select columns
data = df[
    [
        "team1",
        "team2",
        "toss_winner",
        "toss_decision",
        "venue",
        "winner"
    ]
].dropna()

# Encode categorical data
encoders = {}

for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

# Features and target
X = data.drop("winner", axis=1)
y = data["winner"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoders
with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("Model trained successfully!")
