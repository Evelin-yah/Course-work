locations = int(input())

for location in range (locations):
    expected_av_gold_daily = float(input())
    days_for_location = int(input())
    location_gold = 0
    for day in range (days_for_location):
        daily_gold = float(input())
        location_gold += daily_gold
    av_gold = location_gold / days_for_location
    if av_gold >= expected_av_gold_daily:
        print(f"Good job! Average gold per day: {av_gold:.2f}.")

    if av_gold < expected_av_gold_daily:
        ttl = expected_av_gold_daily - av_gold
        print(f"You need {ttl:.2f} gold.")

