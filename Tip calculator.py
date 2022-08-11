#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill=float(input("What wa the total bill? $"))
tip=int(input("What percentage tip would you like to give?10,12 or 15? "))
split=int(input("How many people to split the bill? "))
percent=(tip/100)
total_bill=(bill+percent*bill)/split
final_ans="{:.2f}".format(total_bill)
print("Each person should pay: $"+final_ans)
