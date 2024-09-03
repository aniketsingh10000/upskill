# water_usage_prediction.py
import numpy as np
from sklearn.linear_model import LinearRegression

# Example data: [Previous usage, Day of week] -> [Current usage]
X = np.array([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]])
y = np.array([1.5, 2.5, 3.5, 4.5, 5.5])

model = LinearRegression()
model.fit(X, y)

def predict_usage(previous_usage, day_of_week):
    return model.predict([[previous_usage, day_of_week]])[0]

# Example prediction
previous_usage = 5
day_of_week = 5
predicted_usage = predict_usage(previous_usage, day_of_week)
print(f"Predicted Water Usage: {predicted_usage:.2f} L")
