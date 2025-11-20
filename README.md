# **Employee Segmentation using KNN**

Employee segmentation helps organizations understand employee behavior and performance.  
This project uses the **K-Nearest Neighbors (KNN)** algorithm to classify employees into meaningful groups based on performance-related metrics.

---

## **Project Overview**
This project performs clustering on employee data to group employees into segments such as:
- High Performers  
- Average Performers  
- Low Performers  

A clean and simple **Streamlit interface** displays the predicted segment for user inputs.

---

## **Objectives**
- Segment employees using the KNN algorithm  
- Build an interactive Streamlit app  
- Present employee categories in a clean, understandable format  
- Support HR decision-making and analytics  

---

## **Algorithm Used: KNN**
KNN clusters employees by comparing similarities in:
- Age  
- Salary  
- Projects Completed  
- Productivity (%)  

It is a simple yet powerful algorithm for segmentation tasks.

---


## **Technologies Used**

-Python

-Pandas

-NumPy

-Scikit-Learn

-Streamlit

-Joblib / Pickle

---

 ## **How to Run the Project**


1️⃣ Install Dependencies

pip install -r requirements.txt


2️⃣ Run the Streamlit App

streamlit run streamlit_app.py


3️⃣ Use the App

Enter the following details:

Age

Salary

Projects Completed

Productivity (%)

You will receive a predicted Employee Segment such as:

Cluster 0 → High Performer

Cluster 1 → Average Performer

Cluster 2 → Low Performer

(Cluster names depend on the model’s interpretation.)


---
 
 ## **Output**


The app displays:

Employee Cluster Number

Human-readable segment meaning

Clean, simple interface for HR usage

---


## **KNN Segmentation Logic**


The algorithm finds the k closest employees

Uses their cluster labels

Assigns the most frequent cluster to the new employee


requirements.txt

pandas

numpy

scikit-learn

streamlit

joblib

---

 ## **Use Cases**

HR performance analysis

Workforce planning

Employee behavior understanding

KPI-based segmentation

Identifying training needs

---

## **Conclusion**

This Employee Segmentation project offers a practical and easy-to-use Streamlit interface combined with KNN clustering to categorize employees effectively.
It is ideal for HR teams and data science learners who want to understand segmentation techniques in real business environments.
