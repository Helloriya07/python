rent=int(input("enter your monthly rent ="))
groceries=int(input("enter the groceries purchased amount ="))
milk=int(input("enter the milk purchased amount ="))
veg=int(input("enter the vegetable purchased amount ="))
elec=int(input("enter the electricity spent  ="))
charge=int(input("enter the charge per unit ="))
person=int(input("enter the number of person living in room ="))

total_bill = elec*charge;

amt = rent+groceries+milk+veg+total_bill/person

print("Amount that each person had to pay =",amt)