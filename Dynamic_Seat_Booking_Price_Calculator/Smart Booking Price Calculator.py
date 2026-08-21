#Seat Booking Price Calculator 
base_price = 5000

seat_type = input("Enter your seat type: ").lower()
booking_days = int(input("Enter the number of booking days: "))
festival = input("Is it a festival season? (True/False): ").lower() == "true"
age = int(input("Enter your age: "))

final_price = base_price

if seat_type == "business":
    final_price *= 1.40
elif seat_type == "premium":
    final_price *= 1.20
if booking_days > 30:
    final_price *= 0.90
elif booking_days < 7:
    final_price *= 1.25
if festival:
    final_price *= 1.20
if age > 60:
    final_price *= 0.85
print("Final Price:", final_price)
