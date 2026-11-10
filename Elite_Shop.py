import shutil
from turtle import width

import numpy
import time

in_ ="◈---- SERA sing in ----◈\n"
out_ = "◈---- SERA sing out ----◈\n"
in_Elite = {
    "USER Detail": 1,
    "Start Shoping": 2,
    "HELP": 3,
    "EXIT": 4
}

balence = 10000


in_shop = "✦---- SHOP ----✦"
Shop = {
    "Daily Use Item": "[1]",
    "Food Items": "[2]",
    "Electric Accessories":"[3]",
    "Songs": "[4]",
    "Black Market":"[5]",
    "Checkout":"[6]",
    "Exit":"[0]"
}

Daily_Use_Items = {
    "1.Premium Newspaper": "35",
    "2.Parker Luxury Pen": "450",
    "3.Oral-B Electric Toothbrush": "1200",
    "4.Luxury Fragrance Soap": "180",
    "5.Swiss Premium Toothpaste": "350",
    "6.Designer Match Box": "25",
    "7.Skybags Premium Travel Bag": "4500",
    "8.Premium Stationery Eraser": "30",
    "9.Metallic Luxury Pencil": "120",
    "10.Wooden Luxury Comb": "250",
    "11.Organic Shampoo Sachet": "15",
    "Checkout": "[12]",
    "Exit": "[0]"
}

Food_Items = {
    "1.Imported Almond Milk": "180",
    "2.Artisan Sourdough Bread": "250",
    "3.Organic Farm Eggs": "120",
    "4.Greek Yogurt": "180",
    "5.Imported Korean Noodles": "180",
    "6.Premium Fresh Fruit Juice": "150",
    "7.New Zealand Premium Butter": "350",
    "8.Evian Mineral Water": "250",
    "9.Acqua Panna Natural Water": "300",
    "10.Premium Himalayan Pink Salt": "180",
    "Checkout": "[11]",
    "Exit": "[0]"
}

Electric_Accessories = {
    "1.Philips Smart LED Bulb": "450",
    "2.Premium Designer LED Holder": "180",
    "3.Schneider Electric Smart Switch": "850",
    "4.Premium Modular Plug": "250",
    "5.Schneider Modular Socket": "350",
    "6.3M Electrical Insulation Tape": "180",
    "7.Premium Copper Wire Connector": "120",
    "8.Siemens Safety Fuse": "250",
    "9.Philips Designer Night Lamp": "1500",
    "10.Premium Smart Extension Board": "1800",
    "Checkout": "[12]",
    "Exit": "[0]"
}



shoping = True
cart = []
def daily_use_items():
    global shoping

    print("✦---- Daily Use Items ----✦")
    for item, price in Daily_Use_Items.items():
        print(f"{item}: {price} Rs")
        time.sleep(0.67)

    price = numpy.array("35, 450, 1200, 180, 350, 25, 4500, 30, 120, 250, 15".split(",")).astype(int)
    while shoping:
        time.sleep(1)
        try:
            choise = int(input("\nEnter the number of the item you want to buy: "))
        except ValueError as ERROR:
            print("\nInvalid input. Please enter a number.")
            continue

        if choise == 1:
            cart.append(price[0])
        elif choise == 2:
            cart.append(price[1])
        elif choise == 3:
            cart.append(price[2])
        elif choise == 4:
            cart.append(price[3])
        elif choise == 5:
            cart.append(price[4])
        elif choise == 6:
            cart.append(price[5])
        elif choise == 7:
            cart.append(price[6])
        elif choise == 8:
            cart.append(price[7])
        elif choise == 9:
            cart.append(price[8])
        elif choise == 10:
            cart.append(price[9])
        elif choise == 11:
            cart.append(price[10])
        elif choise == 12:
            checkout()
        elif choise == 0:
            print("\nExiting the shop.")
            shoping = False
            shop()            
        elif choise == "00":
            in_Elite()
        else: print("\nInvalid choice. Please try again.")




def food_items():
    global shoping

    print("✦---- Food Items ----✦")
    for item, price in Food_Items.items():
        print(f"{item}: {price} Rs")
        time.sleep(0.67)
    price = numpy.array("180, 250, 120, 180, 180, 150, 350, 250, 300, 180".split(",")).astype(int)
    while shoping:
        try:
            choise = int(input("\nEnter the number of the item you want to buy: "))
        except ValueError as ERROR:
            print("\nInvalid input. Please enter a number.")
            continue

        if choise == 1:
            cart.append(price[0])
        elif choise == 2:
            cart.append(price[1])
        elif choise == 3:
            cart.append(price[2])
        elif choise == 4:
            cart.append(price[3])
        elif choise == 5:
            cart.append(price[4])
        elif choise == 6:
            cart.append(price[5])
        elif choise == 7:
            cart.append(price[6])
        elif choise == 8:  
            cart.append(price[7])
        elif choise == 9:
            cart.append(price[8])
        elif choise == 10:
            cart.append(price[9])
        elif choise == 11:
            checkout()
        elif choise == 0:
            print("Exiting the shop.")
            shoping = False
            shop()
        elif choise == "00":
            in_Elite()
        else: print("Invalid choice. Please try again.")

