#Write a program in Python to create a Billing system at Supermarket

while True:
    name = input("Enter customer's name : ")
    total =0
    product = input("Enter product's name : ")
    amount = float(input("Enter the amount : "))
    quantity = float(input("Enter the quantity : "))
    total += amount * quantity

    while True:
        repeat = input("Do you want to add more items? (y/n) : ")
        if repeat == "n" or repeat == "N":
            break
        if repeat == "y" or repeat == "Y":
            product = input("Enter product's name : ")
            amount = float(input("Enter the amount : "))
            quantity = float(input("Enter the quantity : "))
            total += amount * quantity
        else:
            print("Please enter a valid input")

    print("-"*40)
    print("Customer Name : ", name)
    print("Product Name : ", product)
    print("Amount to be paid : ", total)
    print("-"*40)
    print("********** THANK YOU **********")
    print("************** PLEASE VISIT AGAIN **************")
    Repeat1 = input("Do you want to go to the next customer? (y/n) : ")
    if Repeat1 == "n" or Repeat1 == "N":
        break