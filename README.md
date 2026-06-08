# 🛒 Big Mart Sales Prediction

<div align="center">

# 📊 Predicting Product Sales Using Machine Learning

### End-to-End Data Science Project | Regression Analysis | Sales Forecasting

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

# 📸 Project Preview

<div align="center">

<img width="100%" src="https://github.com/user-attachments/assets/64cb047b-ba3b-476b-a898-b4b1ca78dbce">

<br><br>

<img width="100%" src="https://github.com/user-attachments/assets/9240c767-bbca-48da-aee8-23fcb2fe25d4">

</div>

---

# 🌟 Project Overview

Big Mart Sales Prediction is a Machine Learning Regression project that predicts product sales across various Big Mart outlets using historical sales data.

The project demonstrates a complete Data Science workflow including:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Model Building
      ↓
Model Evaluation
      ↓
Sales Prediction
```

The goal is to help Big Mart understand which products sell better and identify the factors influencing sales performance.

---

# 🎯 Problem Statement

Big Mart wants to answer important business questions such as:

- Which products generate the highest sales?
- Which outlet types perform best?
- How do product characteristics affect revenue?
- Can future sales be predicted accurately?

### Target Variable

```python
Item_Outlet_Sales
```

---

# 📂 Dataset Information

The dataset contains sales records for:

| Metric | Value |
|----------|----------|
| Products | 1559 |
| Outlets | 10 |
| Features | 12 |
| Target Variable | Item_Outlet_Sales |
| Problem Type | Regression |

---

# 📊 Dataset Features

| Feature | Description |
|----------|----------|
| Item_Identifier | Unique Product ID |
| Item_Weight | Weight of Product |
| Item_Fat_Content | Low Fat / Regular |
| Item_Visibility | Product Visibility |
| Item_Type | Product Category |
| Item_MRP | Maximum Retail Price |
| Outlet_Identifier | Unique Outlet ID |
| Outlet_Establishment_Year | Outlet Opening Year |
| Outlet_Size | Outlet Size |
| Outlet_Location_Type | City Tier |
| Outlet_Type | Outlet Category |
| Item_Outlet_Sales | Sales Amount (Target) |

---

# 🗂️ Repository Structure

```bash
Big-Mart-Sales-Prediction/
│
├── dataset/
│   ├── Train.csv
│   └── Test.csv
│
├── notebooks/
│   └── BigMart_Sales_Prediction.ipynb
│
├── data_cleaning/
│   ├── missing_values.py
│   ├── feature_engineering.py
│   └── preprocessing.py
│
├── models/
│   ├── linear_regression.py
│   ├── decision_tree.py
│   └── random_forest.py
│
├── screenshots/
│   ├── sales_distribution.png
│   ├── outlet_analysis.png
│   └── feature_importance.png
│
├── requirements.txt
│
└── README.md
```

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

### Missing Value Handling

| Feature | Method |
|----------|----------|
| Item_Weight | Mean Imputation |
| Outlet_Size | Mode Imputation |

### Category Standardization

```text
LF → Low Fat
low fat → Low Fat
reg → Regular
```

### Data Quality Checks

- Missing Value Analysis
- Duplicate Detection
- Category Standardization
- Data Type Validation

---

# 📈 Exploratory Data Analysis (EDA)

## Univariate Analysis

- Sales Distribution
- Product Visibility Distribution
- Item MRP Distribution

## Bivariate Analysis

- Sales vs Item Type
- Sales vs Outlet Type
- Sales vs Outlet Size

## Multivariate Analysis

- Correlation Matrix
- Feature Relationships
- Sales Impact Analysis

---

# 📊 Key Visualizations

## Sales Distribution

```python
sns.histplot(df['Item_Outlet_Sales'])
```

## Correlation Heatmap

```python
sns.heatmap(df.corr(), annot=True)
```

## Feature Importance

```python
Random Forest Feature Importance
```

---

# 🔥 Key Insights

### 📌 Item MRP Strongly Influences Sales

Products with higher MRP tend to generate higher sales revenue.

---

### 📌 Supermarket Type 3 Generates Maximum Revenue

This outlet type consistently outperforms others.

---

### 📌 Outlet Age Has Minimal Impact

Older stores do not necessarily produce higher sales.

---

### 📌 Feature Engineering Improved Accuracy

Derived features improved overall model performance.

---

# ⚙️ Feature Engineering

### Label Encoding

Applied on:

```python
Item_Fat_Content
Outlet_Size
```

### One-Hot Encoding

Applied on:

```python
Item_Type
Outlet_Type
Outlet_Location_Type
```

### New Feature Creation

```python
Outlet_Age
```

Formula:

```python
Outlet_Age = Current_Year - Outlet_Establishment_Year
```

---

# 🤖 Machine Learning Models

## Linear Regression

### Advantages

- Fast Training
- Easy Interpretation
- Baseline Performance

---

## Decision Tree Regressor

### Advantages

- Handles Nonlinearity
- Easy Visualization

---

## Random Forest Regressor

### Advantages

- Higher Accuracy
- Reduced Overfitting
- Better Generalization

---

# 📊 Model Performance

| Model | Performance |
|---------|---------|
| Linear Regression | Good Baseline |
| Decision Tree Regressor | Better |
| Random Forest Regressor | Best |

---

# 📏 Evaluation Metrics

### Mean Absolute Error (MAE)

Measures average prediction error.

### Mean Squared Error (MSE)

Measures squared prediction error.

### Root Mean Squared Error (RMSE)

Measures prediction accuracy.

### R² Score

Measures variance explained by the model.

---

# 🏆 Best Performing Model

## 🌟 Random Forest Regressor

### Why?

✅ Highest R² Score

✅ Lowest RMSE

✅ Better Generalization

✅ Handles Nonlinear Relationships

---

# 🛠️ Technologies Used

| Category | Tools |
|-----------|-----------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| IDE | Jupyter Notebook, VS Code |

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Big-Mart-Sales-Prediction.git
```

### Navigate to Project

```bash
cd Big-Mart-Sales-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```bash
BigMart_Sales_Prediction.ipynb
```

---

# 📌 Future Enhancements

### Model Improvements

- Hyperparameter Tuning
- XGBoost Regressor
- LightGBM
- Gradient Boosting

### Deployment

- Flask Web Application
- Streamlit Dashboard
- REST API Integration

### Analytics

- Interactive Power BI Dashboard
- Tableau Dashboard

---

# 📈 Business Value

This project helps businesses:

✔ Forecast future sales

✔ Improve inventory management

✔ Understand customer demand

✔ Optimize product placement

✔ Increase revenue through data-driven decisions

---

# 👨‍💻 Author

## Shridhar Patil

🎓 Computer Science Engineer

📊 Data Science & Machine Learning Enthusiast

📧 shridharpatil0513@gmail.com

🐙 GitHub: https://github.com/Shridharpatil1958

---

# ⭐ Support

If you found this project useful:

🌟 Star the repository

🍴 Fork the project

📢 Share it with others

---

<div align="center">

### 🚀 Turning Data into Business Insights

Made with ❤️ by Shridhar Patil

</div>
