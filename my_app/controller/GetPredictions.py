def GetPredictions(model, inputs):

    prediction = model.predict([inputs])[0]

    result = {
        1: "Hazardous",
        0: "Not Hazardous"
    }

    return result[prediction]