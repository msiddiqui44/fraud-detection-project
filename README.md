# Fraud Detection Project
Detecting fraudulent transactions using machine learning on the IEEE-CIS Fraud Detection dataset. This project combines Python (Pandas, XGBoost, Scikit-learn), SQL, and Power BI to explore, analyze, and visualize fraudulent activity. It includes data preprocessing, feature engineering, model training, and interactive dashboards for insights.

Dataset
**Source**: https://www.kaggle.com/competitions/ieee-fraud-detection/data?select=test_identity.csv

## Data Cleaning & EDA

Merged train_transaction and train_identity on TransactionID
Dropped features with >90% missing values
Encoded key categorical variables
Saved cleaned dataset to data/processed/cleaned_data.csv

Explored fraud vs. non-fraud transaction patterns
Engineered features: TransactionHour, log_TransactionAmt, grouped email domains
Created visuals (distribution plots, comparison charts)
Saved findings in notebooks/01_eda.ipynb

## Modeling & Evaluation

Stratified train-validation split
Trained XGBoost with cross-validation and early stopping
Handled class imbalance via scale_pos_weight
Saved model to models/fraud_model.joblib

Generated prediction DataFrame (TransactionID, fraud score, binary label)
Evaluated using precision, recall, F1, confusion matrix, PR-AUC
Saved all results and rationale in notebooks/02_modeling.ipynb

## SQL Integration

Created local database with schema: fraud_scores (TransactionID, fraud_score, prediction, TransactionAmt, ...)
Inserted predictions using SQLAlchemy

Created views:
high_risk_users: Top risky card_id or email
daily_fraud_stats: Daily fraud rate summary
fraud_by_product: Fraud by ProductCD, browser, card4
Validated views via psql / SQLite GUI

## Power BI Dashboard

Connected Power BI to SQL DB
Imported all tables and views
Finalizing dashboard layout:
Daily fraud trends
Summary KPI card
High-risk transactions table
Fraud by product/browser
Filters by date, device, fraud score, and product



Made using PowerBI

**Created by:** Mustafa Siddiqui and Joshua Golconda
