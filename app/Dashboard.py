import streamlit as st
from PIL import Image

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Customer Churn Executive Dashboard",
    page_icon="📊",
    layout="wide",
)

# ---------------------------
# Header
# ---------------------------
st.title("📊 Customer Churn Executive Summary")
st.markdown("""
This dashboard summarizes key insights from the **Customer Churn Analysis** project.  
It highlights major churn drivers, predictive model performance, and data-driven retention strategies for a telecom company.
""")

st.divider()

# ---------------------------
# KPI Section
# ---------------------------
st.subheader("📈 Key Performance Indicators")

col1, col2, col3 = st.columns(3)
col1.metric("Overall Churn Rate", "26.5%", "Moderate imbalance")
col2.metric("Best ROC_AUC", "0.86", "Logistic Regression")
col3.metric("Accuracy", "75%", "Good Accuracy")

st.divider()

# ---------------------------
# Visual Insights
# ---------------------------
st.subheader("🔍 Visual Insights")

col1, col2 = st.columns(2)

# Load your saved plots
churn_contract = Image.open("../images/Customer_churn_by_contract.png")
churn_tenure = Image.open("../images/Customer_churn_by_tenure_group.png")

col1.image(churn_contract, caption="Churn by Contract Type", use_container_width=True)
col2.image(churn_tenure, caption="Churn by Tenure", use_container_width=True)

st.markdown("""
- **Month-to-month contracts** are the highest churn segment.  
- **Early-tenure customers** are more likely to leave within the first year.
""")

st.divider()

# ---------------------------
# Feature Importance / Modeling
# ---------------------------
st.subheader("🧠 Model Insights")

feature_importance = Image.open("../images/Churn_drivers.png")
st.image(feature_importance, caption="Feature Importance (Logistic Regression)", use_container_width=True)

st.markdown("""
The model identifies key churn drivers:
- **Contract Type**, **Tenure**, and **Tech Support** are top predictors.
- **Tenure** and **Value Added Services** reduce churn risk
- **Month-To-Month Contract** and **Higher Monthly Charges** increases churn risk.
""")

st.divider()

# ---------------------------
# Recommendations
# ---------------------------
st.subheader("💡 Strategic Recommendations")

st.markdown("""
✅ **Retention Incentives:** Offer loyalty rewards to customers in their first year.  
✅ **Contract Upgrades:** Encourage long-term plans via discounts or bundled offers.  
✅ **Service Bundles:** Promote Online Security and Tech Support add-ons.  
✅ **Payment Optimization:** Nudge electronic check users toward automatic payments.

These strategies can **reduce churn by 10–15%** and improve overall **customer lifetime value**.
""")

st.success("🎯 Data-driven actions transform insights into measurable business outcomes.")

st.divider()

# ---------------------------
# Footer
# ---------------------------
st.caption("Built by Rishabh Bubna | Physicist | Data Science & Business Analytics Consultant")
