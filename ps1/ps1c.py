annual_salary = float (input("Enter your starting salary: "))
current_savings = 0.0
month_count = 0
earnings =0
while month_count <36 : # with for because it is better when the step is 6
    month_count = month_count + 1
    earnings = earnings + annual_salary/12
    if month_count%6==0 :
         annual_salary = annual_salary * 1.07
    if month_count%12==0 & month_count!=12 : 
        annual_salary = annual_salary * 1.04
    #print("earnings", earnings)
rate = 250000.0/earnings
if rate<1.0:
    print("Best savings rate: ", rate)
else : print ("It is not possible to pay the down payment in three years.")