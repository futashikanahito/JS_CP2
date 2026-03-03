# JS, 1st, Financial Calculator

# ----- PSUEDOCODE -----
# Create savings function
#   ask user for saving goal
#   ask for how often the user is contributing
#   ask the user how much they are contributing each time
#   calculate result and print it
# Create cic function
#   ask user their starting amount
#   ask user for their interest rate percent
#   ask user for time compounding
#   define cycle function
#       find the calculation for each year
#   call cycle function for every year
#   calculate result and print it
# Create budget function
#   ask user for number of budget categories
#   ask user for each category name
#   ask user for monthly income
#   ask user for percentage of each category
#   calculate result and print it
# Create sale_price function
#   ask user for cost of item
#   ask user for percent discount
#   calculate result and print it
# Create tip function
#   ask user for bill price
#   ask user for percent tip
#   calculate result and print it
# Create an infinite loop
#   ask user for calculator choice
#   call selected calculator function

# ----- CODE -----
def savings():
    print("Welcome to the Savings Goal Calculator")
    goal = input("What amount are you saving to: ").strip().strip("$")
    while True:
        try:
            goal = float(goal)
            break
        except:
            goal = input("That was not a valid option. Please try again\n").strip().strip("$")
    time = input("How often are you contributing?\n 1. Weekly\n 2. Monthly\n 3. Semiyearly\n 4. Yearly\n").strip()
    while time != "1" and time != "2" and time != "3" and time != "4":
        time = input("That was not a valid option. Please try again\n")
    deposit = input("How much are you contributing each time: ").strip().strip("$")
    while True:
        try:
            deposit = float(deposit)
            break
        except:
            deposit = input("That was not a valid option. Please try again\n").strip().strip("$")
    print("\033c", end="")
    result = 0
    count = 0 
    while count < goal:
        count += deposit
        result += 1 
    print(f"It will take ~{result:.2f} {"weeks" if time == "1" else "months" if time == "2" else "half-years" if time == "3" else "years"} to save ${goal:.2f}.")
def cic():
    print("Welcome to the Compound Interest Calculator")
    starting = input("Starting Amount: ").strip().strip("$")
    while True:
        try:
            starting = float(starting)
            break
        except:
            starting = input("That was not a valid option. Please try again\n").strip().strip("$")
    interest = input("Interest Rate Percent: ").strip().strip("%")
    while True:
        try:
            interest = float(interest)
            break
        except:
            interest = input("That was not a valid option. Please try again\n").strip().strip("$")
    years = input("Years Spent compounding: ").strip()
    while True:
        try:
            years = int(years)
            break
        except:
            years = input("That was not a valid option. Please try again\n").strip()
    result = starting
    def cycle():
        nonlocal result
        result *= (1 + interest / 100) 
        return result
    for _ in range(years):
        result = cycle()
    print("\033c", end="")
    print(f"At the end of {years} years you will have ${result:.2f}")
def budget():
    print("Welcome to the Budget Allocator")
    num = input("How many budget categories do you have: ").strip()
    while True:
        try:
            num = int(num)
            break
        except:
            num = input("That was not a valid option. Please try again\n").strip()
    categories = []
    for i in range(num):
        categories.append(input(f"Category {i+1}: ").strip())
    income = input("What is your monthly income: ").strip().strip("$")
    while True:
        try:
            income = float(income)
            break
        except:
            income = input("That was not a valid option. Please try again\n").strip().strip("$")
    percentages = []
    for category in categories:
        percent = input(f"What percent is {category}: ").strip().strip("%")
        while True:
            try:
                percent = float(percent)
                break
            except:
                percent = input("That was not a valid option. Please try again\n").strip().strip("%")
        percentages.append(percent)
    collective = 0
    for i in percentages:
        collective += i
    print("\033c", end="")
    print(f"Your collective percentage is {collective:.2f}")
    if collective > 100:
        again = input("Your collective percentage is over 100. Are you sure you want to continue? (yes/retry) ")
        if again == "retry":
            print("\033c", end="")
            budget()
    for i in range(num):
        result = income * (percentages[i] / 100)
        print(f"{categories[i]} is {result:.2f}", end=", ")
        print()
def sale_price():
    print("Welcome to the Sale Price Calculator")
    cost = input("How much does the item originally cost: ").strip().strip("$")
    while True:
        try:
            cost = float(cost)
            break
        except:
            cost = input("That was not a valid option. Please try again\n").strip().strip("$")
    discount = input("What percent is the discount: ").strip().strip("%")
    while True:
        try:
            discount = float(discount)
            break
        except:
            discount = input("That was not a valid option. Please try again\n").strip().strip("%")
    print("\033c", end="")
    result = cost - (cost * (discount / 100))
    print(f"The item now costs ${result:.2f}")
def tip():
    print("Welcome to the Tip Calculator")
    bill = input("How much is the bill: ").strip().strip("$")
    while True:
        try:
            bill = float(bill)
            break
        except:
            bill = input("That was not a valid option. Please try again\n").strip().strip("$")
    tip = input("What percent of a tip are you giving: ").strip().strip("%")
    while True:
        try:
            tip = float(tip)
            break
        except:
            tip = input("That was not a valid option. Please try again\n").strip().strip("%")
    print("\033c", end="")
    result = bill + (bill * (tip / 100))
    print(f"With the original bill being ${bill:.2f}, and the {tip}% tip being ${(bill * (tip / 100)):.2f}, your total is now ${result:.2f}")

def main():
    while True:
        calc = input("Enter the number to select an option\n 1. Savings Time Calculator\n 2. Compound Interest Calculator\n 3. Budget Allocator\n 4. Sale Price Calculator\n 5. Tip Calculator\n 6. Exit\n")
        if calc == "6":
            print("\033c", end="")
            print("Thank you for using this program.")
            break
        while calc != "1" and calc != "2" and calc != "3" and calc != "4" and calc != "5":
            calc = input("That was not a valid option. Please try again\n")
        print("\033c", end="")
        if calc == "1":
            savings()
        elif calc == "2":
            cic()
        elif calc == "3":
            budget()
        elif calc == "4":
            sale_price()
        else:
            tip()
print("\033c", end="")
main()