import pickle
import pandas as pd
import streamlit as st


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="centered"
)


# ==========================================
# Load Trained Models
# ==========================================

with open("models/Heart_Diesease.sav", "rb") as file:
    heart_model = pickle.load(file)

with open("models/Thyroid_model.sav", "rb") as file:
    thyroid_model = pickle.load(file)

with open("models/lungs_disease_model.sav", "rb") as file:
    lung_model = pickle.load(file)

with open("models/Parkinsons_model.sav", "rb") as file:
    parkinson_model = pickle.load(file)

# ==========================================
# Main Title
# ==========================================

st.title("🩺 Disease Prediction System")

st.write(
    "Select a disease and enter the patient's information "
    "to get a model prediction."
)

# st.info(
#     "This application is for educational/project purposes and "
#     "does not provide a medical diagnosis."
# )

# ==========================================
# Disease Selection
# ==========================================

disease = st.selectbox(
    "Select Disease",
    [
        "Heart Disease",
        "Thyroid Disease",
        "Lung Cancer",
        "Parkinson's Disease"
    ]
)


if disease == "Heart Disease":

    st.header("❤️ Heart Disease Prediction")

    st.write("Enter the patient's information below.")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=57,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        [0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male"
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [1, 2, 3, 4]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=50,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Serum Cholesterol (mg/dl)",
        min_value=100,
        max_value=600,
        value=200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dl",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    restecg = st.selectbox(
        "Resting ECG Result",
        [0, 1, 2]
    )

    thalach = st.number_input(
        "Maximum Heart Rate Achieved",
        min_value=60,
        max_value=220,
        value=150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    oldpeak = st.number_input(
        "ST Depression",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.1
    )

    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        [1, 2, 3]
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4]
    )

    thal = st.selectbox(
        "Thalassemia",
        [0, 1, 2, 3]
    )
    if st.button("🔍 Predict Heart Disease", key="predict_heart"):

        input_data = pd.DataFrame([{
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }])

        prediction = heart_model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ This Person is likely to have Heart Disease.")
        else:
            st.success("✅ This Person isn't likely to have Heart Disease.")

# ==========================================================
# THYROID DISEASE
# ==========================================================

elif disease == "Thyroid Disease":

    st.header("🦋 Thyroid Disease Prediction")

    st.write("Enter the patient's information below.")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=40,
        step=1
    )

    sex = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

    on_thyroxine = st.selectbox(
        "On Thyroxine?",
        ["No", "Yes"]
    )

    TSH = st.number_input(
        "TSH",
        min_value=0.0,
        value=1.0,
        step=0.01,
        format="%.3f"
    )

    T3_measured = st.selectbox(
        "T3 Measured?",
        ["No", "Yes"]
    )

    T3 = st.number_input(
        "T3",
        min_value=0.0,
        value=2.0,
        step=0.01,
        format="%.3f"
    )

    TT4 = st.number_input(
        "TT4",
        min_value=0.0,
        value=100.0,
        step=0.1,
        format="%.3f"
    )

    sex_value = 1 if sex == "Female" else 0
    on_thyroxine_value = 1 if on_thyroxine == "Yes" else 0
    T3_measured_value = 1 if T3_measured == "Yes" else 0

    if st.button("🔍 Predict Thyroid Disease", key="predict_thyroid"):

        input_data = pd.DataFrame([{
            "age": age,
            "sex": sex_value,
            "on thyroxine": on_thyroxine_value,
            "TSH": TSH,
            "T3 measured": T3_measured_value,
            "T3": T3,
            "TT4": TT4
        }])

        prediction = thyroid_model.predict(input_data)

        if prediction[0] == 0:
            st.success("Prediction: This Person isn't likely to have Thyroid")
        else:
            st.warning("Prediction: This Person is likely to have Thyroid")

# ==========================================================
# LUNG CANCER
# ==========================================================

