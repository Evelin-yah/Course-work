destination = input()

while destination != "End":
    budget = float(input())
    saved = 0
    while budget > saved:
        money = float(input())
        saved += money
    print(f"Going to {destination}!")
    destination = input()