def electric_accesories():
    for item, price in Electric_Accessories.items():
        print(f"{item}: {price} Rs")
        time.sleep(1)

    price = numpy.array("450, 180, 850, 250, 350, 180, 120, 250, 1500, 1800".split(",")).astype(int)
    while shoping:
        try:
            choise = int(input("Enter the number of the item you want to buy: "))
        except ValueError as ERROR:
            print("Invalid input. Please enter a number.")
            continue

        if choise == 1:
            cart.append(price[0])
        elif choise == 2:
            cart.append(price[1])
        elif choise == 3:
            cart.append(price[2])
        elif choise == 4:
            cart.append(price[3])
        elif choise == 5:
            cart.append(price[4])
        elif choise == 6:
            cart.append(price[5])
        elif choise == 7:
            cart.append(price[6])
        elif choise == 8:
            cart.append(price[7])
        elif choise == 9:
            cart.append(price[8])
        elif choise == 10:
            cart.append(price[9])
        elif choise == 11:
            checkout()
        elif choise == 0:
            print("Exiting the shop.")
            shoping = False
            shop()
        elif choise == "00":
            in_Elite()
        else: print("Invalid choice. Please try again.")

def shop():
    global shoping
    print(in_shop)
    for item, number in Shop.items():
        print(f"{number}: {item}")
        time.sleep(.67)
    while shoping:
        try:
            choise = int(input("\nEnter the number of the category you want to shop from: "))
        except ValueError as ERROR:
            print("\nInvalid input. Please enter a number.")
            continue

        if choise == 1:
            daily_use_items()
        elif choise == 2:
            food_items()
        elif choise == 3:
            electric_accesories()
        elif choise == 4:
            print("\nSongs section is under construction.")
        elif choise == 5:
            print("\nBlack Market section is under construction.")
        elif choise == 0:
            print("Exiting the shop.")
            shoping = False
            break
        else: print("\nInvalid choice. Please try again.")

def in_ELITE():
    time.sleep(1)
    print(in_)
    time.sleep(1)
    user_name = input("Enter your name: ")
    with open("store_data.txt", "w") as file:
        file.write(f"user_name = {user_name}\n")
    print(f"Welcome, {user_name}!")
    for item, number in in_Elite.items():
        print(f"{number}: {item}")
        time.sleep(1)
    while True:
        try:
            choise = int(input("\nEnter the number of the option you want to select: "))
        except ValueError as ERROR:
            print("Invalid input. Please enter a number.")
            return
        if choise == 1:
            print(f"User Detail: {user_name}")

        elif choise == 2:
            shop()
        elif choise == 3:
            print("HELP section is under construction.")
        elif choise == 4:
            print("Exiting the program.")
            time.sleep(1)
            print(out_)
            exit()


import random
import shutil

def card():
    global balence
    import random
    import shutil
    no = random.randint(1000, 9999)

    card = f"""
╔══════════════════════════════════════╗
║ ✦ PREMIUM BANK          ◈ SERA ◈     ║
║                                      ║
║  ▄▄▄▄▄                               ║
║  █ ░ █   4829 •••• •••• {no}         ║
║  ▀▀▀▀▀                               ║
║                                      ║
║  ❖ SERA ECONOMY          12/29       ║
║  ◈ CONTACTLESS )))       ✦ DEBIT     ║
╚══════════════════════════════════════╝
"""
    width = shutil.get_terminal_size().columns

    for line in card.strip().splitlines():
        print(line.rjust(width))
    time.sleep(3)
    print("\nPlease enter the last four digits of your card to proceed with the payment.")
    card = True
    while card:
        try:
            choise = int(input("\nEnter the last four digits of your card: "))
        except ValueError as ERROR:
            print("\nInvalid input. Please enter a number.")
            continue
        if choise == int(no):
            total = sum(cart)
            if total > balence:
                time.sleep(3)
                print("\nInsufficient balance. Please remove some items from your cart.")
            elif total <= balence:
                time.sleep(3)
                balence -= total
                print(f"Total amount: {total} Rs\n")
                print(f"Remaining balance: {balence} Rs")
                time.sleep(3)
                shop()
                card = False
                break
                
            else:
                print("\npayment failed. Please try again.")
                break
        else: 
            print("\nInvalid card number. Please try again.")

def checkout():
    print("[1]:Card \n[2]:Cash")
    checkout = True
    while checkout:
        try:
            choise = int(input("\nEnter the payment method:"))
        except ValueError as ERROR:
            print("\nInvalid choise, ples try again")
        if choise == 1:
            time.sleep(3)
            card()
            checkout = False
        elif choise == 2:
            time.sleep(3)
            cash()
            checkout = False
        else:print("Invalid")

def cash():
    cost = sum(cart)
    if balence >= cost:
        balence -= cost
        print(f"Total amount: {cost} Rs\n")
        print(f"Remaining balance: {balence} Rs")
        time.sleep(3)
        shop()
    else:
        print("\nInsufficient balance. Please add more funds.")
        shop()

in_ELITE()