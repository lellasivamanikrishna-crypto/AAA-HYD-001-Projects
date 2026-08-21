def main():
    """Run the WhatsApp chat analyzer."""
    raw_messages = get_messages()
    messages = parse_messages(raw_messages)

    while True:
        show_menu()
        choice = input("Choose an option (0-19): ").strip()

        if choice == "1":
            count_total_messages(messages)
        elif choice == "2":
            find_unique_users(messages)
        elif choice == "3":
            count_total_words(messages)
        elif choice == "4":
            average_words_per_message(messages)
        elif choice == "5":
            find_longest_message(messages)
        elif choice == "6":
            find_most_active_user(messages)
        elif choice == "7":
            count_messages_by_user(messages)
        elif choice == "8":
            most_frequent_word_by_user(messages)
        elif choice == "9":
            first_and_last_message_by_user(messages)
        elif choice == "10":
            check_user_presence(messages)
        elif choice == "11":
            find_commonly_repeated_words(messages)
        elif choice == "12":
            find_user_with_longest_average(messages)
        elif choice == "13":
            count_mentions(messages)
        elif choice == "14":
            remove_duplicate_messages(messages)
        elif choice == "15":
            sort_messages_alphabetically(messages)
        elif choice == "16":
            extract_questions(messages)
        elif choice == "17":
            reply_ratio(messages)
        elif choice == "18":
            delete_message(messages)
        elif choice == "19":
            count_deleted_messages(messages)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 19.")


def show_menu():
    print("\n----- WhatsApp Chat Analyzer -----")
    print("1.  Count total messages")
    print("2.  Find unique users")
    print("3.  Count total words")
    print("4.  Calculate average words per message")
    print("5.  Find the longest message")
    print("6.  Find the most active user")
    print("7.  Count messages by user")
    print("8.  Find the most frequent word by user")
    print("9.  Find first and last message by user")
    print("10. Check if a user is present")
    print("11. Find commonly repeated words")
    print("12. Find user with longest average message")
    print("13. Count mentions of a user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Find questions in the chat")
    print("17. Calculate reply ratio")
    print("18. Delete a message")
    print("19. Count deleted messages")
    print("0.  Exit")


def get_messages():
    """Read chat messages from the user."""
    try:
        count = int(input("Enter the number of messages: "))
    except ValueError:
        print("Please enter a valid number.")
        return []

    messages = []

    for _ in range(count):
        messages.append(input())

    return messages


def parse_messages(raw_messages):
    """Convert 'Name: message' lines into tuples."""
    parsed_messages = []

    for line in raw_messages:
        if ":" not in line:
            continue

        user, message = line.split(":", 1)
        parsed_messages.append((user.strip(), message.strip()))

    return parsed_messages


def clean_word(word):
    """Convert a word to lowercase and remove punctuation."""
    punctuation = "!?.,;:\"'()[]{}"
    word = word.lower()

    for character in punctuation:
        word = word.replace(character, "")

    return word


def count_total_messages(messages):
    print(f"Total messages: {len(messages)}")


def find_unique_users(messages):
    users = {user for user, _ in messages}

    if users:
        print("Unique users:")
        for user in sorted(users):
            print(user)
    else:
        print("No users found.")


def count_total_words(messages):
    total_words = sum(len(message.split()) for _, message in messages)
    print(f"Total words in the chat: {total_words}")


def average_words_per_message(messages):
    if not messages:
        print("No messages to analyze.")
        return

    total_words = sum(len(message.split()) for _, message in messages)
    average = total_words / len(messages)

    print(f"Average words per message: {average:.2f}")


def find_longest_message(messages):
    if not messages:
        print("No messages to analyze.")
        return

    user, message = max(messages, key=lambda item: len(item[1]))

    print(f"Longest message: {user}: {message}")


def find_most_active_user(messages):
    if not messages:
        print("No messages to analyze.")
        return

    message_counts = {}

    for user, _ in messages:
        message_counts[user] = message_counts.get(user, 0) + 1

    active_user = max(message_counts, key=message_counts.get)

    print(
        f"Most active user: {active_user} "
        f"({message_counts[active_user]} messages)"
    )


def count_messages_by_user(messages):
    username = input("Enter the username: ").strip()

    count = sum(1 for user, _ in messages if user == username)

    print(f"Messages sent by {username}: {count}")


