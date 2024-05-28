import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import base64

# Function to load image as base64
def load_image(image_file):
    with open(image_file, 'rb') as f:
        img_base64 = base64.b64encode(f.read()).decode()
    return img_base64

# Load background image
background_image_path = background_image_path = r"C:\Users\Hp\Downloads\wallpaperflare.com_wallpaper (1).jpg"
background_image_style = f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{load_image(background_image_path)}");
            background-size: cover;
        }}
    </style>
"""
st.markdown(background_image_style, unsafe_allow_html=True)

# Load the pre-trained models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open("heart_disease.sav", 'rb'))
breast_cancer_model = pickle.load(open("breast_cancer_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction','Breast Cancer Prediction'],                   
                           icons=['activity', 'heart-pulse-fill','bandaid'],
                           default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies', key='pregnancies_key')

    with col2:
        glucose = st.text_input('Glucose Level', key='glucose_key')

    with col3:
        blood_pressure = st.text_input('Blood Pressure value', key='blood_pressure_key')

    with col1:
        skin_thickness = st.text_input('Skin Thickness value', key='skin_thickness_key')

    with col2:
        insulin = st.text_input('Insulin Level', key='insulin_key')

    with col3:
        bmi = st.text_input('BMI value', key='bmi_key')

    with col1:
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function value', key='diabetes_pedigree_function_key')

    with col2:
        age = st.text_input('Age of the Person', key='age_key')

    # Convert input values to numeric types
    pregnancies = int(pregnancies) if pregnancies else 0
    glucose = float(glucose) if glucose else 0.0
    blood_pressure = float(blood_pressure) if blood_pressure else 0.0
    skin_thickness = float(skin_thickness) if skin_thickness else 0.0
    insulin = float(insulin) if insulin else 0.0
    bmi = float(bmi) if bmi else 0.0
    diabetes_pedigree_function = float(diabetes_pedigree_function) if diabetes_pedigree_function else 0.0
    age = int(age) if age else 0

    # Predict diabetes
    Diabetes_Diagnosis = ''
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        if diabetes_prediction[0] == 1:
            Diabetes_Diagnosis = 'The Person is Diabetic'
        else:
            Diabetes_Diagnosis = 'The Person is not Diabetic'
    st.success(Diabetes_Diagnosis)

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age of Patient', key='age_input')

    with col2:
        sex = st.text_input('Gender of Patient (0 for female, 1 for male)', key='sex_input')

    with col3:
        cp = st.text_input('Chest Pain Type (0-3)', key='cp_input')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', key='trestbps_input')

    with col2:
        chol = st.text_input('Serum Cholesterol', key='chol_input')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar (0 or 1)', key='fbs_input')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (0-2)', key='restecg_input')

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved', key='thalach_input')

    with col3:
        exang = st.text_input('Exercise Induced Angina (0 or 1)', key='exang_input')

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest', key='oldpeak_input')

    with col2:
        slope = st.text_input('The Slope of the Peak Exercise ST Segment (0-2)', key='slope_input')

    with col3:
        ca = st.text_input('Number of Major Vessels (0-3)', key='ca_input')

    with col1:
        thal = st.text_input('Thalassemia Value (0-3)', key='thal_input')

    # Convert input values to numeric types
    age = int(age) if age else 0
    sex = int(sex) if sex else 0
    cp = int(cp) if cp else 0
    trestbps = float(trestbps) if trestbps else 0.0
    chol = float(chol) if chol else 0.0
    fbs = int(fbs) if fbs else 0
    restecg = int(restecg) if restecg else 0
    thalach = float(thalach) if thalach else 0.0
    exang = int(exang) if exang else 0
    oldpeak = float(oldpeak) if oldpeak else 0.0
    slope = int(slope) if slope else 0
    ca = int(ca) if ca else 0
    thal = int(thal) if thal else 0

    # Predict heart disease
    Heart_Disease_Diagnosis = ''
    if st.button('Heart Disease Test Result'):
        Heart_Disease_Prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        if Heart_Disease_Prediction[0] == 1:
            Heart_Disease_Diagnosis = 'The Person has Heart Disease'
        else:
            Heart_Disease_Diagnosis = 'The Person does not have Heart Disease'
    st.success(Heart_Disease_Diagnosis)
    
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean_input = st.text_input('Radius mean', key='radius_mean')
        texture_mean_input= st.text_input('Texture mean', key='texture_mean')
        perimeter_mean_input = st.text_input('Perimeter mean', key='perimeter_mean')
        area_mean_input = st.text_input('Area mean', key='area_mean')
        smoothness_mean_input = st.text_input('Smoothness mean', key='smoothness_mean')
        compactness_mean_input = st.text_input('Compactness mean', key='compactness_mean')
        concavity_mean_input = st.text_input('Concavity mean', key='concavity_mean')
        concave_points_mean_input = st.text_input('Concave points mean', key='concave_points_mean')
        symmetry_mean_input = st.text_input('Symmetry mean', key='symmetry_mean')
        fractal_dimension_mean_input = st.text_input('Fractal dimension mean', key='fractal_dimension_mean')

        radius_mean = float(radius_mean_input) if radius_mean_input else 0.0
        texture_mean = float(texture_mean_input) if texture_mean_input else 0.0
        perimeter_mean = float(perimeter_mean_input) if perimeter_mean_input else 0.0
        area_mean = float(area_mean_input) if area_mean_input else 0.0
        smoothness_mean = float(smoothness_mean_input) if smoothness_mean_input else 0.0
        compactness_mean = float(compactness_mean_input) if compactness_mean_input else 0.0
        concavity_mean = float(concavity_mean_input) if concavity_mean_input else 0.0
        concave_points_mean = float(concave_points_mean_input) if concave_points_mean_input else 0.0
        symmetry_mean = float(symmetry_mean_input) if symmetry_mean_input else 0.0
        fractal_dimension_mean = float(fractal_dimension_mean_input) if fractal_dimension_mean_input else 0.0

    with col2:
        radius_se_input = st.text_input('Radius se', key='radius_se')
        texture_se_input = st.text_input('Texture se', key='texture_se')
        perimeter_se_input = st.text_input('Perimeter se', key='perimeter_se')
        area_se_input = st.text_input('Area se', key='area_se')
        smoothness_se_input = st.text_input('Smoothness se', key='smoothness_se')
        compactness_se_input = st.text_input('Compactness se', key='compactness_se')
        concavity_se_input = st.text_input('Concavity se', key='concavity_se')
        concave_points_se_input = st.text_input('Concave points se', key='concave_points_se')
        symmetry_se_input = st.text_input('Symmetry se', key='symmetry_se')
        fractal_dimension_se_input = st.text_input('Fractal dimension se', key='fractal_dimension_se')
    
        radius_se = float(radius_se_input) if radius_se_input else 0.0
        texture_se = float(texture_se_input) if texture_se_input else 0.0
        perimeter_se = float(perimeter_se_input) if perimeter_se_input else 0.0
        area_se = float(area_se_input) if area_se_input else 0.0
        smoothness_se = float(smoothness_se_input) if smoothness_se_input else 0.0
        compactness_se = float(compactness_se_input) if compactness_se_input else 0.0
        concavity_se = float(concavity_se_input) if concavity_se_input else 0.0
        concave_points_se = float(concave_points_se_input) if concave_points_se_input else 0.0
        symmetry_se = float(symmetry_se_input) if symmetry_se_input else 0.0
        fractal_dimension_se = float(fractal_dimension_se_input) if fractal_dimension_se_input else 0.0

    with col3:
        radius_worst_input = st.text_input('Radius worst', key='radius_worst')
        texture_worst_input = st.text_input('Texture worst', key='texture_worst')
        perimeter_worst_input = st.text_input('Perimeter worst', key='perimeter_worst')
        area_worst_input = st.text_input('Area worst', key='area_worst')
        smoothness_worst_input = st.text_input('Smoothness worst', key='smoothness_worst')
        compactness_worst_input = st.text_input('Compactness worst', key='compactness_worst')
        concavity_worst_input = st.text_input('Concavity worst',key='concavity_worst')
        concave_points_worst_input = st.text_input('Concave points worst',key='concave_points_worst')
        symmetry_worst_input = st.text_input('Symmetry worst',key='symmetry_worst')
        fractal_dimension_worst_input = st.text_input('Fractal dimension worst',key='fractal_dimension_worst')

        radius_worst = float(radius_worst_input) if radius_worst_input else 0.0
        texture_worst = float(texture_worst_input) if texture_worst_input else 0.0
        perimeter_worst = float(perimeter_worst_input) if perimeter_worst_input else 0.0
        area_worst = float(area_worst_input) if area_worst_input else 0.0
        smoothness_worst = float(smoothness_worst_input) if smoothness_worst_input else 0.0
        compactness_worst = float(compactness_worst_input) if compactness_worst_input else 0.0
        concavity_worst = float(concavity_worst_input) if concavity_worst_input else 0.0
        concave_points_worst = float(concave_points_worst_input) if concave_points_worst_input else 0.0
        symmetry_worst = float(symmetry_worst_input) if symmetry_worst_input else 0.0
        fractal_dimension_worst = float(fractal_dimension_worst_input) if fractal_dimension_worst_input else 0.0




    # Predict cancer
    Breast_Cancer_Diagnosis = ''
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
        compactness_mean,concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
        radius_se, texture_se, perimeter_se, area_se, smoothness_se,
        compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
        radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
        compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])
        if breast_cancer_prediction[0] == 1:
            Breast_Cancer_Diagnosis = 'The Breast Cancer is Benign'
        else:
            Diabetes_Diagnosis = 'The Breast cancer is Malignant'
    st.success(Breast_Cancer_Diagnosis)