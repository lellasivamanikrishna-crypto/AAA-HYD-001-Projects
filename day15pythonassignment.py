base_price = 5000
seat_type = input("Enter your seat type: ").lower()
booking_days = int(input("Enter The Booking Days: "))
festival = input("Is Festival sesion Or Not: ").lower()== "True"
Age = int(input("Enter Your Age"))
if seat_type == "business":
    base *= 1.40 
elif seat_type == "premium":
    base *= 1.20
if booking_days >30:
    base *= 0.9
elif booking_days <7:
    base *= 1.25
if festival:
    base *= 1.20
if age > 60:
    base *= 0.85

print(base)
