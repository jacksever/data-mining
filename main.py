import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Read dataset from CSV-file
df = pd.read_csv('./Real estate.csv')
print(df)

# Number of columns and rows
print(df.shape)

# Information about rows and columns
print(df.info())

# Data correlation
corrData = df.corr()
print(corrData)

# Displaying visually correlative data
sns.heatmap(corrData, annot=True)
plt.show()

# Displaying the dependence of each column on each row
sns.pairplot(df)
plt.show()
