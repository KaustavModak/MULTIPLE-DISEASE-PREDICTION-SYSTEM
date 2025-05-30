import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model=pickle.load(open('diabetes_model.pkl','rb'))
heart_model=pickle.load(open('heart_model.pkl','rb'))
parkinsons_model=pickle.load(open('parkinsons_model.pkl','rb'))
scaler_diabetes=pickle.load(open('standardized_diabetes.pkl','rb'))
scaler_heart=pickle.load(open('standardized_heart.pkl','rb'))
scaler_parkinsons=pickle.load(open('standardized_parkinsons.pkl','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu(menu_title="Multiple Disease Detection System",
                           options=["Home","Diabetes Prediction","Heart Disease Prediction","Parkinson's Disease Prediction"],
                           icons=['house','activity','heart-fill','person'],default_index=0) # default_index=0 means Diabetes Prediction gets displayed primarily before selecting any option

# for home page
if(selected=="Home"):
    st.title("Your AI-Powered Health Screening Assistant")
    st.image("20250526_1738_Disease Prediction System_remix_01jw67tpgxfbt9gy7v8b6b10ag.png")
    '''
    ---
    ### Press the navigation bar to predict diabetes, heart disease, or Parkinson's disease from simple inputs using machine learning models.
    '''

# Diabetes Prediction Page
if(selected=="Diabetes Prediction"):
    st.title("Diabetes Prediction") # page title

    # getting the input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.number_input("Number of Pregnancies",min_value=0,step=1,format="%d") # min value starts from 0 and the field is in the form of int

    with col2:
        Glucose=st.number_input("Glucose Level",min_value=0.0)

    with col3:
        BloodPressure=st.number_input("Blood Pressure Value",min_value=0.0)

    with col1:
        SkinThickness=st.number_input("Skin Thickness Value",min_value=0.0)

    with col2:
        Insulin=st.number_input("Insulin Level",min_value=0.0)

    with col3:
        BMI=st.number_input("BMI Value",min_value=0.0)

    with col1:
        DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function Value",min_value=0.000,format="%.3f")

    with col2:
        Age=st.number_input("Age",min_value=0,step=1,format="%d")


    diabetes_diagnosis=''
    if st.button('Predict'):
        if not all([Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]): # all the fields are required to be field
            st.warning("Please fill all the fields")
        else:
            input_scaled=scaler_diabetes.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
            diabetes_pred=diabetes_model.predict(input_scaled) # passing a list
            if (diabetes_pred[0]==0):
                diabetes_diagnosis='Prediction: The person does not have diabetes'
            else:
                diabetes_diagnosis='Prediction: The person has diabetes'
            st.success(diabetes_diagnosis)

    '''
    ---
    ## Here are some sample user inputs to test the diabetes disease prediction app:

    ### Likely Non-Diabetic Inputs (Healthy)

    ```text
    Pregnancies: 1  
    Glucose: 95.0  
    Blood Pressure: 70.0  
    Skin Thickness: 20.0  
    Insulin: 85.0  
    BMI: 24.0  
    Diabetes Pedigree Function: 0.3  
    Age: 28
    ```

    ```text
    Pregnancies: 2  
    Glucose: 99.0  
    Blood Pressure: 72.0  
    Skin Thickness: 22.0  
    Insulin: 90.0  
    BMI: 26.5  
    Diabetes Pedigree Function: 0.25  
    Age: 30

    ```
    ---

    ### Borderline / Neutral Inputs

    ```text
    Pregnancies: 3  
    Glucose: 125.0  
    Blood Pressure: 75.0  
    Skin Thickness: 24.0  
    Insulin: 100.0  
    BMI: 30.0  
    Diabetes Pedigree Function: 0.5  
    Age: 38
    ```

    ```text
    Pregnancies: 4  
    Glucose: 132.0  
    Blood Pressure: 76.0  
    Skin Thickness: 25.0  
    Insulin: 110.0  
    BMI: 32.0  
    Diabetes Pedigree Function: 0.6  
    Age: 41
    ```

    ---

    ###  Likely Diabetic Inputs (High Risk)

    ```text
    Pregnancies: 6  
    Glucose: 165.0  
    Blood Pressure: 90.0  
    Skin Thickness: 35.0  
    Insulin: 160.0  
    BMI: 37.5  
    Diabetes Pedigree Function: 1.2  
    Age: 50

    ```

    ```text
    Pregnancies: 8  
    Glucose: 180.0  
    Blood Pressure: 85.0  
    Skin Thickness: 40.0  
    Insulin: 190.0  
    BMI: 42.0  
    Diabetes Pedigree Function: 1.5  
    Age: 55

    ```
    '''
# Heart Disease Prediction Page
if(selected=="Heart Disease Prediction"):
    st.title("Heart Disease Prediction") # page title

    # getting the input data from the user
    col1,col2,col3=st.columns(3)

    with col1:
        Age=st.number_input("Age",min_value=0,step=1,format="%d")

    with col2:
        gender=st.selectbox(label="Sex",options=["Male","Female"],index=None)
        if gender=="Male":
            Sex=1
        else:
            Sex=0
    with col3:
        cpt=st.selectbox(label="Chest Pain Type",options=["Typical Angina","Atypical Angina","Non-Anginal Pain","Asymptomatic"],index=None)
        if cpt=="Typical Angina":
            ChestPainType=0
        elif cpt=="Atypical Angina":
            ChestPainType=1
        elif cpt=="Non-Anginal Pain":
            ChestPainType=2
        else:
            ChestPainType=3
    
    with col1:
        RestingBP=st.number_input("Resting Blood Pressure in mm Hg",min_value=0.0)
    
    with col2:
        Cholesterol=st.number_input("Cholesterol(mg/dl)",min_value=0.0)

    with col3:
        fbs=st.number_input("Fasting blood sugar(mg/dl)",min_value=0,step=1,format="%d")
        if fbs>120:
            FastingBS=1
        else:
            FastingBS=0

    with col1:
        rcg=st.selectbox(label="Resting Electrocardiographic Results",options=["Normal","ST-T Wave Abnormality","Left Ventricular Hypertrophy"],index=None)
        if rcg=="Normal":
            RestingECG=0
        elif rcg=="ST-T Wave Abnormality":
            RestingECG=1
        else:
            RestingECG=2
    
    with col2:
        MaxHR=st.number_input("Maximum Heart Rate",min_value=0,step=1,format="%d")
    
    with col3:
        ea=st.selectbox(label="Exercise-Induced Angina",options=["Yes","No"],index=None)
        if ea=="Yes":
            Exang=1
        else:
            Exang=0

    with col1:
        Oldpeak=st.number_input(label="Old Peak Value",min_value=0.0)

    with col2:
        sts=st.selectbox(label="ST Slope",options=["Upsloping","Flat","downsloping"],index=None)
        if sts=="Upsloping":
            ST_Slope=0
        elif sts=="Flat":
            ST_Slope=1
        else:
            ST_Slope=2

    with col3:
        Ca=st.selectbox(label="The number of major vessels",options=[0,1,2,3])
    
    with col1:
        tl=st.selectbox(label="Thalessemia Situation",options=["Null","Normal Blood Flow","Fixed Defect(no blood flow in some part of the heart)","Reversible Defect (a blood flow is observed but it is not normal)"],index=None)
        if tl=="Null":
            Thal=0
        elif tl=="Normal Blood Flow":
            Thal=1
        elif tl=="Fixed Defect(no blood flow in some part of the heart)":
            Thal=2
        else:
            Thal=3

    heart_diagnosis=''
    if st.button('Predict'):
        if any(v is None for v in [Sex,ChestPainType,RestingECG,Exang,ST_Slope,Thal]):
            st.warning("Please select an option for all dropdown fields.")
        elif any(v == 0 for v in [Age,RestingBP,Cholesterol,MaxHR,Oldpeak]):
            st.warning("Please fill in all numeric fields with non-zero values.") # all the fields are required to be field
            # dropdowns can have 0 as value so we use 'None' for them instead of 'all'
        else:
            input_scaled=scaler_heart.transform([[Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,Exang,Oldpeak,ST_Slope,Ca,Thal]])
            heart_pred=heart_model.predict(input_scaled) # passing a list
            if (heart_pred[0]==0):
                heart_diagnosis='Prediction: The person does not have heart disease'
            else:
                heart_diagnosis='Prediction: The person has heart disease'
            st.success(heart_diagnosis)

    '''
    ---
    ## Here are some sample user inputs to test the heart disease prediction:

    ### Likely No Heart Disease (Healthy)

    ```text
    Age: 63  
    Sex: Male 
    ChestPainType: Asymptomatic  
    RestingBP: 150  
    Cholesterol: 280  
    FastingBS: 123  
    RestingECG: Left Ventricular Hypertrophy  
    MaxHR: 120  
    Exang: Yes  
    Oldpeak: 3.0  
    ST_Slope: Downsloping
    Ca: 2  
    Thal: Reversible Defect

    ```
    ---
    ### Borderline / Neutral Inputs

    ```text
    Age: 58  
    Sex: Male
    ChestPainType: Non-Anginal Pain
    RestingBP: 140  
    Cholesterol: 250  
    FastingBS: 122  
    RestingECG: ST-T Wave Abnormality
    MaxHR: 140  
    Exang: No  
    Oldpeak: 1.2  
    ST_Slope: Flat  
    Ca: 1  
    Thal: Reversible Defect

    ```
    ---

    ### Likely Has Heart Disease

    ```text
    Age: 45  
    Sex: Female
    ChestPainType: Atypical Angina
    RestingBP: 120  
    Cholesterol: 210  
    FastingBS: 118  
    RestingECG: Normal
    MaxHR: 165  
    Exang: No
    Oldpeak: 0.5  
    ST_Slope: Upsloping
    Ca: 0  
    Thal: Fixed Defect
    

    ```
    '''
# Parkinsons Disease Prediction Page
if(selected=="Parkinson's Disease Prediction"):
    st.title("Parkinson's Disease Prediction") # page title

    col1,col2,col3=st.columns(3)

    with col1:
        MDVP_Fo_Hz = st.number_input("Average fundamental frequency(pitch) of the voice", min_value=0.000,format="%.3f")

    with col2:
        MDVP_Fhi_Hz	 = st.number_input("Maximum fundamental frequency", min_value=0.000,format="%.3f")

    with col3:
        MDVP_Flo_Hz = st.number_input("Minimum fundamental frequency", min_value=0.000,format="%.3f")

    with col1:
        MDVP_Jitter_Perc= st.number_input("Average deviation in frequency(%)",min_value=0.00000,format="%.5f")

    with col2:
        MDVP_Jitter_Abs = st.number_input("Absolute jitter(in seconds)",min_value=0.00000,format="%.5f")

    with col3:
        MDVP_RAP = st.number_input("Relative Average Perturbation",min_value=0.00000,format="%.5f")
    
    with col1:
        MDVP_PPQ = st.number_input("Five-point Period Perturbation Quotient",min_value=0.00000,format="%.5f")

    with col2:
        Jitter_DDP = st.number_input("Derivative of RAP",min_value=0.00000,format="%.5f")

    with col3:
        MDVP_Shimmer=st.number_input("Average shimmer (amplitude variation as percentage)",min_value=0.00000,format="%.5f")

    with col1:
        MDVP_Shimmer_dB=st.number_input("Shimmer in decibels",min_value=0.00000,format="%.5f")

    with col2:
        Shimmer_APQ3=st.number_input("3-point Amplitude Perturbation Quotient",min_value=0.00000,format="%.5f")

    with col3:
        Shimmer_APQ5=st.number_input("5-point Amplitude Perturbation Quotient",min_value=0.00000,format="%.5f")

    with col1:
        MDVP_APQ=st.number_input("Average Amplitude Perturbation Quotient",min_value=0.00000,format="%.5f")

    with col2:
        Shimmer_DDA=st.number_input("Derivative of APQ3",min_value=0.00000,format="%.5f")

    with col3:
        NHR=st.number_input("Noise-to-Harmonics Ratio",min_value=0.00000,format="%.5f")

    with col1:
        HNR=st.number_input("Harmonics-to-Noise Ratio", min_value=0.000,format="%.3f")

    with col2:
        RPDE=st.number_input("Recurrence Period Density Entropy",min_value=0.000000,format="%.6f")

    with col3:
        DFA=st.number_input("Detrended Fluctuation Analysis",min_value=0.000000,format="%.6f")

    with col1:
        Spread1=st.number_input("1st dimension of signal spread",min_value=-10.000000,format="%.6f")

    with col2:
        Spread2=st.number_input("2nd dimension of signal spread",min_value=0.00000,format="%.6f")
 
    with col3:
        D2=st.number_input("Correlation dimension",min_value=0.000000,format="%.6f")

    with col1:
        PPE=st.number_input("Pitch Period Entropy",min_value=0.000000,format="%.6f")

    parkinsons_diagnosis=''
    if st.button("Predict"):
        if any(v is None or v == 0 for v in [MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_Perc, MDVP_Jitter_Abs, MDVP_RAP,MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, Spread1,Spread2, D2, PPE]):
            st.warning("Please fill all the fields with valid values")

        else:
            input_scaled=scaler_parkinsons.transform([[MDVP_Fo_Hz,MDVP_Fhi_Hz,MDVP_Flo_Hz,MDVP_Jitter_Perc,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,Spread1,Spread2,D2,PPE]])
            parkinsons_pred=parkinsons_model.predict(input_scaled)
            if(parkinsons_pred[0]==0):
                parkinsons_diagnosis="The person does not have Parkinsons's Disease"
            else:
                parkinsons_diagnosis="The person has Parkinsons's Disease"
            st.success(parkinsons_diagnosis)

    '''
    ---
    ## Here are some sample user inputs to test the heart disease prediction:

    ### Likely Healthy (No Parkinson’s)

    ```text
    Average fundamental frequency (pitch) of the voice: 209.14400  
    Maximum fundamental frequency: 237.49400
    Minimum fundamental frequency: 109.37900
    Average deviation in frequency (%): 0.00282
    Absolute jitter (in seconds): 0.00001
    Relative Average Perturbation: 0.00147 
    Five-point Period Perturbation Quotient: 0.0152
    Derivative of RAP: 0.00442
    Average shimmer (amplitude variation as percentage): 0.01861
    Shimmer in decibels: 0.17000
    3-point Amplitude Perturbation Quotient: 0.00975
    5-point Amplitude Perturbation Quotient: 0.01258
    Average Amplitude Perturbation Quotient: 0.01382
    Derivative of APQ3: 0.02925  
    Noise-to-Harmonics Ratio: 0.00871  
    Harmonics-to-Noise Ratio: 25.554
    Recurrence Period Density Entropy: 0.341788  
    Detrended Fluctuation Analysis: 0.678874  
    1st dimension of signal spread: -7.040508  
    2nd dimension of signal spread: 0.066994
    Correlation dimension: 2.460791
    Pitch Period Entropy: 0.101516


    ```
    ---
    ### Borderline / Neutral Inputs

    ```text
    Average fundamental frequency (pitch) of the voice: 140.0  
    Maximum fundamental frequency: 175.0  
    Minimum fundamental frequency: 110.0  
    Average deviation in frequency (%): 0.0045  
    Absolute jitter (in seconds): 0.00004  
    Relative Average Perturbation: 0.0025  
    Five-point Period Perturbation Quotient: 0.0028  
    Derivative of RAP: 0.0075  
    Average shimmer (amplitude variation as percentage): 0.025  
    Shimmer in decibels: 0.3  
    3-point Amplitude Perturbation Quotient: 0.014  
    5-point Amplitude Perturbation Quotient: 0.017  
    Average Amplitude Perturbation Quotient: 0.018  
    Derivative of APQ3: 0.042  
    Noise-to-Harmonics Ratio: 0.02  
    Harmonics-to-Noise Ratio: 18.0  
    Recurrence Period Density Entropy: 0.55  
    Detrended Fluctuation Analysis: 0.68  
    1st dimension of signal spread: -5.5  
    2nd dimension of signal spread: 0.3  
    Correlation dimension: 2.8  
    Pitch Period Entropy: 0.22


    ```
    ---

    ### Likely Has Parkinson’s Disease

    ```text
    Average fundamental frequency (pitch) of the voice: 160.0  
    Maximum fundamental frequency: 180.0  
    Minimum fundamental frequency: 145.0  
    Average deviation in frequency (%): 0.002  
    Absolute jitter (in seconds): 0.00002  
    Relative Average Perturbation: 0.001  
    Five-point Period Perturbation Quotient: 0.0015  
    Derivative of RAP: 0.003  
    Average shimmer (amplitude variation as percentage): 0.02  
    Shimmer in decibels: 0.2  
    3-point Amplitude Perturbation Quotient: 0.01  
    5-point Amplitude Perturbation Quotient: 0.013  
    Average Amplitude Perturbation Quotient: 0.014  
    Derivative of APQ3: 0.03  
    Noise-to-Harmonics Ratio: 0.01  
    Harmonics-to-Noise Ratio: 22.0  
    Recurrence Period Density Entropy: 0.45  
    Detrended Fluctuation Analysis: 0.6  
    1st dimension of signal spread: -4.5  
    2nd dimension of signal spread: 0.2  
    Correlation dimension: 2.1  
    Pitch Period Entropy: 0.1


    ```
    '''
