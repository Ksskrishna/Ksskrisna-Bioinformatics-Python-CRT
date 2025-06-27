'''
write a py prog to count how many genes belong to each family from the given data 
and visualize it using bar chart
'''
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "GeneID": [f"G{i}" for i in range(1, 19)],
    "Family": [
        "Kinase", "Ligase", "Kinase", "Polymerase", "Kinase", "Ligase",
        "Transferase", "Kinase", "Transferase", "Polymerase", "Ligase",
        "Kinase", "Transferase", "Polymerase", "Ligase", "Kinase",
        "Transferase", "Kinase"
    ]
}

df = pd.DataFrame(data)

family_counts = df['Family'].value_counts()
print(family_counts)


plt.bar(family_counts.index, family_counts.values, color='blue')
plt.title('Gene Family Counts')
plt.xlabel('Family')
plt.ylabel('Number of Genes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()