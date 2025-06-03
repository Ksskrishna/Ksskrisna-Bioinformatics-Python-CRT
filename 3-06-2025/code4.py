#read amount as input from user and print the number of notes required in indian currency dimension
rupees = int(input())
amount_2000 = rupees % 2000
quo_2000 = rupees // 2000
amount_500 = amount_2000 % 500
quo_500 = amount_2000 // 500
amount_200 = amount_500 % 200
quo_200 = amount_500 // 200
amount_50 = amount_200 % 50
quo_50 = amount_200 // 50
amount_1 = amount_50 % 1
quo_1 = amount_50 // 1
print(quo_2000)
print(quo_500)
print(quo_200)
print(quo_50)
print(quo_1)