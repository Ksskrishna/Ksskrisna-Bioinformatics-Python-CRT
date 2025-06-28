def dates(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            l1 = list[j].split('-')
            l2 = list[j+1].split('-')
            day1 = int(l1[0])
            month1 = int(l1[1])
            year1 = int(l1[2])
            day2 = int(l2[0])
            month2 = int(l2[1])
            year2 = int(l2[2])
            if (month1>=1 and month1<=12) and (month2>=1 and month2<=12):
                if day1 in range(1,32) and day2 in range(1,32):
                    if (year1 > year2) or (year1 == year2 and month1 > month2) or (year1 == year2 and month1 == month2 and day1 > day2): 
                        list[j], list[j+1] = list[j+1], list[j]
                else:
                    print ("invalid days")
            else:
                print("invalid months")
    print(f"sorted dates:{list}")
list = ["27-15-2025", "01-01-2024", "15-03-2023", "05-12-2024"]
dates(list)