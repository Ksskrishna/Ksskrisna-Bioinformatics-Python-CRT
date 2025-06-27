import pandas as pd
data = {
    'Std1':
    {
        'Name':'Krishna',
        'Branch':'Bioinfo',
        'ID': 14058,
        'skills':['Python','dsa','C']
    },
    'std2':
    {
        'Name':'Rohith',
        'Branch':'Radiology',
        'ID':2540,
        'skills':['Radiogtraphs','MRI']
    }
}
var = pd.Series(data,index=['Std1'])
print(var)
print(pd.Series(data))