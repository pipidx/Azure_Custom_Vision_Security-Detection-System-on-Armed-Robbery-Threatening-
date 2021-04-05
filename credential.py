from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

def predictor():
    # <Predicition Key>
    project_id = "bf40f005-083f-42b8-ad2c-debcef73af2f"
    prediction_key = "2eaf7993091647e8bab3a3b649789b58"
    ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
    # predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

    iteration_name = "Iteration5"
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    #</Predicition Key>
    
    return predictor, project_id, iteration_name