elif disease == "Lung Cancer":

    st.header("🫁 Lung Cancer Prediction")

    st.write(
        "Enter the patient's information below. "
        "The model uses the same feature encoding as the training dataset."
    )

    # -----------------------------------
    # Patient Information
    # -----------------------------------

    gender = st.selectbox(
        "Gender",
        [0, 1],
        format_func=lambda x: "Female" if x == 0 else "Male"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=60,
        step=1
    )

    # -----------------------------------
    # Risk Factors & Symptoms
    # -----------------------------------

    st.subheader("Risk Factors & Symptoms")

    smoking = st.selectbox(
        "Smoking",
        [1, 2]
    )

    yellow_fingers = st.selectbox(
        "Yellow Fingers",
        [1, 2]
    )

    anxiety = st.selectbox(
        "Anxiety",
        [1, 2]
    )

    peer_pressure = st.selectbox(
        "Peer Pressure",
        [1, 2]
    )

    chronic_disease = st.selectbox(
        "Chronic Disease",
        [1, 2]
    )

    fatigue = st.selectbox(
        "Fatigue",
        [1, 2]
    )

    allergy = st.selectbox(
        "Allergy",
        [1, 2]
    )

    wheezing = st.selectbox(
        "Wheezing",
        [1, 2]
    )

    alcohol_consuming = st.selectbox(
        "Alcohol Consuming",
        [1, 2]
    )

    coughing = st.selectbox(
        "Coughing",
        [1, 2]
    )

    shortness_of_breath = st.selectbox(
        "Shortness of Breath",
        [1, 2]
    )

    swallowing_difficulty = st.selectbox(
        "Swallowing Difficulty",
        [1, 2]
    )

    chest_pain = st.selectbox(
        "Chest Pain",
        [1, 2]
    )

    # -----------------------------------
    # Lung Cancer Prediction
    # -----------------------------------

    if st.button("🔍 Predict Lung Cancer", key="predict_lung"):

        input_data = pd.DataFrame([{
            "GENDER": gender,
            "AGE": age,
            "SMOKING": smoking,
            "YELLOW_FINGERS": yellow_fingers,
            "ANXIETY": anxiety,
            "PEER_PRESSURE": peer_pressure,
            "CHRONIC DISEASE": chronic_disease,
            "FATIGUE": fatigue,
            "ALLERGY": allergy,
            "WHEEZING": wheezing,
            "ALCOHOL CONSUMING": alcohol_consuming,
            "COUGHING": coughing,
            "SHORTNESS OF BREATH": shortness_of_breath,
            "SWALLOWING DIFFICULTY": swallowing_difficulty,
            "CHEST PAIN": chest_pain
        }])

        prediction = lung_model.predict(input_data)
        probability = lung_model.predict_proba(input_data)

        if prediction[0] == 1:

            st.error(
                "⚠️ The Person is likely to have lung cancer."
            )

        else:

            st.success(
                "✅ The Person isn't likely to have lung cancer."
            )

        st.write(
            f"Probability of YES: "
            f"{probability[0][1] * 100:.2f}%"
        )

        st.write(
            f"Probability of NO: "
            f"{probability[0][0] * 100:.2f}%"
        )

# ==========================================================
# PARKINSON'S DISEASE
# ==========================================================

