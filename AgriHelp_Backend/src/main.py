import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS
from twilio.rest import Client
import boto3



from config import ACCESS_KEY_ID, ACCESS_SECRET_KEY, BUCKET_NAME, config
from crop_recommendation.corp_prediction import recommend_crop
from crop_recommendation.weather import weather_fetch
from disease_classifier.classify_disease import predict_image
from farmers_log.search_user_request import search_log
from fertilizier_predict.crop_type_encoder import encode_crop_type
from fertilizier_predict.decode_fertilizer import decode_fertilizer
from fertilizier_predict.fertilizer_report import generate_fertilizer_report
from fertilizier_predict.min_max import min_max
from fertilizier_predict.predict_fertilizer import recommend_fertilizer
from fertilizier_predict.soil_type_encoder import encode_soil_type
from localization.translator import translate_text_to_language
from disease_classifier.disease_info import get_disease_recommendation
from utils import response_payload
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import json
from sklearn.preprocessing import LabelEncoder
from joblib import load
from fastapi import File, UploadFile
label_encoder = load("models/label_encoder.joblib")
labels = ['apple', 'banana', 'blackgram', 'chickpea', 'coconut', 'coffee',
        'cotton', 'grapes', 'jute', 'kidneybeans', 'lentil', 'maize',
        'mango', 'mothbeans', 'mungbean', 'muskmelon', 'orange', 'papaya',
        'pigeonpeas', 'pomegranate', 'rice', 'watermelon']
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def check_form_data():
    try:
        data = request.get_json()
        valid = 1
    except Exception:
        data = "Request body could not be found"
        valid = 0
    if not data:
        valid = 0
        data = "No data provided"
    return data, valid

@app.get("/test")
def test():
    return response_payload(True, "Hello World")

@app.get("/search/{body}")
def search(body: str):
    body = "solution for " + body
    resp = farmers_log(query={"log": body, "lang": "en"})
    response = resp["data"]["organic_result_1"]["response"]
    if response == "":
        response = "Sorry, we could not find any solution for your problem"
    return response_payload(True, {"response": response}, "Working")

@app.post("/farmers-log")
def farmers_log(query=None):
    if query is None:
        data, form_valid = check_form_data()
    else:
        data, form_valid = query, 1
    if form_valid == 0:
        return response_payload(False, msg=data)
    log = data.get("log")
    lang = data.get("lang", "en")
    print('Log is : ', log)
    if not log:
        return response_payload(False, msg="No log provided")
    search_result = search_log(log, lang)
    return response_payload(True, search_result, "Success search")


class UserInput(BaseModel):
    nitrogen: float
    phosphorous: float
    potassium: float 
    ph: float 
    rainfall: float 
    temperature: float 
    humidity: float 
    city: str 
    lang: str = "en"

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        return json.JSONEncoder.default(self, obj)    


@app.post('/crop-recommedation')
async def crop_recommedation(data: UserInput):
    data = data.dict()
    N = data["nitrogen"]
    P = data["phosphorous"]
    K = data["potassium"]
    ph = data["ph"]
    rainfall = data["rainfall"]
    temperature = data["temperature"]
    humidity = data["humidity"]
    city = data["city"]
    lang = data["lang"]

    print(N)
    print(K)

    if city != "":
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = recommend_crop(data)
        output=labels[int(my_prediction)]
        # original_labels = label_encoder.inverse_transform(my_prediction)
        print("pridiction")
        print(output)
        recommendation_result = {
            "prediction": output
        }
    else:
        recommendation_result = "city not found"

    # Convert the recommendation_result to JSON using custom encoder
    recommendation_json = json.dumps(recommendation_result, cls=NumpyEncoder)
    return recommendation_result


class FertilizerInput(BaseModel):
    soil_type: str
    crop_type: str
    moisture: float
    nitrogen: float
    phosphorous: float
    potassium: float
    city: str
    lang: str = "en"
    
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        return json.JSONEncoder.default(self, obj)     

@app.post('/fertilizer-predict')
async def predict_fertilizer(data: FertilizerInput):
    my_prediction=""
    data = data.dict()
    soil_type = data["soil_type"]
    crop_type = data["crop_type"]
    moisture = data["moisture"]
    N = data["nitrogen"]
    P = data["phosphorous"]
    K = data["potassium"]
    city = data["city"]
    lang = data["lang"]
    soil_type = str(soil_type)
    crop_type = str(crop_type)
    N = int(N)
    P = int(P)
    K = int(K)
    
    # soil_type = translate_text_to_language(soil_type, "en", lang)
    # crop_type = translate_text_to_language(crop_type, "en", lang)
    city = translate_text_to_language(city, "en", lang)
    city_info = weather_fetch(city)
    print("city",city_info)
    print("soil",soil_type)
    print("crop",crop_type)
    
    
        
    encoded_soil_type = encode_soil_type(soil_type)
    encoded_crop_type = encode_crop_type(crop_type)
        
    if(encoded_soil_type == None and encoded_crop_type == None):
        return response_payload(False, msg="Invalid soil type or crop type")
        
    if city_info != None:
        temperature, humidity = city_info
        temperature=int(temperature)
        humidity=int(humidity)
        print("temp",temperature)
        print("humid",humidity)
        data = np.array([[ temperature , humidity , moisture,encoded_soil_type,encoded_crop_type, N, P, K]])
        print("data",data)
            
        try:
            # data = min_max(data)
            print('Data ', data)
        except  Exception as e:
            print('Error')
            print(e)
                
        try:
            my_prediction = recommend_fertilizer(data)
            
        except  Exception as e:
            print('Error')
            print(e)
        prediction = decode_fertilizer(my_prediction)
        print("predictions",prediction)
        recommendation_result = {
                "prediction": prediction,
                "info":  generate_fertilizer_report(prediction, lang)
            }
        return response_payload(True,recommendation_result, "Success prediction")
    else:
         return response_payload(False, 'Please try again') 
        
    # except Exception as e:
    #     print(e)
    #     return response_payload(False, msg="Request body is not valid")
# Your existing code for fetching weather, encoding data, and making predictions
    


#@app.post('/disease-predict/{lang}')
#async def disease_prediction(lang: str, file: UploadFile = File(...)):
    if lang is None:
        lang = "en"

    if 'file' not in request.files:
        raise HTTPException(status_code=400, detail='Please select a file')
    file = request.files.get('file')
    if not file:
        raise HTTPException(status_code=400, detail='Please select a file. Make sure there is a file')
    try:
        img = file.read()

        prediction = predict_image(img)
        recommendation_result = {
            "prediction": translate_text_to_language(prediction, lang, "en"),
        }
        return response_payload(True, recommendation_result, "Success prediction")

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Please try again')
    
from fastapi import File, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse

@app.post('/disease-predict/{lang}')
async def disease_prediction(request: Request, lang: str, file: UploadFile = File(...)):
    if lang is None:
        lang = "en"

    try:
        img = await file.read()

        prediction = predict_image(img)
        recommendation_result = {
            "prediction": prediction,
            "info":  get_disease_recommendation(prediction, lang),
        }
        return JSONResponse(content=response_payload(True, recommendation_result, "Success prediction"))

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Please try again')


@app.exception_handler(404)
async def page_not_found(request, exc):
    return "<h1> Page not found ...", 404
    