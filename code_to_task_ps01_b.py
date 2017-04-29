annual_salary = float(input("Enter the starting annual salary: "))
portion_saved = float(input("Enter the percentage of salary to be saved: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual salary raise: "))

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

number_of_months = i 
print ("Number of months:", number_of_months)