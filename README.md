
# Stock Price Prediction - Machine Learning Mini Project

## Folder Structure

app.py                   # Streamlit app
train_model.py           # Script to train your model
stock_price_model.pkl    # Trained ML model (may need to retrain locally)
stock_data.csv           # You must add your Excel dataset file here
README.txt               # Instructions

## How to Run

1. Install requirements:
   pip install streamlit scikit-learn joblib pandas openpyxl

2. Create a virtual environment. For that run :
       python -m venv .venv  
   To activate the environment,
       .venv\Scripts\activate     

3. Run the app:
   streamlit run app.py

4. Use the UI to input stock data and get the predicted closing price.

## Notes
- This version uses RandomForestRegressor
- Works best with historical stock market data

**Output**

![Screenshot 2025-05-16 213456](https://github.com/user-attachments/assets/c4f6adce-b9f1-4f8e-985b-3bbaa9b0d413)

