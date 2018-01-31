#Alexandra Montgomery
#Quiz 1 - Question 1

# Get data
amount = float(input("Enter the amount of the loan: "))
rate = float(input("Enter the interest rate in percent form (%): "))
duration = float(input("Enter the duration of the loan: "))

# Tell user if the data is not good
if amount >= 5000 and rate > 0 and duration == 36 or 60:
    print("The data you've supplied is valid.")
else:
    print("The data you've supplied is invalid.")
# Calculate
r = rate / 12
monthly = (amount * r) / (1 - (1 + r) **(-1 * duration))
totalInterest = (duration * monthly) - amount

# Export
print("Monthly payment is: ${0:,.2f}".format(monthly))
print("Total interest paid: ${0:,.2f}".format(totalInterest))
