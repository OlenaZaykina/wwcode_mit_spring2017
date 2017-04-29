Annual_salary = float(input("Enter your annual salary: "))
Portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
Total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = Total_cost * 0.25

Monthly_salary = Annual_salary / 12

Every_monthly_payment = Monthly_salary * Portion_saved

annual_rate = 0.04
current_savings = 0
i = 0
while current_savings < portion_down_payment:
    Addition_current_savings = current_savings * annual_rate / 12
    current_savings += (Every_monthly_payment + Addition_current_savings)
    i += 1
    
Number_of_months = i 
print ("Number of months:", Number_of_months)