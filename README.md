🛒 Big Mart Sales Prediction – Data Science Project

<img width="1280" height="604" alt="image" src="https://github.com/user-attachments/assets/64cb047b-ba3b-476b-a898-b4b1ca78dbce" />
<img width="1280" height="619" alt="image" src="https://github.com/user-attachments/assets/9240c767-bbca-48da-aee8-23fcb2fe25d4" />

📌 Project Overview

Big Mart Sales Prediction is a machine learning project that aims to predict the sales of products across different Big Mart outlets using historical sales data. The project applies data preprocessing, exploratory data analysis (EDA), feature engineering, and regression models to build an accurate prediction system.

This project demonstrates end-to-end data science workflow and is suitable for showcasing on resumes and GitHub portfolios.

🎯 Problem Statement

Big Mart wants to understand which products sell better and why.
The goal is to predict the sales (Item_Outlet_Sales) based on product and outlet characteristics such as:

Item type

Item visibility

Item MRP

Outlet size and location

Outlet type

📂 Dataset Description

The dataset contains sales data for 1559 products across 10 outlets.

🔑 Key Features
Feature	Description
Item_Identifier	Unique product ID
Item_Weight	Weight of the product
Item_Fat_Content	Fat content (Low Fat / Regular)
Item_Visibility	Visibility of the product
Item_Type	Category of the product
Item_MRP	Maximum Retail Price
Outlet_Identifier	Unique outlet ID
Outlet_Establishment_Year	Year outlet was established
Outlet_Size	Size of the outlet
Outlet_Location_Type	City tier
Outlet_Type	Type of outlet
Item_Outlet_Sales	Target variable (Sales)
🛠️ Technologies & Tools Used

Programming Language: Python

Libraries:

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

IDE / Tools: Jupyter Notebook / VS Code

🔍 Project Workflow

Data Loading & Understanding

Data Cleaning

Handling missing values

Correcting inconsistent categories

Exploratory Data Analysis (EDA)

Sales distribution

Feature relationships

Feature Engineering

Encoding categorical variables

Creating new meaningful features

Model Building

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Model Evaluation

R² Score

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Prediction on Test Data

📊 Model Performance
Model	R² Score
Linear Regression	Good baseline
Decision Tree	Improved performance
Random Forest	Best performance

🔥 Random Forest Regressor produced the highest accuracy and lowest error.

📈 Results & Insights

Item MRP has the highest impact on sales

Supermarket Type 3 outlets generate maximum revenue

Outlet age does not significantly affect sales

Feature engineering improved model performance


📌 Future Enhancements

Hyperparameter tuning

XGBoost / Gradient Boosting models

Model deployment using Flask or Streamlit

Real-time sales prediction dashboard

👨‍💻 Author

Shridhar Patil
🎓 Computer Science Engineer
📊 Data Science & Machine Learning Enthusiast

⭐ Acknowledgment

Dataset inspired by the Big Mart Sales Prediction problem commonly used in data science competitions and practice projects.
