'''
problem: Given DNA sequence, calculate the GC content of each and plot its histogram
'''
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "GeneID": [f"G{i}" for i in range(1, 16)],
    "Sequence": [
        "ATGCGTAA", "GGGCGCGT", "ATATATAT", "CGCGATAT",
        "GCGTGCAT", "TTATTATA", "CCGGCCGG", "GATCGATC",
        "TATATATA", "GCGCGCGC", "ATGCATGC", "GGATCCGG",
        "CATCATGG", "TGCATGCA", "GGTACCGA"
    ]
}
df = pd.DataFrame(data)

gc_contents = []
for seq in df['Sequence']:
    gc = 0
    for i in seq:
        if i == 'G' or i == 'C':
            gc += 1
    gc_percent = (gc / len(seq)) * 100
    gc_contents.append(gc_percent)

df['GC_Content'] = gc_contents
print(df[['GeneID', 'Sequence', 'GC_Content']])

plt.hist(df['GC_Content'], color='skyblue')
plt.title('GC Content Histogram')
plt.xlabel('GC Content (%)')
plt.ylabel('Frequency')
plt.show()