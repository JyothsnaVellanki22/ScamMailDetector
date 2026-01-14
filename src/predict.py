import os
import argparse
import joblib
import string

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/spam_classifier.joblib")

def preprocess_text(text):
    # Must match the preprocessing used in training
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

def predict(message):
    if not os.path.exists(MODEL_PATH):
        print("Model not found. Please run train.py first.")
        return

    print("Loading model...")
    model = joblib.load(MODEL_PATH)
    
    # Preprocess
    clean_message = preprocess_text(message)
    
    # Predict
    prediction = model.predict([clean_message])[0]
    proba = model.predict_proba([clean_message])[0]
    
    print(f"\nMessage: '{message}'")
    print(f"Prediction: {prediction.upper()}")
    print(f"Confidence: {max(proba)*100:.2f}%")
    print("-" * 30)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spam Detector")
    parser.add_argument("message", type=str, help="The email/SMS text to classify")
    args = parser.parse_args()
    
    predict(args.message)