def most_frequent_word_by_user(messages):
    username = input("Enter the username: ").strip()
    word_counts = {}

    for user, message in messages:
        if user != username:
            continue

        for word in message.split():
            cleaned = clean_word(word)

            if cleaned:
                word_counts[cleaned] = word_counts.get(cleaned, 0) + 1

    if not word_counts:
        print(f"No messages found for user '{username}'.")
        return

    most_common = max(word_counts, key=word_counts.get)

    print(
        f"Most frequent word used by {username}: "
        f"'{most_common}' ({word_counts[most_common]} times)"
    )


def first_and_last_message_by_user(messages):
    username = input("Enter the username: ").strip()

    user_messages = [
        message for user, message in messages
        if user == username
    ]

    if not user_messages:
        print(f"No messages found for user '{username}'.")
        return

    print(f"First message by {username}: {user_messages[0]}")
    print(f"Last message by {username}: {user_messages[-1]}")


def check_user_presence(messages):
    username = input("Enter the username: ").strip()

    users = {user for user, _ in messages}

    if username in users:
        print(f"User '{username}' is present in the chat.")
    else:
        print(f"User '{username}' was not found in the chat.")


def find_commonly_repeated_words(messages):
    word_counts = {}

    for _, message in messages:
        for word in message.split():
            cleaned = clean_word(word)

            if cleaned:
                word_counts[cleaned] = word_counts.get(cleaned, 0) + 1

    repeated_words = [
        word for word, count in word_counts.items()
        if count > 1
    ]

    if repeated_words:
        print("Common repeated words:")

        for word in sorted(repeated_words):
            print(f"{word}: {word_counts[word]} times")
    else:
        print("No repeated words found.")


def find_user_with_longest_average(messages):
    if not messages:
        print("No messages to analyze.")
        return

    total_words = {}
    message_counts = {}

    for user, message in messages:
        total_words[user] = total_words.get(user, 0) + len(message.split())
        message_counts[user] = message_counts.get(user, 0) + 1

    averages = {
        user: total_words[user] / message_counts[user]
        for user in total_words
    }

    top_user = max(averages, key=averages.get)

    print(
        f"User with longest average message: {top_user} "
        f"({averages[top_user]:.2f} words per message)"
    )


def count_mentions(messages):
    username = input("Enter the username to search for: ").strip().lower()

    count = 0

    for _, message in messages:
        words = [clean_word(word) for word in message.split()]

        if username in words:
            count += 1

    print(f"Messages mentioning '{username}': {count}")


def remove_duplicate_messages(messages):
    unique_messages = []
    seen = set()

    for user, message in messages:
        current = (user, message)

        if current not in seen:
            seen.add(current)
            unique_messages.append(current)

    print(f"Original messages: {len(messages)}")
    print(f"Unique messages: {len(unique_messages)}")
    print(f"Duplicates removed: {len(messages) - len(unique_messages)}")


def sort_messages_alphabetically(messages):
    if not messages:
        print("No messages to sort.")
        return

    sorted_messages = sorted(
        messages,
        key=lambda item: item[1].lower()
    )

    print("\nMessages sorted alphabetically:")

    for user, message in sorted_messages:
        print(f"{user}: {message}")


def extract_questions(messages):
    questions = [
        (user, message)
        for user, message in messages
        if "?" in message
    ]

    if not questions:
        print("No questions found in the chat.")
        return

    print("Questions found:")

    for user, message in questions:
        print(f"{user}: {message}")


def reply_ratio(messages):
    if len(messages) < 2:
        print("Not enough messages to calculate replies.")
        return

    replying_user = input("Enter the username that is replying: ").strip()
    previous_user = input("Enter the username being replied to: ").strip()

    reply_count = 0

    for index in range(1, len(messages)):
        previous_sender = messages[index - 1][0]
        current_sender = messages[index][0]

        if (
            previous_sender == previous_user
            and current_sender == replying_user
        ):
            reply_count += 1

    print(
        f"Reply count from {replying_user} "
        f"to {previous_user}: {reply_count}"
    )


def delete_message(messages):
    if not messages:
        print("No messages to delete.")
        return

    print("\nCurrent messages:")

    for index, (user, message) in enumerate(messages, start=1):
        print(f"{index}. {user}: {message}")

    choice = input("Enter the message number to delete: ").strip()

    if not choice.isdigit():
        print("Please enter a valid message number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(messages):
        print("That message number does not exist.")
        return

    user, _ = messages[index]
    messages[index] = (user, "This message was deleted")

    print(f"Message {index + 1} from {user} has been deleted.")


def count_deleted_messages(messages):
    deleted_count = 0

    for _, message in messages:
        if message.strip().lower() in {
            "this message was deleted",
            "<deleted>",
            "[deleted]"
        }:
            deleted_count += 1

    print(f"Total deleted messages: {deleted_count}")


if __name__ == "__main__":
    main()