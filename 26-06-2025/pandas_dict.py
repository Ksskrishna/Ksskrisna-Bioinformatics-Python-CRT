import pandas as pd
calories = {"day1":500,"day2":600,"day3":700}
#prints all values
var = pd.Series(calories)
#prints onlu index specified values
var = pd.Series(calories,index=["day1","day2"])
print(var)