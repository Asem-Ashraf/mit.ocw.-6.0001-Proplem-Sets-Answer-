annual_salary = float (input("Enter your annual salary: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_saved = float(input("Enter the percent of your salary to save, as a percentage: "))
semi_annual_raise = float (input("Enter the semi­annual raise, as a percentage: "))
portion_down_payment = total_cost/4.0
current_savings = 0.0
month_count = 0
while current_savings < portion_down_payment :
    current_savings = current_savings*4/1200.0 + annual_salary*portion_saved/1200.0 + current_savings
    month_count = month_count + 1
    if (month_count%6)==0.0 :
        annual_salary =  annual_salary*(1+semi_annual_raise/100)
print("Number of months: ",month_count)
