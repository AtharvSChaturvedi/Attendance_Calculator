days = int(input("Total No. of Days: "))
present_days = int(input("No. of Present: "))

percentage_wanted = float(input("Percentage wanted: "))

current_percentage = (present_days / days) * 100
days_required = 0

if percentage_wanted > 100:
    print("Percentage cannot be greater than 100.")
elif current_percentage >= percentage_wanted:
    print("You already meet or exceed the desired percentage.")
else:
    while (present_days / days) * 100 < percentage_wanted:
        present_days += 1
        days += 1
        days_required += 1

    print(f"{days_required} more days")
