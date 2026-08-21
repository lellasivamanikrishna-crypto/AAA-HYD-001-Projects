#Vehicle Insurance Price Calculator

price = 10000

age = int(input("Enter your age: "))
health_score = int(input("Enter your vehicle health score: "))
vehicle_type = input("Enter your vehicle type (Sport, SUV, Sedan): ").lower()

if age <= 25:
    price *= 1.20
elif age > 50:
    price *= 1.15

if vehicle_type == "sport":
    price *= 1.30
elif vehicle_type == "suv":
    price *= 1.15

if health_score >= 80:
    price *= 0.90
elif health_score <= 60:
    price *= 1.20

print("Final Insurance Price:", price)