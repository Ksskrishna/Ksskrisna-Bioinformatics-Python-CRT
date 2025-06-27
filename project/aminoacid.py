import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
'''
problem: Given protein sequences, compute the
amino acid composition and display it as a pie chart
'''

#------< data
data = {
    "ProteinID": [f"P{i}" for i in range(1, 13)],
    "Sequence": [
        "MAGDTPLKNQV", "AAAGGTTCCSS", "MLVITGVAGGL", "WQQVVSSGGA",
        "FFTLLVVAAK", "GGGGSSSAAA", "CCDDDEEEFF", "MMNNPPQQRR",
        "KKTTSSTTGG", "VVVVAAAAFFF", "LLLIIIHHHHH", "SSSTTTGGGAA"
    ]
}
df = pd.DataFrame(data)
all_Seq = "".join(df["Sequence"])
counts = Counter(all_Seq)
labels, sizes = zip(*sorted(counts.items()))


camp=plt.colormaps.get_camp("tab20")
colors=[camp(i)for i in range(len(labels))]
plt.figure(figsize=(9,9))
wedges,_,autotexts=plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    explore=[0.5]*len(labels),
    startangle=140,
    autopct=lambda pct:f"{pct:.1f}%\n({int(pct/100*sum(sizes))})",
    textprops=dict(color="blck", fontsize=10)
)
plt.legend(
    wedges,
    [f"{aa}:{cnt}"for aa,cnt in counts.items()],
    title="Amino Acid (Count)",
    bbox_to_anchor=(1, 0.5),
    loc="center left",
    fontsize=9
)
plt.title("Amino.Acid Composition from 12 Protiens",
          fontsize=14,fontweight="bold",color="darkblue")
plt.tight_layout()
plt.show()