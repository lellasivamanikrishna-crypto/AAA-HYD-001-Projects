import datetime
import random

print("Welcome to MovieMate AI!")

name = input("Enter your name: ").title()

print("\nChoose a movie genre:")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Romance")

genre_choice = int(input("Enter your choice: "))

movies = {
    1: ["Spider-Man: Brand New Day", "The Odyssey", "Avengers: Doomsday"],
    2: ["Jathi Ratnalu", "F3", "DJ Tillu"],
    3: ["Virupaksha", "Arundhati", "Deyyam"],
    4: ["Sita Ramam", "Hit 3", "Hi Nanna"]
}

show_times = [
    "10:00 AM",
    "1:30 PM",
    "4:00 PM",
    "7:30 PM",
    "10:15 PM"
]

print("\nAvailable Movies:")

for index, movie in enumerate(movies[genre_choice], start=1):
    print(f"{index}. {movie}")

movie_choice = int(input("Enter movie choice: "))

booking_date = datetime.datetime.now()
booking_date_str = booking_date.strftime("%d-%b-%Y")

days_to_show = random.randint(1, 7)
show_date = booking_date + datetime.timedelta(days=days_to_show)

show_date_str = show_date.strftime("%d-%b-%Y")
day_name = show_date.strftime("%A")

show_time = random.choice(show_times)

selected_movie = movies[genre_choice][movie_choice - 1]

print("\nBooking Confirmed!")
print(f"Name         : {name}")
print(f"Movie        : {selected_movie}")
print(f"Booking Date : {booking_date_str}")
print(f"Show Date    : {show_date_str}")
print(f"Show Time    : {show_time}")
print(f"Day          : {day_name}")

print("\nEnjoy your movie!")