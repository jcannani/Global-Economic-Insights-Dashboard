import pandas as pd

# Load the dataset
df = pd.read_csv('bank_data.csv')

# Basic info
print(df.info())
print(df.head())

# Check missing values
missing = df.isnull().sum()
print(missing[missing > 0])

# Fill or drop missing values (choose wisely)
df_clean = df.dropna(subset=['GDP (Current USD)', 'Inflation (CPI %)', 'Unemployment Rate (%)'])
df_clean = df_clean.fillna(method='ffill')

# Save cleaned data
df_clean.to_csv('cleaned_bank_data.csv', index=False)
print('Cleaned data saved!')