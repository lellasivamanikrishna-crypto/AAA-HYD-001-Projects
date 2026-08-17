                                                      #Day 16/100
#Built Python Programs for Vehicle Insurance Premium & Loan Eligibility Evaluation Using Conditional Statements

price = 10000
Age = int(input("Enter Your Age: "))
Health = int(input("Enter your Vehicle Health Score: "))
Vehicle = input("Enter Your Vehicle Type(Sport,Suv,Sedan)").lower()
if Age <= 25:
    price *= 1.20 
elif Age > 50:
    price *= 1.15
if Vehicle == "Sport":
    price *= 1.30
elif Vehicle == "Suv":
    price *= 1.15
if Health >= 80:
    price -= 0.90
elif Health <= 60:
    price *= 1.20
print(price)


#Solved Real-World Python Problems with Decision-Making Logic: Insurance Premium Calculator & Loan Eligibility Checker

price = 10000
score = int(input("Enter Your Credit Score: "))
income = int(input("Enter your Monthly Income: "))
liabilities = int(input("Enter Your Liabilities Value: "))
approval = " "
if score >= 750 and income >= 50000 and liabilities < 20000:
    approval = "Eligible"
elif 650 <= score <=749 and income >= 50000 and liabilities < 20000:
    approval = "Conditionally Eligible"
else:
    approval = "Rejected"
print(f'Your Loan is {approval}')
