import pandas as pd
import csv
import numpy as np


csv_path = "C:/Users/y-zem/Desktop/HOMEWORK/homework3/budget_data.csv"
dfbudget= pd.read_csv(csv_path)
dfbudget.head()

# Title of the analysis
Title=("financial analysis")
Title


#Number of months
Total_Months= dfbudget.Date.count()
Total_Months

dollar='$'
dollar


#dfbudget.mean()
TTL= dfbudget["Profit/Losses"].sum()
TTL

Total = '$' + str(TTL)
Total

#df['otm'] = df.Value.diff()
OTM = dfbudget.TTL.diff(12)