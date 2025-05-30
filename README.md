# Multiple Disease Prediction System

A comprehensive AI-powered health screening assistant that predicts the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson's Disease** using machine learning models. Built with Streamlit for an intuitive web interface and deployed with pre-trained models for real-time predictions.

![Health Screening Assistant](20250526_1738_Disease%20Prediction%20System_remix_01jw67tpgxfbt9gy7v8b6b10ag.png)

---

## 🌟 Features

- **Multi-Disease Prediction**: Supports prediction for three critical health conditions
- **Interactive Web Interface**: User-friendly Streamlit application with intuitive navigation
- **Real-time Predictions**: Instant results using pre-trained machine learning models
- **Sample Data Provided**: Test cases included for each disease prediction
- **Standardized Input Processing**: Features are automatically scaled for optimal model performance

---

## 🏥 Supported Diseases

### 1. **Diabetes Prediction**
Predicts diabetes risk based on:
- Number of pregnancies
- Glucose level
- Blood pressure
- Skin thickness
- Insulin level
- BMI (Body Mass Index)
- Diabetes Pedigree Function
- Age

### 2. **Heart Disease Prediction**
Assesses cardiovascular risk using:
- Age and gender
- Chest pain type
- Resting blood pressure
- Cholesterol levels
- Fasting blood sugar
- Resting electrocardiographic results
- Maximum heart rate
- Exercise-induced angina
- ST depression and slope
- Number of major vessels
- Thalassemia status

### 3. **Parkinson's Disease Prediction**
Analyzes voice measurements including:
- Fundamental frequency variations
- Jitter and shimmer measurements
- Noise-to-harmonics ratios
- Nonlinear dynamical complexity measures
- Signal processing features

---

## 📁 Project Structure

```
├── application.py                    # Main Streamlit application
├── requirements.txt                  # Python dependencies
├── diabetes_model.pkl               # Trained diabetes prediction model
├── heart_model.pkl                  # Trained heart disease prediction model
├── parkinsons_model.pkl             # Trained Parkinson's disease prediction model
├── standardized_diabetes.pkl        # Feature scaler for diabetes data
├── standardized_heart.pkl           # Feature scaler for heart disease data
├── standardized_parkinsons.pkl      # Feature scaler for Parkinson's data
└── 20250526_1738_Disease_Prediction_System_remix_01jw67tpgxfbt9gy7v8b6b10ag.png
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd multiple-disease-prediction-system
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run application.py
```

### Step 4: Access the Application
Open your web browser and navigate to:
```
http://localhost:8501
```

---

## 💻 Usage

1. **Launch the Application**: Run the Streamlit app using the command above
2. **Navigate**: Use the sidebar menu to select the disease prediction you want to perform
3. **Input Data**: Fill in the required medical parameters in the form
4. **Get Prediction**: Click the "Predict" button to receive instant results
5. **Test with Samples**: Use the provided sample inputs to test the application

---

## 📊 Sample Test Cases

Each prediction page includes comprehensive test cases:

### Diabetes Prediction Examples
- **Healthy Profile**: Low glucose, normal BMI, younger age
- **Borderline Risk**: Moderate values across parameters
- **High Risk**: Elevated glucose, high BMI, multiple risk factors

### Heart Disease Examples
- **Low Risk**: Optimal blood pressure, normal cholesterol
- **Moderate Risk**: Some elevated parameters
- **High Risk**: Multiple cardiovascular risk factors

### Parkinson's Disease Examples
- **Healthy Voice**: Normal frequency variations and harmonics
- **Borderline**: Slight voice irregularities
- **Parkinson's Indicators**: Significant voice tremor patterns

---

## 🔧 Technical Details

### Machine Learning Models
- **Algorithms**: The system uses trained classification models (specific algorithms may include SVM, Random Forest, or Neural Networks)
- **Feature Scaling**: All inputs are standardized using pre-fitted scalers for optimal model performance
- **Model Format**: Models are serialized using Python's pickle module for efficient loading

### Dependencies
- **Streamlit**: Web application framework
- **Streamlit-option-menu**: Enhanced navigation menu
- **Scikit-learn**: Machine learning library for model operations
- **NumPy**: Numerical computing for data processing
- **Pickle**: Model serialization and deserialization

---

## ⚠️ Important Disclaimers

- **Medical Advisory**: This tool is for educational and screening purposes only
- **Not a Substitute**: Results should not replace professional medical diagnosis
- **Consult Healthcare Providers**: Always seek medical advice for health concerns
- **Accuracy Limitations**: Model predictions are based on training data and may not be 100% accurate

---

## 🛠️ Development

### Adding New Features
1. **New Disease Models**: Add new pickle files and update the navigation menu
2. **Enhanced UI**: Modify the Streamlit interface in `application.py`
3. **Model Updates**: Replace existing pickle files with retrained models

### Model Training
The models were trained on standard medical datasets. To retrain:
1. Prepare your dataset with appropriate features
2. Train using scikit-learn or similar ML libraries
3. Save models and scalers using pickle
4. Update the application to load new models

---

## 📈 Future Enhancements

- [ ] Add more disease prediction models
- [ ] Implement model confidence scores
- [ ] Add data visualization for risk factors
- [ ] Include historical prediction tracking
- [ ] Deploy to cloud platforms (Heroku, AWS, etc.)
- [ ] Add user authentication and data storage
- [ ] Implement API endpoints for integration

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed as a comprehensive health screening tool combining machine learning with user-friendly web interfaces for accessible medical risk assessment.

---

## 🆘 Support

If you encounter any issues or have questions:
1. Check the sample inputs provided in each prediction page
2. Ensure all required fields are filled correctly
3. Verify that dependencies are properly installed
4. Open an issue in the GitHub repository for technical problems

---

**🔥 Ready to start predicting? Launch the app and explore the power of AI in healthcare screening!**