# Find best savings rate using bisection search

starting_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
down_payment = 0.25 * total_cost
annual_return = 0.04
semi_annual_raise = 0.07
months = 36

low = 0
high = 10000
steps = 0
best_rate = None

def savings_after_36(rate):
    current_savings = 0
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12

    for month in range(1, months + 1 ):
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_salary * rate

        if month % 6 == 0:
            annual_salary *= (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12

    return current_savings

#Check impossible case

if savings_after_36(1.0) < down_payment:
    print("It is not possible to pay the down payment in the years: ")
else:
    while low <= high:
        mid = (low + high) // 2
        rate = mid / 10000
        current = savings_after_36(rate)
        steps += 1

        if abs(current - down_payment) <= 100:
            best_rate = rate
            break
        elif current < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    if best_rate is not None:
        print("Best savings rate:", round(best_rate, 4))
        print("Steps in bisection search:", steps)
    else:
        print("Could not finds a suitable savings rate:")    

        