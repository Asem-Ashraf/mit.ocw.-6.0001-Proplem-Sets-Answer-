annual_salary = float (input("Enter your starting salary: "))
current_savings = 0
month_count = 0
steps = 0
high=1
low=0
guess = (high +low)/2.0
for month_count in range(1,37) :
        current_savings += annual_salary/12.0
        if month_count%6==0 :
             annual_salary *= 1.07
        if month_count%12==0 : 
            annual_salary *= 1.04
while abs(current_savings*guess - 250000) >= 100:
  if guess<1.0 :  
    if current_savings*guess<250000 :
       low = guess
    else :
       high = guess
    guess = (high +low)/2.0
    steps +=1
  else :
        print ("It is not possible to pay the down payment in three years.")
        break
else :
        print("Best savings rate: ", guess)
        print('Steps in bisection search:', steps)
