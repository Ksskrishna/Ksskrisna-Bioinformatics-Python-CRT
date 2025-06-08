#1.write a py program to display a menu of food items as list
#2.create a tuple of prises wrt food items list
#3.read input form user for ordering the food  including the quantity 
#   if it exists in the menu --confirm order
#   if it is not avaliable -- print order something else
#4.while billing, read phone N.o, feedback, read tip amount
#5.add 18% Gst to bill and print the bill if bill > 0

print("********************************MENU********************************")
print("Staters___________________________")
print("Prawns fry")
print("Chicken fry")
print("Mutton fry")
print("Apollo fish")
print("Main Course_______________________")
print("Biriyani")

food = ["Biriyani", "Prawns fry", "Chicken fry", "Mutton fry", "Apollo fish"]
prices = (10, 20, 30, 40, 50)
total = 0
order_size = int(input("How many items ypu want to order: "))
for i in range(order_size):
    query = input("enter the item you eant to order:")
    query_index = food.index(query)
    if query in food:
        print(f"{query} exists in the menu")
        print("your order is confirmed")
        gst = prices[query_index] * (18/100)
        price = prices[query_index] + gst
        print(f"*********Bill: {price}***********")
        total = total + price
    else:
        print(f"{query} is not there in the menu! order omething else")
print(f"total amount = {total}")
#write a python prog to declare a list of words and declare a tuple of words and map it to print the combined words