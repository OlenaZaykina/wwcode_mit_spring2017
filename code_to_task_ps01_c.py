annual_salary = float(input("Enter the starting annual salary: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual salary raise: "))
number_of_months = float(input("Enter the number of months to down payment: "))
monthly_salary = annual_salary / 12	

def calculate_needed_month(annual_salary, portion_saved, total_cost, 
                           semi_annual_raise, annual_rate):
    portion_down_payment = total_cost * 0.25

    monthly_salary = annual_salary / 12
    
    every_monthly_payment = monthly_salary * portion_saved
    annual_rate = 0.04
    current_savings = 0
    i = 0
    mounthly_increases = range (7, 100000, 6)
    
    while current_savings < portion_down_payment:
        i += 1
        if i in mounthly_increases:
            every_monthly_payment = every_monthly_payment * (1 + semi_annual_raise)
        addition_current_savings = current_savings * annual_rate / 12
        current_savings += (every_monthly_payment + addition_current_savings)
    
    return i

annual_rate = 0.04

current_portion_saved = 0.5

riched_condition = False
counter = 0
while not riched_condition:
    current_month = calculate_needed_month(annual_salary, current_portion_saved, 
                                           total_cost, semi_annual_raise, annual_rate)
    if current_month == number_of_months:
        riched_condition = True
        break
    elif current_month > number_of_months:
        current_portion_saved += current_portion_saved/2
    else:
        current_portion_saved -= current_portion_saved/2
    counter += 1
    if current_portion_saved > 1:
        break
if riched_condition:
    print (float(round(current_portion_saved, 4)))
    print (counter)
else:
    print ("It is not possible to pay the down payment in three years.")