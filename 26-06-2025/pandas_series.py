'''
ETL --> extract tranform load
ELT --> extract load transform
'''
import pandas as pd
num = [10,20,30,40,50,60]
num_ser = pd.Series(num,index=["i","ii","iii","iv","v","vi"])
print(pd.Series(num_ser))