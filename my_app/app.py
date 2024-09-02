from fastapi import FastAPI
from controller.LoadModel import LoadModel
from controller.GetPredictions import GetPredictions

model_path = "model\dangerous_asteroids_model.pkl"
model = LoadModel(model_path)

app = FastAPI()


@app.get("/")
def get_predictions(absolute_magnitude: float, estimated_diameter_min: float, 
                    estimated_diameter_max: float, relative_velocity: float, 
                    miss_distance: float):
    
    inputs = [absolute_magnitude, estimated_diameter_min, estimated_diameter_max, relative_velocity, miss_distance]
    prediction = GetPredictions(model=model, inputs=inputs)
    if prediction == "Hazardous":
        return "Warning: This asteroid is potentially hazardous!"
    else:
        return "This asteroid is not hazardous."
