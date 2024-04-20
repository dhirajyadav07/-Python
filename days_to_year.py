days=int(input("Enter the number of days :"))
year=int(days/365)
remaining_days=days-year*365       # calculate the remaining days for calculating month
months=int(remaining_days/30)
remaining_days=remaining_days-months*30
day=remaining_days
print("%d years %d months %d days"%(year ,months ,day))

