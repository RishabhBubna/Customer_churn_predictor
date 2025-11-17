from sklearn import pipeline
import streamlit as st
import pandas as pd
import joblib

#### Html/CSS

st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6{
            font-family: 'Playfair Display', serif !important;
        }
    </style>
""", unsafe_allow_html=True)

st.html(''' <style>
        .stMainBlockContainer {
            padding: 20px 80px 0px;
        }
</style>
''')

st.html(''' <style>
        .stNumberInput > label > div {
            font-size: 16px;
            # color: #17becf;
        }
</style>
''')

st.html(''' <style>
        .stNumberInput > div{
            border : 2px solid black;
        
        }
</style>
''')

st.html(''' <style>
        .stSelectbox > label > div {
            font-size: 16px;
            # color: #17becf;
        }
</style>
''')

st.html(''' <style>
        .stSelectbox > div > div{
            border : 2px solid black;
        }
</style>
''')

st.html(''' <style>
        .stButton > button {
            border : 4px solid black;
            background-color: #1f77b4;
        }
</style>
''')

st.html(''' <style>
        .stButton > button > div >  p {
            font-size: 25px;
            font-weight: bold;
            color: white;
            text-align: center;
        }
</style>
''')

st.html(''' <style>
        .stAlert {
            text-align: center;
        }
</style>
''')

st.html(''' <style>
        .stAlert > div > div > div > div > div > p {
            font-size: 20px;
        }
</style>
''')

st.html(''' <style>
        #customer-churn-predictor {
            text-align: center;
            }
        </style>
        ''')

st.html(''' <style>
        #use-the-logistic-regression-model-to-predict-whether-a-customer-will-churn-or-not-based-on-the-input-features {
            text-align: center;
            }
        </style>
        ''')

#### Function to load the model

def load_model(file):
    model = joblib.load(file)
    return model

#### Main code

with st.container(border=False,horizontal_alignment ="center"):
    with st.container(border=False, width = 1400):
        st.title("Customer Churn Predictor")
        st.markdown(
                """
                ###### Use the :red[Logistic Regression] model to predict whether a customer will churn or not based on the input features.
                """
            )
        model = load_model("log_reg_churn_pipeline.pkl")
        col_name = ['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection',
                    'TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            tenure = st.number_input("Tenure (Months)", min_value=0, max_value=120, step=1, width = 200)
            monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, step=0.1, format="%.2f", width = 200)
            total_charges = tenure * monthly_charges
            gender = st.selectbox("Gender", options=["Female", "Male"], index=None, placeholder="Select Option", width = 200)
            contract = st.selectbox("Contract", options=["Month-to-month", "One year", "Two year"], index=None, placeholder="Select Option", width = 200)
            paperless_billing = st.selectbox("Paperless Billing", options=["No", "Yes"], index=None, placeholder="Select Option", width = 200)
        with col2:
            senior_citizen = st.selectbox("Senior Citizen", options=["No", "Yes"], index=None, placeholder="Select Option", width = 200)
            # senior_citizen = st.radio("Senior Citizen", options=["No", "Yes"], index=None, horizontal=False, key="senior_citizen_radio")
            partner = st.selectbox("Partner", options=["No", "Yes"], index=None, placeholder="Select Option", width = 200)
            dependents = st.selectbox("Dependents", options=["No", "Yes"], index=None, placeholder="Select Option", width = 200)
            phone_service = st.selectbox("Phone Service", options=["No", "Yes"], index=None, placeholder="Select Option", width = 200)
            payment_method = st.selectbox("Payment Method", options=["Bank transfer (automatic)", "Credit card (automatic)", "Electronic check", "Mailed check"], index=None, placeholder="Select Option", width = 200)
        with col3:
            multiple_lines = st.selectbox("Multiple Lines", options=["No phone service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
            # multiple_lines = st.radio("Multiple Lines", options=["No phone service", "No", "Yes"], index=None, horizontal=False, key="multiple_lines_radio")
            internet_service = st.selectbox("Internet Service", options=["DSL", "Fiber optic", "No"], index=None, placeholder="Select Option", width = 200)
            online_security = st.selectbox("Online Security", options=["No internet service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
            online_backup = st.selectbox("Online Backup", options=["No internet service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
        with col4:
            device_protection = st.selectbox("Device Protection", options=["No internet service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
            tech_support = st.selectbox("Tech Support", options=["No internet service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
            streaming_tv = st.selectbox("Streaming TV", options=["No internet service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
            streaming_movies = st.selectbox("Streaming Movies", options=["No internet service", "No", "Yes"], index=None, placeholder="Select Option", width = 200)
        
        col4, col5, col6 = st.columns([0.3,0.4,0.3])
        with col5:
            if st.button("Predict Churn", width = 540):
                input_data = pd.DataFrame([[gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines, internet_service,
                                            online_security, online_backup, device_protection, tech_support,
                                            streaming_tv, streaming_movies, contract, paperless_billing,
                                            payment_method, monthly_charges, total_charges]], columns=col_name)
                if input_data.isnull().values.any():
                    st.error("Please fill all the input fields.")
                else:
                    prob = model.predict_proba(input_data)[:, 1]

                    if prob[0] >= 0.60:
                        st.error('Probability of Churn: {:.2f}%, High Risk of Churn!'.format(prob[0] * 100))
                    elif prob[0] < 0.60 and prob[0] >= 0.40:
                        st.warning('Probability of Churn: {:.2f}%, Moderate Risk of Churn.'.format(prob[0] * 100))
                    else:
                        st.success('Probability of Churn: {:.2f}%, Low Risk of Churn.'.format(prob[0] * 100))




