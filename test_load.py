import joblib
model = joblib.load('vinodh.pkl')

# Predict one sample
sample = [[5.1, 3.5, 1.4, 0.2]]
print("Prediction:", model.predict(sample))

