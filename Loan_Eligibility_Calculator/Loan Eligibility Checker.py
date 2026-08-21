#Loan Eligibility Checker

credit_score = int(input("Enter your credit score: "))
monthly_income = int(input("Enter your monthly income: "))
liabilities = int(input("Enter your total liabilities: "))

if credit_score >= 750 and monthly_income >= 50000 and liabilities < 20000:
    status = "Eligible"
elif 650 <= credit_score <= 749 and monthly_income >= 50000 and liabilities < 20000:
    status = "Conditionally Eligible"
else:
    status = "Rejected"

print(f"Your loan application is {status}")