money_needed = float(input())
pocket_money = float(input())
days_counter = 0
spend_counter = 0
while pocket_money < money_needed and spend_counter < 5:
    action = input()
    action_money = float(input())
    if action == "save":
        pocket_money += action_money
        spend_counter = 0

    elif action == "spend":
        pocket_money -= action_money
        spend_counter +=1
        if pocket_money < 0:
            pocket_money = 0

    days_counter += 1
    if spend_counter == 5:
        print("You can't save the money.")
        print(f"{days_counter}")
        break
    elif pocket_money >= money_needed and spend_counter < 5:
        print(f"You saved the money for {days_counter} days.")
