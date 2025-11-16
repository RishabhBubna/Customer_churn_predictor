import streamlit as st

home_page = st.Page("Home_page.py", title="Home", icon=":material/home:")
page_1 = st.Page("page_1.py", title="Dashboard", icon=":material/analytics:")
page_2 = st.Page("page_2.py", title="Predictive Model", icon=":material/model_training:")
pg = st.navigation([home_page, page_1, page_2], position="top")

st.html(''' <style>
        .stAppHeader {
            font-family:sans-serif;
        }
</style>
''')

st.set_page_config(
    page_title="Customer Churn Analysis and Prediction",
    layout="wide",
    page_icon=":material/network_intelligence:"
)
pg.run()





