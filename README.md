## 🩺 Prediction of Disease Outbreaks
A machine learning-based Disease Prediction System developed using Python and Streamlit. The application integrates multiple trained machine learning models into a single interactive web interface for predicting different diseases based on patient-related input parameters.
Disclaimer: This project is developed for educational and academic purposes only. It is not intended to provide medical diagnosis, treatment, or professional medical advice.

## 📌 Project Overview
Early identification of potential diseases can help in understanding health-related risk patterns and supporting further medical evaluation.
This project aims to demonstrate how Machine Learning, Data Preprocessing, Model Training, and Streamlit can be integrated into a single application for disease prediction.
The system currently supports four disease prediction modules:
- ❤️ Heart Disease Prediction
- 🦋 Thyroid Disease Prediction
- 🫁 Lung Cancer Prediction
- 🧠 Parkinson's Disease Prediction
Users can select a disease from the Streamlit interface, provide the required input parameters, and receive a prediction from the corresponding trained machine learning model.

## 🎯 Objectives
The main objectives of this project are:
- To apply machine learning techniques to healthcare-related datasets.
- To perform data preprocessing and exploratory analysis.
- To train and evaluate multiple classification algorithms.
- To select suitable models based on evaluation metrics.
- To save trained models for later use.
- To integrate multiple ML models into a single Streamlit application.
- To create a simple and interactive prediction interface.
- To demonstrate an end-to-end machine learning workflow.

## 🏗️ System Architecture

                ┌─────────────────────────┐
                │     Patient Input       │
                └────────────┬────────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │    Streamlit Web App    │
                │        (app.py)         │
                └────────────┬────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       Heart Disease      Thyroid       Lung Cancer
          Model            Model           Model
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                    Parkinson's Model
                             │
                             ▼
                  Prediction / Probability

## 🧠 Machine Learning Models
## ❤️ _Heart Disease_

The Heart Disease module uses patient health-related parameters such as:
- Age
- Sex
- Chest pain type
- Resting blood pressure
- Cholesterol
- Fasting blood sugar
- Resting ECG
- Maximum heart rate
- Exercise-induced angina
- ST depression
- Slope
- Number of major vessels
- Thalassemia

The trained model is stored as:

## _models/Heart_Diesease.sav_

## 🦋 Thyroid Disease
The Thyroid Disease module uses selected clinical parameters including:
- Age
- Sex
- Thyroxine status
- TSH
- T3 measurement
- T3
- TT4
The final model uses a preprocessing pipeline containing imputation, scaling, and Logistic Regression.

The trained model is stored as:

## _models/Thyroid_model.sav_

## 🫁 Lung Cancer
The Lung Cancer module uses patient demographic, risk-factor, and symptom-related parameters such as:
- Gender
- Age
- Smoking
- Yellow fingers
- Anxiety
- Peer pressure
- Chronic disease
- Fatigue
- Allergy
- Wheezing
- Alcohol consumption
- Coughing
- Shortness of breath
- Swallowing difficulty
- Chest pain
- 
Multiple models were evaluated during development, including Logistic Regression and Random Forest.

Random Forest was selected as the final model based on the evaluation results obtained during development.

The trained model is stored as:

## _models/lungs_disease_model.sav_

## 🧠 Parkinson's Disease

The Parkinson's Disease module uses 22 voice-analysis features, including:
- Average vocal frequency
- Maximum vocal frequency
- Minimum vocal frequency
- Jitter-related measurements
- Shimmer-related measurements
- Noise-to-Harmonics Ratio
- Harmonics-to-Noise Ratio
- RPDE
- DFA
- Spread features
- D2
- PPE
Several classification algorithms were compared:

--  Model	Test Accuracy

-- Logistic Regression	76.92%

--  SVM Linear	82.05%

-- SVM RBF	79.49%

-- Random Forest	94.87%


Based on the selected test split, Random Forest achieved the best performance and was selected as the final Parkinson's model.

The trained model is stored as:
## _models/Parkinsons_model.sav_

The reported accuracy is based on the project's test split and should not be interpreted as clinical or real-world diagnostic accuracy.

