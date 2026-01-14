import os
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/SMSSpamCollection")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models")

def load_data(path):
    print(f"Loading data from {path}...")
    # SMS Spam Collection is tab-separated
    df = pd.read_csv(path, sep='\t', names=['label', 'message'])
    print(f"Data loaded. Shape: {df.shape}")
    print(f"Class distribution:\n{df['label'].value_counts()}")
    return df

def preprocess_text(text):
    # Simple preprocessing: lowercase and remove punctuation
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

def train_model():
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_PATH)

    df = load_data(DATA_PATH)
    
    # Preprocessing
    print("Preprocessing data...")
    df['clean_message'] = df['message'].apply(preprocess_text)
    
    X = df['clean_message']
    y = df['label']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Pipeline
    print("Training model...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', MultinomialNB()),
    ])
    
    pipeline.fit(X_train, y_train)
    
    # Evaluate
    print("Evaluating model...")
    predictions = pipeline.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))
    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_test, predictions))
    
    # Save
    model_file = os.path.join(MODEL_PATH, "spam_classifier.joblib")
    joblib.dump(pipeline, model_file)
    print(f"Model saved to {model_file}")

if __name__ == "__main__":
    train_model()
