price = 10000
Age = int(input("Enter Your Age"))
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
