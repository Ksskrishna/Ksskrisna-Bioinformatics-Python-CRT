str = "KRISHNA"
n = len(str)
half = n // 2

for i in range(n):
    for j in range(n):
        if i == half or j == half:
            print(str[j], end=" ")
        else:
            print("  ", end="")
    print()