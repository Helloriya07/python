menu={
    'Pizza':60,
    'Pasta':80,
    'Burger':80,
    'Salad':50,
    'Coffee':120,
}
print("Welcome to Riya's Kitchen")
print("Pizza: Rs60\nPasta: Rs80\nBurger: Rs80\nSalad: Rs50\nCoffee: Rs120")

order_total=0

item1 =input("Enter the name of the item you want to order")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item{item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item2 = input("Enter the name of second item=")
    if item2 in menu:
        order_total += menu[item2]
    print(f"Your item{item2} has been added to your order")
else:
    print(f"Ordered item is not available yet")


print(f"The total amount of items is to pay {order_total}")    