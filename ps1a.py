# calcute the number of months required to save for down payment

annualsalary = float(input("Enter the annual salary: "))
portionsaved = float(input("enter portion saved: "))
totalcost = float(input("Enter cost of dream house: "))

portion_down_payment = 0.25
r = 0.04
current_savings = 0.0

monthly_salary =  annualsalary / 12
down_payment = totalcost * portion_down_payment
months = 0

while current_savings < down_payment:
    current_savings += current_savings * (r / 12)   #interest
    current_savings += monthly_salary * portionsaved   #saving
    months += 1

print("Number of months:", months)