import os
import zipfile
import requests
import io

DATA_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")

def download_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    print(f"Downloading data from {DATA_URL}...")
    response = requests.get(DATA_URL)
    response.raise_for_status()
    
    print("Extracting data...")
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall(DATA_DIR)
        
    print(f"Data downloaded and extracted to {DATA_DIR}")

if __name__ == "__main__":
    download_data()
