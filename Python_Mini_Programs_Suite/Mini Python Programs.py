import random
import smtplib
import string


def main():
    programs = {
        "1": ("Rock Paper Scissors", rock_paper_scissors),
        "2": ("Random Story Generator", story_generator),
        "3": ("OTP Email Verification", otp_verification),
        "4": ("BMI Calculator", bmi_calculator)
    }

    while True:
        print("\n" + "=" * 40)
        print("           MINI PROGRAMS")
        print("=" * 40)

        for number, (name, _) in programs.items():
            print(f"{number}. {name}")

        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Program closed.")
            break

        if choice in programs:
            programs[choice][1]()
        else:
            print("Invalid choice. Please try again.")


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    print("\n===== ROCK PAPER SCISSORS =====")

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? (1-5): "))

            if 1 <= rounds <= 5:
                break

            print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")

    player_score = 0
    computer_score = 0

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")

        player_choice = input(
            "Choose rock, paper or scissors: "
        ).strip().lower()

        if player_choice not in choices:
            print("Invalid choice. Round skipped.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("Result: Draw")

        elif winning_moves[player_choice] == computer_choice:
            print("Result: You win this round.")
            player_score += 1

        else:
            print("Result: Computer wins this round.")
            computer_score += 1

        print(f"Score: You {player_score} - Computer {computer_score}")

    print("\n===== FINAL RESULT =====")

    if player_score > computer_score:
        print("You won the game.")
    elif computer_score > player_score:
        print("Computer won the game.")
    else:
        print("The game ended in a draw.")

    print(f"Final Score: You {player_score} - Computer {computer_score}")


def story_generator():
    time_options = [
        "Yesterday",
        "Last weekend",
        "One evening",
        "Early this morning",
        "A few years ago"
    ]

    characters = [
        "a student",
        "a software developer",
        "a photographer",
        "a detective",
        "a young entrepreneur"
    ]

    places = [
        "in a small village",
        "inside an old library",
        "near the beach",
        "in a busy city",
        "on a remote island"
    ]

    events = [
        "found a mysterious box",
        "discovered a hidden map",
        "solved an unusual problem",
        "received an unexpected message",
        "found a secret room"
    ]

    endings = [
        "by following a strange clue",
        "with the help of a friend",
        "after taking a big risk",
        "by trusting their instincts",
        "after learning from a mistake"
    ]

    print("\n===== RANDOM STORY GENERATOR =====")

    try:
        number_of_stories = int(
            input("How many stories do you want? ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if number_of_stories <= 0:
        print("Please enter a number greater than zero.")
        return

    print()

    for number in range(1, number_of_stories + 1):
        story = (
            f"{random.choice(time_options)}, "
            f"{random.choice(characters)} "
            f"{random.choice(events)} "
            f"{random.choice(places)} "
            f"{random.choice(endings)}."
        )

        print(f"Story {number}:")
        print(story)
        print()


def generate_otp(length=6):
    return "".join(random.choices(string.digits, k=length))


def otp_verification():
    print("\n===== OTP EMAIL VERIFICATION =====")

    sender_email = input("Enter your Gmail address: ").strip()
    app_password = input("Enter your Gmail app password: ").strip()
    receiver_email = input("Enter the receiver's email: ").strip()

    otp = generate_otp()

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, app_password)

        email_message = (
            f"Subject: OTP Verification\n\n"
            f"Your OTP is: {otp}\n"
            f"Please do not share this OTP with anyone."
        )

        server.sendmail(
            sender_email,
            receiver_email,
            email_message
        )

        server.quit()

        print(f"OTP sent successfully to {receiver_email}.")

        entered_otp = input("Enter the OTP you received: ").strip()

        if entered_otp == otp:
            print("OTP verification successful.")
        else:
            print("Incorrect OTP. Verification failed.")

    except smtplib.SMTPAuthenticationError:
        print("Gmail login failed. Check your email and app password.")

    except Exception as error:
        print("Unable to send the OTP.")
        print("Error:", error)


def bmi_calculator():
    print("\n===== BMI CALCULATOR =====")

    name = input("Enter your name: ").strip()

    try:
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if age <= 0:
            print("Age must be greater than zero.")
            return

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        print("\n===== BMI RESULT =====")
        print(f"Name     : {name}")
        print(f"Age      : {age}")
        print(f"Weight   : {weight:.1f} kg")
        print(f"Height   : {height:.2f} m")
        print(f"BMI      : {bmi:.2f}")
        print(f"Category : {category}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()