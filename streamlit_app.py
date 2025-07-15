import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai
import io

# 🔐 Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "your-api-key-here"

st.set_page_config(page_title="AI Excel Dashboard Generator", layout="wide")

# Title and Description
st.title("📊 AI-Powered Excel Dashboard Generator")
st.markdown("Upload an Excel file and get instant AI insights and charts.")

# File Uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"], key="excel_uploader")

# Sidebar Options
st.sidebar.header("Dashboard Settings")
chart_type = st.sidebar.selectbox("Chart Type", ["Bar", "Line", "Heatmap"])
use_ai_analysis = st.sidebar.checkbox("Include AI Insights", value=True)

# Function to generate AI insights
def generate_ai_summary(df):
    prompt = f"""You are a data analyst. Analyze this dataset and provide insights:\n\n{df.head(10).to_markdown()}"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error generating insights: {e}"

# When a file is uploaded
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        st.subheader("📄 Data Preview")
        st.dataframe(df, use_container_width=True)

        # Dropdown to select column for visualization
        numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()
        if len(numeric_cols) >= 2:
            x_col = st.selectbox("X-Axis", numeric_cols, key="x_col")
            y_col = st.selectbox("Y-Axis", numeric_cols, key="y_col")

            # Plot
            st.subheader("📈 Chart")
            fig, ax = plt.subplots()
            if chart_type == "Bar":
                sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
            elif chart_type == "Line":
                sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
            elif chart_type == "Heatmap":
                sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

        # Button to analyze with AI
        if use_ai_analysis and st.button("🧠 Analyze with AI", key="analyze_button"):
            with st.spinner("Generating AI insights..."):
                summary = generate_ai_summary(df)
                st.subheader("🔍 AI Analysis")
                st.markdown(summary)

    except Exception as e:
        st.error(f"Error reading file: {e}")

