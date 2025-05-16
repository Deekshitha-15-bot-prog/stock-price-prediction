import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load CSV instead of Excel
df = pd.read_csv("stock_data.csv")

# Prepare data
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, "stock_price_model.pkl")
print("Model trained and saved as stock_price_model.pkl")
