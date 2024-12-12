import random
import time
import os

one_round = 1500
balance_file = "balance_roulette.txt"

def load_balance():
    if os.path.exists(balance_file):
        with open(balance_file, "r") as file:
            content = file.read().strip()
            if content:
                try:
                    return float(content)
                except ValueError:
                    print("Invalid data in balance file. Resetting balance to 10,000.")
                    return 10000
    return 10000

def save_balance(money):
    with open(balance_file, "w") as file:
        file.write(f"{money:.2f}")

money = load_balance()
print(f"\nYour money: {money}\n")
print(f"Revolver loaded with one bullet.\nA game costs {one_round}.\nGamble {one_round}?\n")

def add_to_money(money):
    money = ((money * 1.0187) + (one_round * 1.3))
    return money

def sub_to_money(money):
    money = money - one_round * 3.3
    return money

def roulette():
    chamber = random.randint(1, 6)

    global money

    if money < one_round:
        print("Broke ahh")
        return

    money -= one_round

    while money >= one_round:
        choice = input("Do you want to play? (yes/no):\n\n").strip().lower()
        if choice == "yes":
            if random.randint(1, 6) == chamber:
                money = sub_to_money(money)
                print(f"You lost: {one_round * 5.3:.2f}\n")
                print(f"New balance: {money:.2f}\n")
            else:
                money = add_to_money(money)
                print("You survived.\n")
                print(f"New balance: {money:.2f}\n")
                time.sleep(0.5)
        elif choice == "no":
            print("You take your earning and leave.\n")
            print(f"Final balance: {money:.2f}\n")
            break
        else:
            print("Invalid input. Type 'yes' or 'no'.\n")

    save_balance(money)

roulette()