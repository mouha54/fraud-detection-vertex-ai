from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from deployment.predictor import predict

app = FastAPI()

class FraudRequest(BaseModel):
    features: list[float]  # adapt length based on your dataset

@app.post("/predict")
def predict_fraud(request: FraudRequest):
    try:
        if len(request.features) != 30:  # Assuming your model expects 30 features
            raise ValueError(f"Expected 30 features, got {len(request.features)}")

        result = predict(request.features)
        return {"prediction": result}
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
