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
    'num100': 0,
    'numOrange': 0,
    'numApple': 0,
    'numCoke':0,
    'numSprites': 0
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
    1. 100 Plus
    2. Orange Juice
    3. Apple Juice
    4. CocaCola
    5. Sprite\n""")

def getmenuoptions():
    menuoptions = (input("Please enter your options: "))
    return menuoptions

def getdrinkoptions():
    drinkoptions = (input("Please enter your options: "))
    return drinkoptions

def getamount(number):
    amount = int(input("Please enter desired amount: "))
    if number=="1":
        cart['num100']+= amount
        print("Number of 100Plus: ", cart['num100'])
    elif number=="2":
        cart['numOrange'] += amount
        print("Number of Orange Juice: ", cart['numOrange'])
    elif number =="3":
        cart['numApple'] += amount
        print("Number of Apple Juice: ", cart['numApple'])
        
    elif number == "4":
        cart['numCoke'] += amount
        print("Number of CocaCola: ", cart['numCoke'])
        
    elif number == "5":
        cart['numSprites'] += amount
        print("Number of Sprite: ", cart['numSprites'])
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
    sum = cart['num100']*prices['price100'] + cart['numOrange']*prices['priceOrange'] + cart['numApple']*prices['priceApple'] + cart['numCoke']*prices['priceCoke'] + cart['numSprites']*prices['priceSprite']
    print("Total: RM",sum)
    return sum

def getpayment():
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
            getpayment()
    else:
        print("Invalid Input...")
