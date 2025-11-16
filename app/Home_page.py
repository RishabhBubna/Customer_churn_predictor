import streamlit as st
import pandas as pd
# from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

#### HTML/CSS

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Playfair Display', serif !important;
        }
        p {
            font-family: 'Playfair Display', serif !important;
            }
    </style>
""", unsafe_allow_html=True)

st.html(''' <style>
        .stMainBlockContainer {
            padding: 0px 80px 0px;
        }
</style>
''')

st.html(''' <style>
        #customer-churn-analysis-and-prediction {
            text-align: center;
            }
        </style>
        ''')
st.html(''' <style>
        #an-interactive-web-application-to-present-the-analysis-of-teleco-customer-churn-dataset-and-use-the-trained-model-to-predict-customer-churn {
            text-align: center;
            }
        </style>
        ''')

st.html(''' <style>
        .stHeading > hr {
            background-color: rgb(255, 108, 108);
            height: 2px;
            }
        </style>
        ''')

#### Main code

with st.container(border=False,horizontal_alignment ="center"):

    with st.container(border=False, width = 1400):
        st.title("Customer Churn Analysis and Prediction",width="stretch")
        st.markdown(
            """
            ###### _An interactive web application to present the analysis of [Teleco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and use the trained model to predict customer churn._
            """
        )
        with st.columns(3)[1]:
            st.markdown(
            ":red-badge[Python] :blue-badge[Pandas] :yellow-badge[Scikit-learn] :green-badge[Logistic Regression] :violet-badge[Streamlit]"
        )
        col1, col2 = st.columns(2)
        with col1:
            st.header("Understanding Customer Churn", divider = "yellow",width = "content")
            st.subheader("What is Customer Churn?")

            st.markdown(
                """
                Customer churn refers to the rate at which customers or clients stop doing business with a company over a given period, often indicating potential problems with the company's products, services, or customer satisfaction levels.
                """
            )


            st.subheader("How does Customer Churn Impact Businesses?")

            st.markdown(
                """
                Customer churn reduces revenue by cutting off recurring income, increasing acquisition costs to replace lost customers, and lowering overall customer lifetime value, which slows business growth.
                """
            )
            st.subheader("How can businesses reduce customer churn?")

            st.markdown(
                """
                Businesses can reduce customer churn by strengthening customer relationships through excellent support, personalizing services, analyzing churn data to identify risks early, and offering loyalty programs or targeted retention incentives.
                """
            )
        with col2:
            st.header("Project Overview", divider = "yellow",width = "content")

            st.markdown(
                """
                This project analyzes customer churn behavior for a telecom company and develops data-driven strategies to improve customer retention. It combines exploratory data analysis, predictive modeling, and business insight generation to identify high-risk customer segments and recommend targeted interventions.
                -  :red[Dashboard]: An interactive dashboard visualizes key churn metrics, customer demographics, and service usage patterns to help stakeholders understand churn drivers.
                -  :red[Predictive Model]: A logistic regression model which predicts the likelihood of individual customers churning.
                """
            )
