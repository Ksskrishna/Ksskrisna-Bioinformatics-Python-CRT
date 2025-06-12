'''
Scenario based questions "Bioinformatics domain"
'''
string = input("enter the bases: ")
count_a = 0
count_t = 0
count_g = 0
count_c = 0

for i in string:
    if i in "A":
        count_a = count_a + 1
    elif i in "T":
        count_t = count_t + 1
    elif i in "G":
        count_g = count_g + 1
    elif i in "C":
        count_c = count_c + 1

dict = {'A':count_a,'T':count_t,'G':count_g,'C':count_c}
print(dict)