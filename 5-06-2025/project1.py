'''
write a py prog to 
1. Add confirmed guest list to a list
2. Remove guests who cancels
3. Check if guest is on the list
4. Sort and print the final guest list
'''
guest_list=[]
while(True):
    print("______________--MENU--______________")
    print("1. Add the guest list")
    print("2. Remove the Guests who cancels")
    print("3. Check if guest is on the list")
    print("4. sort and print the final list")
    print("5. Exit")
    print("____________________________________")
    choice = int(input("Enter your choice: "))
    if(choice>=1 and choice<=5):
        if(choice==1):
            guest_name = input("Enter the guest names: ")
            guest_list.append(guest_name)
            print(f"{guest_name} is added to Guest list")
        elif(choice==2):
            cancelled_guest = input("Enter the guest name you want to remove: ")
            if cancelled_guest in guest_list:
                guest_list.remove(cancelled_guest)
                print(f"{cancelled_guest} is removed from the guest list")
            else:
                print(f"{cancelled_guest} is not in guest list")
        elif(choice==3):
            check_guest = input("Enter the guest name to check: ")
            if check_guest in guest_list:
                print(f"{check_guest} is attending the party")
            else:
                print(f"{check_guest} is not attending the party")
        elif(choice==4):
            if(len(guest_list)==0):
                print("The guest list is empty")
            else:
                guest_list.sort()
                print("this is your final guest list")
                print(guest_list)
        else:
            print("Enjoy Your party")
            break
    else:
        print("Invalid Input")

