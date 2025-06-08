#write a py prog to declare a list of grossery items and read the input from the user from 1 to 5
#1 to display items in a sorted way
#2. to take input from user and add items to the cart
#3. t0 view the cart items 
#4. to update the quantity or item present in the cart
#5. generate a bill including item names, item quantity, price and if the final bill amount is > 1000 the user will get 10% discount
    #if the user purchases any item more than 10kgs reduce the amount of 1kg from that particular items price
    #if the user purchases any particular items add buy 1 and get 1 offer to it.
    #add 25% gst to overall bill and print the bill.|||| after printing bill break

global_bill = 0
while True:
    print("\nSections:\n1. Groceries\n2. Essentials\n3. Exit")
    choice = int(input("Enter which section you want to enter: "))
    
    if(choice == 1):
        print("____________You are in Groceries Section____________")
        print("********************* Menu *********************")
        print("Rice, Dal, Sugar, Bellam, Ground-nut, Maida, Aata")
        groceries = ["Rice", "Dal", "Sugar", "Bellam", "Ground-nut", "Maida", "Aata"]
        groceries_prices = (10, 20, 50, 40, 45, 30, 50)
        cart = []
        total = 0
        num = int(input("Enter how many groceries: "))
        for i in range(num):
            query = input("Enter grocery item to cart: ")
            if query in groceries:
                query_index = groceries.index(query)
                print("Added to cart")
                cart.append(query)
                print(cart)
                quantity = int(input("Enter quantity in kgs: "))
                if(quantity > 10):
                    quantity = quantity-1
                bill = quantity * groceries_prices[query_index]
                print(f"The bill for {query} is: ₹{bill}")
                total += bill
                print(f"Total bill for groceries so far: ₹{total}")
            else:
                print(f"{query} is not available in store.")
        global_bill += total  

    elif(choice == 2):
        print("____________You are in Essentials Section____________")
        print("********************* Menu *********************")
        print("Tissue box, Maggie, Shampoo, Surf, soap, face cream, coffee powder")
        essentials = ["Tissue box", "Maggie", "Shampoo", "Surf", "soap", "face cream", "coffee powder"]
        essentials_prices = (10, 20, 50, 40, 45, 30, 50)
        cart = []
        essentials_total = 0
        num = int(input("Enter how many essentials: "))
        for i in range(num):
            query = input("Enter essential item to cart: ")
            if query in essentials:
                query_index = essentials.index(query)
                print("Added to cart")
                cart.append(query)
                print(cart)
                quantity = int(input("Enter quantity in numbers: "))
                bill = quantity * essentials_prices[query_index]
                print(f"The bill for {query} is: ₹{bill}")
                essentials_total += bill
                print(f"Total bill for essentials so far: ₹{essentials_total}")
            else:
                print(f"{query} is not available in store.")
        global_bill += essentials_total  
    
    elif(choice == 3):
        print("Thank you for shopping!")
        print(f"Your final total bill is ₹{global_bill}")
        break

    else:
        print("Section unavailable")

    continue_shopping = input("Do you want to shop in another section? (yes/no): ")
    if continue_shopping != "yes":
        print("Thank you for shopping with us!")
        print(f"\nSubtotal: ₹{global_bill}")

        if global_bill > 1000:
            discount_amount = global_bill * 0.10
            after_discount = global_bill - discount_amount
            gst_amount = after_discount * 0.25
            final_price = after_discount + gst_amount

            print(f"Discount (10%): ₹{discount_amount}")
            print(f"Price after discount: ₹{after_discount}")
            print(f"GST (25%): ₹{gst_amount}")
            print(f"Final price to pay: ₹{final_price}")
        else:
            print("No discount applied.")
            print(f"Final price to pay: ₹{global_bill}")
        break
