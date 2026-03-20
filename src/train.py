import pandas as pd
import joblib
import os

# Load data
df = pd.read_csv("D:\\Phishingwebsite_detection\\data\\dataset_phishing.csv")

# Convert target
df['status'] = df['status'].map({
    'phishing': 1,
    'legitimate': 0
})

# Drop URL column (not useful)
df = df.drop('url', axis=1)

# Fill missing
df.fillna(0, inplace=True)

# Split
from sklearn.model_selection import train_test_split

X = df.drop('status', axis=1)
y = df['status']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save
os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/phishing_model.pkl")
joblib.dump(X.columns.tolist(), "models/features.pkl")

print("✅ Model trained & saved!")