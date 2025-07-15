import streamlit as st
import pandas as pd
import openai
import matplotlib.pyplot as plt
import seaborn as sns
import io

st.set_page_config(page_title="AI Dashboard Generator", layout="wide")
st.title("📊 AI-Powered Excel Dashboard Generator")

# --- Upload Excel File ---
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    # Optional: let user choose prompt
    prompt = st.text_area("✏️ Describe what you want to analyze (e.g. 'Summarize project status')", 
                          value="Give a summary of the uploaded construction data.")

    # --- Generate AI Insights ---
    if st.button("🧠 Analyze with AI"):
        with st.spinner("Thinking..."):
            # Prepare data sample (first 1000 chars of CSV for context)
            data_sample = df.head(10).to_csv(index=False)
            system_prompt = "You are a helpful assistant who summarizes and analyzes Excel data for dashboards."

            openai.api_key = st.secrets["OPENAI_API_KEY"]  # Add this in Streamlit Cloud secrets

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{prompt}\n\nHere is the sample data:\n{data_sample}"}
                ]
            )
            result = response.choices[0].message.content
            st.success("✅ Analysis complete:")
            st.markdown(result)

    # --- Visualization ---
    st.subheader("📈 Quick Charts")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("Select X-axis", numeric_cols)
        y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1)
        chart_type = st.radio("Chart Type", ["Scatter", "Line", "Bar"])

        fig, ax = plt.subplots()
        if chart_type == "Scatter":
            sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        elif chart_type == "Line":
            sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        elif chart_type == "Bar":
            sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)

        st.pyplot(fig)
    # --- Generate AI Insights ---
    if st.button("🧠 Analyze with AI"):
        with st.spinner("Thinking..."):
            data_sample = df.head(10).to_csv(index=False)
            system_prompt = "You are a helpful assistant who summarizes Excel data."

            openai.api_key = st.secrets["OPENAI_API_KEY"]  # Make sure you set this in secrets

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{prompt}\n\nHere is the sample data:\n{data_sample}"}
                ]
            )
            result = response.choices[0].message.content
            st.success("✅ Analysis complete:")
            st.markdown(result)

    # --- Visualization ---
    st.subheader("📈 Quick Charts")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("Select X-axis", numeric_cols)
        y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1)
        chart_type = st.radio("Chart Type", ["Scatter", "Line", "Bar"])

        fig, ax = plt.subplots()
        if chart_type == "Scatter":
            sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        elif chart_type == "Line":
            sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        elif chart_type == "Bar":
            sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)

        st.pyplot(fig)
    # --- Generate AI Insights ---
    if st.button("🧠 Analyze with AI"):
        with st.spinner("Thinking..."):
            data_sample = df.head(10).to_csv(index=False)
            system_prompt = "You are a helpful assistant who summarizes Excel data."

            openai.api_key = st.secrets["OPENAI_API_KEY"]  # Make sure you set this in secrets

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{prompt}\n\nHere is the sample data:\n{data_sample}"}
                ]
            )
            result = response.choices[0].message.content
            st.success("✅ Analysis complete:")
            st.markdown(result)

    # --- Visualization ---
    st.subheader("📈 Quick Charts")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("Select X-axis", numeric_cols)
        y_axis = st.selectbox("Select Y-axis", numeric_cols, index=1)
        chart_type = st.radio("Chart Type", ["Scatter", "Line", "Bar"])

        fig, ax = plt.subplots()
        if chart_type == "Scatter":
            sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        elif chart_type == "Line":
            sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        elif chart_type == "Bar":
            sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)

        st.pyplot(fig)
