# You are tasked to code the vending machine logic out using Python Programming Language.
# In your code, you can have a few drinks as your items with any price (no coin).
# The customer should be able to insert any notes to buy his preferred drinks.
# The outcome is to release the least amount of notes back to the customer.

#------------------------------Variables---------------------------
prices = {
    'price100': 3,
    'priceOrange': 3,
    'priceApple': 4,
    'priceCoke': 3,
    'priceSprite': 3
}

cart = {
    'Number of 100Plus': 0,
    'Number of Orange Juice': 0,
    'Number of Apple Juice': 0,
    'Number of CocaCola':0,
    'Number of Sprite': 0
}

#------------------------------Functions---------------------------
def main_menu():
    print ("""
    0. Exit Vending Machine
    1. Select Drink.
    2. View Cart
    3. Proceed Payment\n""")

def drink_menu():
    print("""
    0. Exit to Main Menu
    1. 100 Plus - RM 3
    2. Orange Juice - RM 3
    3. Apple Juice - RM 4
    4. CocaCola - RM 3
    5. Sprite - RM 3\n""")

def getmenuoptions():
    menuoptions = (input("Please enter your options: "))
    return menuoptions

def getdrinkoptions():
    drinkoptions = (input("Please enter your options: "))
    return drinkoptions

def getamount(number):
    amount = int(input("Please enter desired amount: "))
    if number=="1":
        cart['Number of 100Plus']+= amount
        print("Number of 100Plus: ", cart['Number of 100Plus'])
    elif number=="2":
        cart['Number of Orange Juice'] += amount
        print("Number of Orange Juice: ", cart['Number of Orange Juice'])
    elif number =="3":
        cart['Number of Apple Juice'] += amount
        print("Number of Apple Juice: ", cart['Number of Apple Juice'])
        
    elif number == "4":
        cart['Number of CocaCola'] += amount
        print("Number of CocaCola: ", cart['Number of CocaCola'])
        
    elif number == "5":
        cart['Number of Sprite'] += amount
        print("Number of Sprite: ", cart['Number of Sprite'])
    else:
        print("Invalid Input.")

def displaycart(total):
    if(total==0):
        print("Cart is empty. Please select some drinks items")
    else:
        for drink, amount in cart.items():
            if amount > 0:
                print(f"{drink}: {amount}")

def getsum():
    sum = 0
    sum = cart['Number of 100Plus']*prices['price100'] + cart['Number of Orange Juice']*prices['priceOrange'] + cart['Number of Apple Juice']*prices['priceApple'] + cart['Number of CocaCola']*prices['priceCoke'] + cart['Number of Sprite']*prices['priceSprite']
    print("Total: RM",sum)
    return sum

def getpayment(sum):
    change = 0
    while True:
        payment = int(input("Please Payment Amount: RM "))
        if(payment<sum):
            print("Insufficient amount of payment...")
        else:
            change = payment - sum
            print("Payment Successful! Change: RM ", change)
            getchange(change)
            break
    
    return change

def getchange(change):
    notes = [50, 20, 10, 5, 1]
    change_notes = {}
    for i in notes:
        if change >= i:
            change_notes[i] = change // i
            change %= i

    print("Notes returned:")
    for a, b in change_notes.items():
        print(f"RM {a} : {b}")

    # Reset cart
    for drink in cart:
        cart[drink] = 0

#-----------------------------------------Main-------------------------------------------
while True:
    main_menu()
    a = getmenuoptions()
    if(a=="0"):
        print("Exiting Vending Machine...")
        break
    elif(a=="1"):
        while True:
            drink_menu()
            b = getdrinkoptions()
            if(b=="0"):
                print("\nExiting to Main Menu...")
                break
            elif(b=="1" or b=="2" or b=="3" or b=="4" or b=="5"):
                getamount(b)
            else:
                print("Invalid Input...")
    elif(a=="2"):
        total = getsum()
        displaycart(total)
    elif(a=="3"):
        total = getsum()
        displaycart(total)
        if(total != 0):
            getpayment(total)
    else:
        print("Invalid Input...")
