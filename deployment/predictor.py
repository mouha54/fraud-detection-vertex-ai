import numpy as np
from deployment.model_loader import model, scaler

def predict(input_data: list) -> int:
    """
    input_data: list of numerical features (same order as training)
    returns: prediction (0 or 1)
    """
    data = np.array([input_data])
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)
    return int(prediction[0])
