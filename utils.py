from datetime import date, datetime
from config import DATE_FORMAT


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed_date = datetime.strptime(value, DATE_FORMAT).date()

            # Reject dates that do not exactly match YYYY-MM-DD.
            if parsed_date.strftime(DATE_FORMAT) != value:
                raise ValueError

            return value

        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")
            print("Example: 2027-05-25")


def get_optional_date(prompt, current_value):
    value = input(f"{prompt} [{current_value}]: ").strip()

    if not value:
        return current_value

    try:
        parsed_date = datetime.strptime(value, DATE_FORMAT).date()

        if parsed_date.strftime(DATE_FORMAT) != value:
            raise ValueError

        return value

    except ValueError:
        print("Invalid date. Keeping the previous date.")
        return current_value


def get_choice(prompt, options):
    print("\nAvailable options:")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        choice = input(prompt).strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(options):
                return options[number - 1]

        print(f"Enter a number from 1 to {len(options)}.")


def calculate_days_remaining(expiry_date):
    expiry = datetime.strptime(expiry_date, DATE_FORMAT).date()
    return (expiry - date.today()).days


def pause():
    input("\nPress Enter to continue...")
