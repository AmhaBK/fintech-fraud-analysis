# E-commerce Fraud Detection Project

This project focuses on building a robust fraud detection system for **Adey Innovations**, an e-commerce company.  
The primary goal is to minimize financial losses from fraudulent transactions while maintaining a seamless user experience.  

This repository contains the code and analysis for two distinct fraud detection tasks:  
1. Using a provided e-commerce dataset.  
2. Using an anonymized credit card dataset.



## 1. Project Structure

The project is organized into the following directories:

- **data/**: Contains the raw and processed datasets.  
  - **raw/**: The original `Fraud_Data.csv` and `IpAddress_to_Country.csv` files.  
  - **processed/**: Intermediate data files generated after cleaning, feature engineering, and encoding, stored in formats like `.csv` and `.pkl`.  

- **src/**: Contains custom Python modules for data preprocessing.  
  - **preprocessing/**: Modules for data cleaning, feature engineering, and transformation.  

- **notebooks/**: Jupyter notebooks detailing the full data analysis, model training, and evaluation pipelines for both datasets.  

- **reports/**: Contains the final project report summarizing the findings and recommendations.



## 2. E-commerce Fraud Detection

### 2.1. Overview
The primary dataset for this part of the project is `Fraud_Data.csv`.  
It contains information on e-commerce transactions, including user details, device information, and transaction timestamps.  
A separate `IpAddress_to_Country.csv` dataset was used to enrich the data with geographical information.

### 2.2. Key Steps

#### Data Preprocessing
- Extracted time-based features like `hour_of_day`, `day_of_week`, and `time_since_signup` from the `purchase_time` and `signup_time` columns.  
- Used the `ip_address` column to merge the data with `IpAddress_to_Country.csv` to add a **country** feature.  
- One-hot encoded categorical features such as `source`, `browser`, `sex`, `country`, `day_of_week`, and `hour_of_day`.  
- Scaled the processed data using a **StandardScaler**.

#### Class Imbalance Handling
- Original dataset had a significant imbalance:  
  - **Non-fraudulent transactions (Class 0)**: 136,961  
  - **Fraudulent transactions (Class 1)**: 14,151  
- Applied **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the training data.

#### Model Training & Evaluation
- Models trained: Logistic Regression, Random Forest, Gradient Boosting, and XGBoost.  
- Evaluation metrics for imbalanced data: **AUC-PR**, **Precision**, and **Confusion Matrix**.  
- **Gradient Boosting** was selected as the best model:  
  - AUC-PR: **0.62**  
  - Precision: ~**100%**  
  - Only 6 false positives.

#### Model Explainability
- Used **SHAP (SHapley Additive exPlanations)** to identify influential features.  
- Top predictors:  
  1. `time_since_signup`  
  2. `country_United States`  
  3. `browser_Chrome`



## 3. Credit Card Fraud Detection

This task used a publicly available, anonymized credit card fraud dataset.  
The main difference was that the features (`V1` to `V28`) were not human-readable.

- Followed the same modeling pipeline as the e-commerce dataset.  
- Performed SHAP analysis on the best-performing model.  
- **V14** was found to be the most impactful feature for fraud detection.  
  - Although its original meaning is unknown (due to PCA transformation), its importance shows the model’s ability to detect critical fraud patterns.



## 4. Getting Started

To run the project:

1. **Clone** this repository.  
2. **Install** required libraries:  
   ```bash
   pip install pandas numpy scikit-learn xgboost shap imblearn

3. Ensure your data files are in the data/raw/ directory.

4. Run the notebooks in notebooks/ in the specified order to reproduce the analysis and results.