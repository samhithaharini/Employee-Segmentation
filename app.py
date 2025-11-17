import streamlit as st
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
kmeans = joblib.load("kmeans_model.pkl")
cluster_mapping = joblib.load("cluster_mapping.pkl")

level_meaning = {
    "Junior": "Employees with lower productivity and fewer completed projects. They may require guidance and training.",
    "Mid": "Employees performing at an average level with moderate productivity and consistent output.",
    "Senior": "High-performing employees with strong productivity and maximum project completion efficiency."
}

st.set_page_config(page_title="Employee Level Predictor", layout="centered")

st.title("Employee Level Prediction App")
st.write("Enter employee details to predict their performance level.")

# Inputs
age = st.number_input("Age", min_value=18, max_value=60, step=1)
salary = st.number_input("Salary", min_value=10000, max_value=200000, step=1000)
projects = st.number_input("Projects Completed", min_value=0, max_value=50, step=1)
productivity = st.number_input("Productivity (%)", min_value=0, max_value=100, step=1)

# Predict button
if st.button("Predict Level"):
    # Prepare features: only 2 features used in clustering
    X = np.array([[projects, productivity]])
    
    # Scale
    X_scaled = scaler.transform(X)
    
    # Predict cluster
    cluster = kmeans.predict(X_scaled)[0]
    
    # Convert cluster → level
    level = cluster_mapping.get(cluster, "Unknown")
    
    # Meaning of level
    meaning = level_meaning.get(level, "No description available.")
    
    # Display results
    st.subheader("Prediction Result")
    st.write(f"**Cluster:** {cluster}")
    st.write(f"**Employee Level:** {level}")
    st.write(f"**Meaning:** {meaning}")
