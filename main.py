from storage import initialize_storage
from document_manager import (
    add_document,
    view_all_documents,
    search_documents,
    edit_document,
    delete_document,
    list_expired_documents,
    list_expiring_soon
)
from report_manager import (
    expiry_report,
    category_report,
    owner_report,
    upcoming_expiry_report
)
from utils import pause


def show_menu():
    print("\n" + "=" * 46)
    print("         DOCUMENT EXPIRY TRACKER")
    print("=" * 46)
    print("1. Add Document")
    print("2. View All Documents")
    print("3. Search Documents")
    print("4. Edit Document")
    print("5. Delete Document")
    print("6. View Expired Documents")
    print("7. View Documents Expiring Within 30 Days")
    print("8. Document Expiry Summary")
    print("9. Category-Wise Report")
    print("10. Owner-Wise Report")
    print("11. Documents Expiring Within 90 Days")
    print("0. Exit")
    print("=" * 46)


def main():
    initialize_storage()

    actions = {
        "1": add_document,
        "2": view_all_documents,
        "3": search_documents,
        "4": edit_document,
        "5": delete_document,
        "6": list_expired_documents,
        "7": list_expiring_soon,
        "8": expiry_report,
        "9": category_report,
        "10": owner_report,
        "11": upcoming_expiry_report
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Document Expiry Tracker!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, ValueError, KeyError, TypeError) as error:
                print(f"An error occurred: {error}")

            pause()
        else:
            print("Invalid choice. Please select a valid menu option.")
            pause()


if __name__ == "__main__":
    main()