## 📊 Model Evaluation
The project evaluates classification models using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report
Model selection is based on comparative performance rather than assuming a single algorithm is best for every disease.

🛠️ Technologies Used
Programming Language
- Python
Machine Learning
- Scikit-learn
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- Classification metrics
Data Processing
- Pandas
- NumPy
Visualization / Analysis
- Matplotlib
- Seaborn
- Jupyter Notebook
Web Application
- Streamlit
Development Environment
- PyCharm
- Jupyter Notebook
Model Serialization
- Pickle

## 📁 Project Structure

```text
Prediction-of-Disease-Outbreaks/
│
├── data/
│   ├── heart_disease_data.csv
│   ├── hypothyroid.csv
│   ├── parkinson_data.csv
│   └── survey lung cancer.csv
│
├── models/
│   ├── Heart_Diesease.sav
│   ├── lungs_disease_model.sav
│   ├── Parkinsons_model.sav
│   └── Thyroid_model.sav
│
├── notebooks/
│   ├── Heart Disease.ipynb
│   ├── Lung Cancer.ipynb
│   ├── Parkinson's Disease.ipynb
│   └── Thyroid_Predict.ipynb
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup
**1. Clone the Repository**

**_git clone_** 
 - https://github.com/YOUR-USERNAME/Prediction-of-Disease-Outbreaks.git

Move into the project directory:

- cd Prediction-of-Disease-Outbreaks

**_2. Create a Virtual Environment_**

- python -m venv .venv

**_Windows_**

- .venv\Scripts\activate

**_3. Install Dependencies_**

- pip install -r requirements.txt

**_4. Run the Streamlit Application_**

- python -m streamlit run app.py

**_The application will open in your browser._**

Usually:

- http://localhost:8501

## 🖥️ Application Features

The Streamlit application provides:
- Interactive disease selection
- Disease-specific input forms
- Pre-trained machine learning models
- Prediction results
- Model probability outputs where available
- User-friendly parameter descriptions
- Educational disclaimer
- Multiple disease models in a single application

## 🔄 Machine Learning Workflow

The general workflow followed in this project is:

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Model Evaluation
   ↓
Final Model Selection
   ↓
Model Serialization
   ↓
Streamlit Integration
   ↓
Disease Prediction
```

## 📚 Project Notebooks

Each disease has a dedicated Jupyter Notebook containing the corresponding data analysis and machine learning workflow.

-- Heart Disease.ipynb

-- Lung Cancer.ipynb

-- Parkinson's Disease.ipynb

-- Thyroid_Predict.ipynb

These notebooks are included to demonstrate the development and training process behind the models used by the application.

## 🔐 Data & Privacy

The application should only be used with appropriate datasets and test information.
Do not enter or upload personally identifiable or confidential medical information into the application.
No passwords, API keys, credentials, or other private secrets should be committed to the repository.

## ⚠️ Disclaimer

This project is intended strictly for educational, academic, and demonstration purposes.
The predictions generated by the machine learning models:
- Are not medical diagnoses.
- Should not be used for treatment decisions.
- Should not replace consultation with qualified healthcare professionals.
- May produce incorrect predictions.
- Are dependent on the datasets and models used during development.

For any real medical concern, consult a qualified healthcare professional.

## 🚀 Future Improvements

Possible future improvements include:
- Improving model validation using cross-validation.
- Hyperparameter tuning.
- Feature importance visualization.
- Better model explainability using SHAP or similar techniques.
- Improving the Streamlit UI/UX.
- Adding interactive charts and visualizations.
- Adding additional disease prediction models.
- Developing automated voice-feature extraction for Parkinson's prediction.
- Deploying the application to a cloud platform.
- Adding authentication and secure data handling for production use.

## 👨‍💻 Author

## _Swarnavo Daw_

**_BCA | Data Analytics & Machine Learning Enthusiast_**

**_Areas of Interest:_**

- Data Analytics
- Machine Learning
- Python
- SQL
- Power BI
- Data Visualization
- Artificial Intelligence

**_⭐ If you find this project useful_**

If this project helped you understand machine learning or multi-model Streamlit applications, consider giving the repository a ⭐ on GitHub.

