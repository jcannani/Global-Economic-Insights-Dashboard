import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv('cleaned_bank_data.csv')

# Correlation map
corr = df[['GDP (Current USD)', 'Inflation (CPI %)', 'GDP Growth (% Annual)', 'Unemployment Rate (%)']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Economic Indicator Correlation')
plt.show()