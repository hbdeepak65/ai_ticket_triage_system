import joblib
import os

# Paths (adjust if needed)
BASE_DIR = os.path.dirname(__file__)

# Load models and vectorizers
category_model = joblib.load(os.path.join(BASE_DIR, 'category_classifier.joblib'))
category_vectorizer = joblib.load(os.path.join(BASE_DIR, 'category_vectorizer.joblib'))

presence_model = joblib.load(os.path.join(BASE_DIR, 'presence_classifier.joblib'))
presence_vectorizer = joblib.load(os.path.join(BASE_DIR, 'presence_vectorizer.joblib'))

# Function 1: Predict category or urgency
def predict_category_urgency(text):
    category_input = category_vectorizer.transform([text])
    category_prediction = category_model.predict(category_input)[0]

    urgency_input = presence_vectorizer.transform([text])
    urgency_prediction = presence_model.predict(urgency_input)[0]

    return {
        'category': category_prediction,
        'urgency': urgency_prediction
    }

# Function 2: Simple prediction for testing/demo
def predict_ticket(text):
    vectorized_input = category_vectorizer.transform([text])
    prediction = category_model.predict(vectorized_input)
    return prediction[0]

if __name__ == "__main__":
    test_text = "My server is down and needs immediate attention"
    result = predict_category_urgency(test_text)
    print(result)
