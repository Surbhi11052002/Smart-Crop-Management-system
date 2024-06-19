import pickle

def recommend_fertilizer(data):
    model_path = 'models/classifier.pkl'
    model = pickle.load(open(model_path, 'rb'))
    print("type",type(model))
    #return model.predict([[34,67,62,0,1,7,0,30]])
    return model.predict(data)