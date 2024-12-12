money = 10000
one_round = 1500

def add_to_money(money):
    while True:
        input("Press Enter to add to money...")
        money = ((money * 1.0087) + (one_round * 1.3))
        print(f"{money:.2f}")
        if money >= 100000:
            return money
        
money = add_to_money(money)
print(f"You've reached you cap of {money:.2f}")
