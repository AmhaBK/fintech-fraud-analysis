# Credit Risk Probability Model

This project develops a machine learning-based probability model to detect fraudulent financial transactions using two datasets:
1. **E-Commerce Fraud Dataset** (`fraud_dataset.csv`)
2. **Credit Card Transactions Dataset** (`creditcard.csv`)

The project is part of a credit scoring challenge, with the goal of improving fraud detection through robust preprocessing, model training, and evaluation.


### 1. Data Cleaning and Feature Engineering

- Removed identifiers like `user_id`, `transaction_id`.
- Encoded categorical columns (`device_type`, `browser`, `payment_method`, `entry_mode`) using label encoding.
- Dropped highly correlated features to reduce multicollinearity.

### 2. Handling Class Imbalance

- Applied **SMOTE** on training data only (both datasets) to balance fraud (minority) and non-fraud (majority) transactions.
- Ensured **no SMOTE was applied to test sets** to maintain realistic fraud ratios for evaluation.

### 3. Train-Test Splitting

- Used `train_test_split()` with `stratify` to preserve class distribution in both train and test sets.

### 4. Scaling

- Fitted `StandardScaler` only on the balanced training set.
- Applied the same scaler to transform test data.

### 5. Saving Artifacts

Used `joblib` to save preprocessed datasets:
- For e-commerce fraud:
  - `X_train_bal.pkl`, `y_train_bal.pkl`
  - `X_test.pkl`, `y_test.pkl`
- For credit card fraud:
  - `Xc_train_bal.pkl`, `yc_train_bal.pkl`
  - `Xc_test.pkl`, `yc_test.pkl`

##  Upcoming Steps

- Train classification models: Logistic Regression, Random Forest, and XGBoost.
- Compare model performance using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC AUC Score
- Choose best model for fraud detection and deploy using a simple REST API.


## Notes & Best Practices

- Test sets remain **imbalanced** to simulate real-world data.
- SMOTE and scaling are only done **after splitting**, and **only on training data**.
- Saved preprocessed files allow seamless continuation of the project after restarting.

---

## Environment & Libraries

- Python 3.10+
- pandas
- scikit-learn
- imbalanced-learn
- joblib
- xgboost
- matplotlib, seaborn (for EDA)

Install dependencies with:

```bash
pip install -r requirements.txt
