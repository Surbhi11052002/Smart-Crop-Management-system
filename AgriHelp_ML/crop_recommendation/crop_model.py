import pickle

def crop_classifier():
    crop_recommendation_model_path = 'models/LogisticRegression.pkl'
    crop_recommendation_model = pickle.load(
        open(crop_recommendation_model_path, 'rb'))
    return crop_recommendation_model

print("Model loaded successfully")

