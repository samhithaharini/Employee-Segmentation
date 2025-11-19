##Employee Segmentation using K-Nearest Neighbors (KNN)

This project performs Employee Segmentation using K-Nearest Neighbors (KNN) to group employees based on key performance metrics.
The output helps organizations understand employee categories such as High Performers, Average Performers, and Low Performers, enabling better decision-making in HR and workforce planning.


 Project Overview

Employee segmentation is an essential HR analytics task used to analyze employee behavior and performance patterns.


 In this project:

Employee data is preprocessed

Features are scaled

KNN clustering is applied

Each employee is assigned to a segment

A simple and clean Streamlit web app is used to predict and visualize segmentation



 Objectives


Segment employees using KNN algorithm

Build a clean and user-friendly Streamlit interface

Allow users to input employee metrics and get a predicted segment

Help organizations understand workforce distribution and performance trends


Machine Learning Algorithm: KNN


K-Nearest Neighbors is used for segmentation based on similarity between employees.

Employees closer in feature space are grouped into the same cluster.


 Why KNN?


Simple and effective

Non-parametric

Good for HR datasets with smaller dimensions

Easy to interpret outputs


 Features Used


Age

Salary

Projects Completed

Productivity (%)

These features help determine employee similarity for segmentation.


 Technologies Used

Python

Pandas

NumPy

Scikit-Learn

Streamlit

Joblib / Pickle



 How to Run the Project


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



 Output


The app displays:

Employee Cluster Number

Human-readable segment meaning

Clean, simple interface for HR usage


KNN Segmentation Logic


The algorithm finds the k closest employees

Uses their cluster labels

Assigns the most frequent cluster to the new employee


requirements.txt

pandas

numpy

scikit-learn

streamlit

joblib


 Use Cases

HR performance analysis

Workforce planning

Employee behavior understanding

KPI-based segmentation

Identifying training needs

 Conclusion

This Employee Segmentation project offers a practical and easy-to-use Streamlit interface combined with KNN clustering to categorize employees effectively.
It is ideal for HR teams and data science learners who want to understand segmentation techniques in real business environments.
