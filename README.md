# 📧 Scam Mail / Spam Detector

[![Angular](https://img.shields.io/badge/Frontend-Angular_17-dd0031?style=flat&logo=angular)](https://angular.io/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/ML-Scikit--Learn-F7931E?style=flat&logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A full-stack machine learning application designed to identify and classify spam messages (SMS/Email) in real-time. Built with a powerful **Naive Bayes** model, served via a high-performance **FastAPI** backend, and visualized through a modern **Angular** frontend with a premium Glassmorphism design.

---

## 🌟 Features

*   **Real-time Analysis**: Instantly classifies messages as **Spam** or **Ham** (Not Spam).
*   **Confidence Scores**: Provides a percentage probability score for every prediction.
*   **Machine Learning Core**: Uses **TF-IDF Vectorization** and **Multinomial Naive Bayes** for high accuracy (~97% on test data).
*   **Modern UI**: A responsive, 2-column layout with a beautiful specialized Gradeient and Glassmorphism effects.
*   **Full Stack**: Demonstrates seamless integration between Python/FastAPI and Angular.

---

## 🛠️ Tech Stack

### **Machine Learning & Backend**
*   **Python 3.13**: Core programming language.
*   **Scikit-learn**: For model training and vectorization logic.
*   **Pandas**: For data preprocessing and manipulation.
*   **Joblib**: For serializing and loading the trained model.
*   **FastAPI**: For creating the REST API endpoint (`/predict`).
*   **Uvicorn**: ASGI server for high-performance deployment.

### **Frontend**
*   **Angular 17+**: Robust frontend framework.
*   **TypeScript**: Type-safe development.
*   **PrimeIcons**: For consistent iconography.
*   **CSS3**: Custom Flexbox layouts and advanced styling (Glassmorphism, Animations).

---

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites
Ensure you have the following installed:
*   **Python 3.10+**
*   **Node.js 18+** & **npm**
*   **Git**

### 1. Clone the Repository
```bash
git clone https://github.com/JyothsnaVellanki22/ScamMailDetector.git
cd ScamMailDetector
```

### 2. Backend Setup (Python)

Create a virtual environment and install dependencies:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate
# Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Download Data & Train Model:**
Before running the server, you need to download the dataset and train the model locally.

```bash
python src/download_data.py
python src/train.py
```
*This will create a `models/spam_classifier.joblib` file.*

### 3. Frontend Setup (Angular)

Open a **new terminal** window and navigate to the frontend directory:

```bash
cd src/frontend

# Install Angular dependencies
npm install
```

---

## ▶️ Running the Application

You need to run the Backend and Frontend in separate terminals.

### Terminal 1: Backend
```bash
# Make sure your virtual environment is active!
source venv/bin/activate

# Start the server
uvicorn src.backend.main:app --reload
```
✅ Server running at: `http://localhost:8000`

### Terminal 2: Frontend
```bash
# Inside src/frontend
npm start
```
✅ App running at: `http://localhost:4200`

---

## 📂 Project Structure

```
├── data/                  # Raw dataset (SMS Spam Collection)
├── models/                # Saved ML models (.joblib)
├── src/
│   ├── backend/           # FastAPI application
│   │   └── main.py
│   ├── frontend/          # Angular application
│   └── train.py           # ML Training script
├── requirements.txt       # Python dependencies
└── vercel.json            # Vercel Deployment Config
```

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
