# from sklearn import pipeline
import streamlit as st
import pandas as pd
# from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
# import joblib

#### Html/CSS

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        h1, h2, h3 {
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
        #customer-churn-dashboard {
            text-align: center;
            }
        </style>
        ''')
st.html(''' <style>
        .stMetric {
        padding: 0px;
        background-color: #1f77b4;
        outline: 4px solid #17becf;
        # box-shadow: 4px 4px #17becf;
        }
        .stMetric > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        }
        .stMetric > div > label > div > div > p {
        font-size: 12px;
        # text-shadow: 2px 4px 2px black;
        }
        .stMetric > div > div {
        font-size: 18px;
        # text-shadow: 2px 4px 2px black;
        }
        </style>
        ''')

st.html(''' <style>
        .stPlotlyChart {
        # padding: 6px;
        # background-color: #9467bd;
        outline: 4px solid #17becf;
        border-radius: 5px;
        }
        </style>
        '''
)

st.html(''' <style>
        .container1 {
        outline: 4px solid #17becf;
        border-radius: 5px;
        }
        </style>
        '''
)
#### data loading function

def load_data(file):
    data = pd.read_csv(file)
    return data

#### plotting functions

def plot_countplot(x):
    fig = px.histogram(df, x=x, color="Churn",barmode='group', width=600, height=180, color_discrete_sequence=["#17becf",'#1f77b4'])
    fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig)

def group_countplot():
    df['tenure_group'] = pd.cut(df['tenure'], bins=[0,12,24,48,72], labels=['0–1yr','1–2yrs','2–4yrs','4–6yrs'])
    tenure_summary = df.groupby('tenure_group')['Churn'].value_counts(normalize=True).unstack() * 100
    fig = px.bar(tenure_summary, x=tenure_summary.index, y=['No', 'Yes'], labels={'value':'Percentage', 'tenure_group':'Tenure Group'}, color_discrete_sequence=["#17becf",'#1f77b4'], width=600, height=180)
    fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig)

def importance_plot():
    feature_importance = load_data('../feature_importance.csv')
    fig = px.bar(feature_importance.sort_values("Importance"), x="Importance", y="Feature", color = "Churn Driver" ,color_discrete_sequence=["#17becf",'#1f77b4'], width=600, height=180)
    fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig)


#### Main Code

with st.container(border=False,horizontal_alignment ="center"):
    with st.container(border=False, width = 1400):
        st.title("Customer Churn Dashboard")
        container1 = st.container(border=True)
        with container1:
            df = load_data('../cleaned_data.csv')
            col1, col2, col3 = st.columns([0.1,0.6,0.4])
            with col1:
                st.metric(label="Churn Rate", value="26.54%",border = True)
                st.metric(label="Lifetime (Avg)", value="2.7 years",border = True)
                st.metric(label="MRR at Risk", value="$139,130",border = True)
                st.metric(label="High-Value CR", value="19.30%",border = True)
            with col2:
                col11, col12 = st.columns(2)
                with col11:
                    plot_countplot("TechSupport")

                with col12:
                    group_countplot()
                plot_countplot("PaymentMethod")           
            with col3:
                plot_countplot("tenure")
                importance_plot()

            col4, col5, col6 = st.columns([0.2,0.4,0.5])
            with col4:
                plot_countplot("MonthlyCharges")
            with col5:
                plot_countplot("Contract")
            with col6:
                st.dataframe(df, hide_index=True, height=180, width = 750)

    

    