elif disease == "Parkinson's Disease":

    st.header("🧠 Parkinson's Disease Prediction")

    # st.write(
    #     "Enter the patient's voice measurement information below. "
    #     "The model uses the same 22 features used during training."
    # )

    # -----------------------------------
    # Patient Voice Measurements
    # -----------------------------------

    st.subheader("Voice Measurements")

    mdvp_fo = st.number_input(
        "Average Vocal Frequency (Hz)",
        min_value=88.333,
        max_value=260.105,
        value=119.992,
        step=0.001,
        format="%.3f",
        help="Average fundamental frequency of the voice. "
             "Dataset range: 88.333–260.105 Hz."
    )

    mdvp_fhi = st.number_input(
        "Maximum Vocal Frequency (Hz)",
        min_value=102.145,
        max_value=592.030,
        value=157.302,
        step=0.001,
        format="%.3f",
        help="Highest fundamental frequency detected in the voice. "
             "Dataset range: 102.145–592.030 Hz."
    )

    mdvp_flo = st.number_input(
        "Minimum Vocal Frequency (Hz)",
        min_value=65.476,
        max_value=239.170,
        value=74.997,
        step=0.001,
        format="%.3f",
        help="Lowest fundamental frequency detected in the voice. "
             "Dataset range: 65.476–239.170 Hz."
    )
    # -----------------------------------
    # Jitter Parameters
    # -----------------------------------
    st.subheader("📈 Frequency Variation (Jitter)")

    mdvp_jitter = st.number_input(
        "Frequency Variation / Jitter (%)",
        min_value=0.001680,
        max_value=0.033160,
        value=0.007840,
        step=0.000001,
        format="%.6f",
        help="Measures small variations in the fundamental frequency of the voice. "
             "Dataset range: 0.001680–0.033160."
    )

    mdvp_jitter_abs = st.number_input(
        "Absolute Jitter",
        min_value=0.000007,
        max_value=0.000260,
        value=0.000070,
        step=0.000001,
        format="%.6f",
        help="Absolute measure of variation between consecutive voice periods. "
             "Dataset range: 0.000007–0.000260."
    )

    mdvp_rap = st.number_input(
        "Relative Average Perturbation (RAP)",
        min_value=0.000680,
        max_value=0.021440,
        value=0.003700,
        step=0.000001,
        format="%.6f",
        help="Measures short-term variation in vocal period length. "
             "Dataset range: 0.000680–0.021440."
    )

    mdvp_ppq = st.number_input(
        "Pitch Period Perturbation (PPQ)",
        min_value=0.000920,
        max_value=0.019580,
        value=0.005540,
        step=0.000001,
        format="%.6f",
        help="Measures variation in vocal pitch periods. "
             "Dataset range: 0.000920–0.019580."
    )

    jitter_ddp = st.number_input(
        "Jitter Difference of Differences (DDP)",
        min_value=0.002040,
        max_value=0.064330,
        value=0.011090,
        step=0.000001,
        format="%.6f",
        help="A measure derived from RAP that represents jitter variation. "
             "Dataset range: 0.002040–0.064330."
    )

    # -----------------------------------
    # Shimmer Parameters
    # -----------------------------------
    st.subheader("🔊 Voice Amplitude Variation (Shimmer)")

    mdvp_shimmer = st.number_input(
        "Amplitude Variation / Shimmer",
        min_value=0.009540,
        max_value=0.119080,
        value=0.043740,
        step=0.000001,
        format="%.6f",
        help="Measures variation in the amplitude of consecutive voice signals. "
             "Dataset range: 0.009540–0.119080."
    )

    mdvp_shimmer_db = st.number_input(
        "Shimmer (dB)",
        min_value=0.085,
        max_value=1.302,
        value=0.426,
        step=0.001,
        format="%.3f",
        help="Shimmer expressed in decibels. "
             "Dataset range: 0.085–1.302 dB."
    )

    shimmer_apq3 = st.number_input(
        "Amplitude Perturbation (APQ3)",
        min_value=0.004550,
        max_value=0.056470,
        value=0.021820,
        step=0.000001,
        format="%.6f",
        help="Three-period amplitude perturbation measure. "
             "Dataset range: 0.004550–0.056470."
    )

    shimmer_apq5 = st.number_input(
        "Amplitude Perturbation (APQ5)",
        min_value=0.005700,
        max_value=0.079400,
        value=0.031300,
        step=0.000001,
        format="%.6f",
        help="Five-period amplitude perturbation measure. "
             "Dataset range: 0.005700–0.079400."
    )

    mdvp_apq = st.number_input(
        "Amplitude Perturbation Quotient (APQ)",
        min_value=0.007190,
        max_value=0.137780,
        value=0.029710,
        step=0.000001,
        format="%.6f",
        help="Measures variation in the amplitude of the voice signal. "
             "Dataset range: 0.007190–0.137780."
    )

    shimmer_dda = st.number_input(
        "Shimmer Difference of Differences (DDA)",
        min_value=0.013640,
        max_value=0.169420,
        value=0.065450,
        step=0.000001,
        format="%.6f",
        help="A derived measure of amplitude variation. "
             "Dataset range: 0.013640–0.169420."
    )

    # -----------------------------------
    # Noise & Harmonics
    # -----------------------------------

    st.subheader("🎚️ Noise & Harmonic Characteristics")

    nhr = st.number_input(
        "Noise-to-Harmonics Ratio (NHR)",
        min_value=0.000650,
        max_value=0.314820,
        value=0.022110,
        step=0.000001,
        format="%.6f",
        help="Represents the amount of noise relative to harmonic components "
             "in the voice. Dataset range: 0.000650–0.314820."
    )

    hnr = st.number_input(
        "Harmonics-to-Noise Ratio (HNR)",
        min_value=8.441,
        max_value=33.047,
        value=21.033,
        step=0.001,
        format="%.3f",
        help="Represents the strength of harmonic components relative to noise. "
             "Dataset range: 8.441–33.047."
    )

    # -----------------------------------
    # Nonlinear Voice Features
    # -----------------------------------

    st.subheader("🧬 Nonlinear Voice Features")

    rpde = st.number_input(
        "Recurrence Period Density Entropy (RPDE)",
        min_value=0.256570,
        max_value=0.685151,
        value=0.414783,
        step=0.000001,
        format="%.6f",
        help="A nonlinear measure describing the complexity of vocal signal "
             "periodicity. Dataset range: 0.256570–0.685151."
    )

    dfa = st.number_input(
        "Detrended Fluctuation Analysis (DFA)",
        min_value=0.574282,
        max_value=0.825288,
        value=0.815285,
        step=0.000001,
        format="%.6f",
        help="Measures long-range patterns and fluctuations in the voice signal. "
             "Dataset range: 0.574282–0.825288."
    )

    spread1 = st.number_input(
        "Frequency Spread 1",
        min_value=-7.964984,
        max_value=-2.434031,
        value=-4.813031,
        step=0.000001,
        format="%.6f",
        help="A nonlinear frequency-distribution feature derived from the voice "
             "signal. Dataset range: -7.964984–-2.434031."
    )

    spread2 = st.number_input(
        "Frequency Spread 2",
        min_value=0.006274,
        max_value=0.450493,
        value=0.266482,
        step=0.000001,
        format="%.6f",
        help="A second measure describing the spread of voice-frequency "
             "characteristics. Dataset range: 0.006274–0.450493."
    )

    d2 = st.number_input(
        "Correlation Dimension (D2)",
        min_value=1.423287,
        max_value=3.671155,
        value=2.301442,
        step=0.000001,
        format="%.6f",
        help="A nonlinear measure describing the complexity of the voice signal. "
             "Dataset range: 1.423287–3.671155."
    )

    ppe = st.number_input(
        "Pitch Period Entropy (PPE)",
        min_value=0.044539,
        max_value=0.527367,
        value=0.284654,
        step=0.000001,
        format="%.6f",
        help="Measures the variation/entropy of pitch periods in the voice. "
             "Dataset range: 0.044539–0.527367."
    )

    # -----------------------------------
    # Parkinson's Prediction
    # -----------------------------------

    if st.button(
        "🔍 Predict Parkinson's Disease",
        key="predict_parkinson"
    ):

        input_data = pd.DataFrame([{
            "MDVP:Fo(Hz)": mdvp_fo,
            "MDVP:Fhi(Hz)": mdvp_fhi,
            "MDVP:Flo(Hz)": mdvp_flo,
            "MDVP:Jitter(%)": mdvp_jitter,
            "MDVP:Jitter(Abs)": mdvp_jitter_abs,
            "MDVP:RAP": mdvp_rap,
            "MDVP:PPQ": mdvp_ppq,
            "Jitter:DDP": jitter_ddp,
            "MDVP:Shimmer": mdvp_shimmer,
            "MDVP:Shimmer(dB)": mdvp_shimmer_db,
            "Shimmer:APQ3": shimmer_apq3,
            "Shimmer:APQ5": shimmer_apq5,
            "MDVP:APQ": mdvp_apq,
            "Shimmer:DDA": shimmer_dda,
            "NHR": nhr,
            "HNR": hnr,
            "RPDE": rpde,
            "DFA": dfa,
            "spread1": spread1,
            "spread2": spread2,
            "D2": d2,
            "PPE": ppe
        }])

        prediction = parkinson_model.predict(input_data)
        probability = parkinson_model.predict_proba(input_data)

        if prediction[0] == 1:

            st.error(
                "⚠️ The Person may have Parkinson's disease."
            )

        else:

            st.success(
                "✅ The Person is healthy."
            )

        st.write(
            f"Probability of Parkinson's: "
            f"{probability[0][1] * 100:.2f}%"
        )

        st.write(
            f"Probability of Healthy: "
            f"{probability[0][0] * 100:.2f}%"
        )