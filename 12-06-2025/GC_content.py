seq = input("enter the sequence: ")
g_count = 0
for i in range(len(seq)):
    if(seq[i]=="G" or seq[i]=="C"):
        g_count = g_count + 1
GC_count = (g_count/len(seq))*100
if(GC_count > 60):
    print(f"High GC content {GC_count}")
elif(GC_count <= 40):
    print(f"Low GC Content {GC_count}")
else:
    print(f"Moderate GC content {GC_count}")