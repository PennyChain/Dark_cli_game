import random
import time

money = 10000
one_round = 1500
print(f"\nYour money: {money}\n")
print(f"Revolver loaded with one bullet.\nOne round costs {one_round}.\nGamble {one_round}?\n")

def roulette():
    chamber = random.randint(1, 6)

    print(f"New balance: {money}")

    alive = True

    while alive:
        choice = input("").lower()
        if choice == "yes":
            money - one_round
            if chamber == random.randint(1, 6):
                print("You're dead.\n")
                break
            else:
                print("You survived.\n")
                money = money + one_round * 1.3
                time.sleep(0.5)
                roulette()
                break
        elif choice == "no":
            print("You take your earning and leave.\n")
            alive = False
        else:
            print("Invalid input. Type 'yes' or 'no'.\n")
            roulette()
            break

roulette()

