import pandas as pd

#read csv file
d=pd.read_csv("customers.csv")

#how many customers are in the dataset?
print(d.shape)

#how many columns are there?
print(d.info())

#which columns contain missing values?
print(d.isnull().sum())

#are there duplicate rows?
print(d.duplicated().sum())

#whats the average age?
#whats the average monthly spending?
print(d.describe())

#whats the average satisfaction score?
print(d['satisfaction'].mean())

#who are the customers spending more than 500?
print(d[d['monthly_spending']>500])

#sort customers by monthly_spending from highest to lowest
print(d.sort_values('monthly_spending',ascending=False))