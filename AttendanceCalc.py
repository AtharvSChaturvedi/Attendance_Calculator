days=int(input("Total No. of Days: "))
present_days=int(input("No. of Present: "))

percentage_wanted=float(input("Percentage wanted: "))

current_percentage=(present_days/days)*100
days_required=0

if percentage_wanted >= 100:
    print("INVALID!")
elif current_percentage >= percentage_wanted:
    print("Already achieved")
else:
    while (present_days/days)*100 < percentage_wanted:
        present_days+=1
        days+=1
        days_required+=1

    print(f"{days_required} more days")
