menu ={
    'pizza' : 80,
    'Pasta' : 120,
    'Coffee' : 50,
    'Burger' : 80,
    'Fries' : 70,
    'Sandwitch' : 60,
}


#greet
print("Welcome to the PYTHON Restaurant !!")
print("Pizza : 80 Rs \nPasta : 120 Rs\nCoffee : 50 Rs\nBurger : 80 Rs\nFries : 70 Rs\nSandwitch : 60 Rs")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1} has been added to your order ")

else:
    print(f"Ordered item {item_1} is not available yet !")

another_order =  input("Do you want to add another item (yes/no) : ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item you want to order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order ")

    else:
       print(f"Ordered item {item_2} is not available yet !")
        
print(f"Total Amount of items to pay is {order_total}")