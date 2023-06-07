print("Welcome to the tip calculator")
total = input("What was the total bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill with? ")

totalperson = (float(total) * (int(tip_percentage)/100 + 1)) / int(people)

print(f"Each person should pay: ${round(totalperson, 2):.2f}") # :.2f adds two 0 after the decimal point last number until lenght of 2.