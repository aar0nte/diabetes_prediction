import pandas as pd
import numpy as np
import seaborn as sns


data = pd.read_csv('C:/Users/Aaron/python/demo/data/diabetes.csv')

data.shape

data.info()

data.describe()

sns.pairplot(data = data, hue = 'Outcome', vars = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

data.isnull().sum()

# data = data.dropna()

data.columns

data.duplicated().sum()

data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].eq(0).sum()

data.drop('Insulin', axis=1, inplace=True) # inplace =True modifies the original DataFrame we can also use data = data.drop('Insulin', axis=1)

cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']

for col in cols_with_zero:
    median_value = data[col].median()
    data[col] = data[col].replace(0, median_value)

data[['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']].eq(0).sum()    


data.shape


a = 1 + 1