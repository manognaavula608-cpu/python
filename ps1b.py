annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual rase, as a decimal: "))

down_payment = 0.25 * total_cost
current_savings = 0
annual_return = 0.04

monthly_salary = annual_salary / 12
months = 0

while current_savings < down_payment:

    current_savings += current_savings * (annual_return / 12)

    current_savings += monthly_salary * portion_saved

    months += 1

    if months % 6 == 0:
        annual_salry *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12

prinntf("Number of months: ", months)       