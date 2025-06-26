import pandas as pd

# Load first 10,000 rows from train
df_train = pd.read_csv('data/raw/train_transaction.csv', nrows=10000)
df_train.to_csv('data/processed/train_transaction_sample.csv', index=False)

# Load first 10,000 rows from test
df_test = pd.read_csv('data/raw/test_transaction.csv', nrows=10000)
df_test.to_csv('data/processed/test_transaction_sample.csv', index=False)

print("✅ Sample files created successfully.")
