from datetime import date, datetime

from config import DOCUMENT_CATEGORIES, DATE_FORMAT
from storage import load_documents, save_documents
from utils import (
    get_text,
    get_date,
    get_choice,
    get_optional_date,
    calculate_days_remaining
)


def generate_document_id(documents):
    highest_number = 0

    for document in documents:
        document_id = document.get("document_id", "")

        if document_id.startswith("DOC"):
            try:
                number = int(document_id[3:])
                highest_number = max(highest_number, number)
            except ValueError:
                continue

    return f"DOC{highest_number + 1:04d}"


def get_document_status(document):
    days = calculate_days_remaining(document["expiry_date"])

    if days < 0:
        return "Expired"

    if days == 0:
        return "Expires Today"

    if days <= 30:
        return "Expiring Soon"

    return "Valid"


def add_document():
    documents = load_documents()

    print("\n--- Add New Document ---")

    name = get_text("Document name: ")
    owner = get_text("Owner name: ")

    category = get_choice(
        "Select document category: ",
        DOCUMENT_CATEGORIES
    )

    document_number = get_text("Document number/reference: ")
    issue_date = get_date("Issue date (YYYY-MM-DD): ")
    expiry_date = get_date("Expiry date (YYYY-MM-DD): ")

    parsed_issue = datetime.strptime(issue_date, DATE_FORMAT).date()
    parsed_expiry = datetime.strptime(expiry_date, DATE_FORMAT).date()

    if parsed_expiry < parsed_issue:
        print("Expiry date cannot be earlier than the issue date.")
        return

    notes = input("Additional notes (optional): ").strip()

    document = {
        "document_id": generate_document_id(documents),
        "name": name,
        "owner": owner,
        "category": category,
        "document_number": document_number,
        "issue_date": issue_date,
        "expiry_date": expiry_date,
        "notes": notes,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    documents.append(document)
    save_documents(documents)

    print("\nDocument added successfully!")
    print(f"Document ID: {document['document_id']}")
    print(f"Current status: {get_document_status(document)}")


def display_document(document):
    days = calculate_days_remaining(document["expiry_date"])
    status = get_document_status(document)

    print("-" * 50)
    print(f"Document ID      : {document.get('document_id', '')}")
    print(f"Document Name    : {document.get('name', '')}")
    print(f"Owner            : {document.get('owner', '')}")
    print(f"Category         : {document.get('category', '')}")
    print(f"Document Number  : {document.get('document_number', '')}")
    print(f"Issue Date       : {document.get('issue_date', '')}")
    print(f"Expiry Date      : {document.get('expiry_date', '')}")
    print(f"Status           : {status}")

    if days < 0:
        print(f"Expired          : {abs(days)} day(s) ago")
    elif days == 0:
        print("Expiry           : Today")
    else:
        print(f"Days Remaining   : {days}")

    print(f"Notes            : {document.get('notes', '')}")
    print("-" * 50)


def view_all_documents():
    documents = load_documents()

    print("\n--- All Documents ---")

    if not documents:
        print("No documents found.")
        return

    documents.sort(key=lambda item: item.get("expiry_date", ""))

    for document in documents:
        display_document(document)

    print(f"Total documents: {len(documents)}")


def search_documents():
    documents = load_documents()

    if not documents:
        print("No documents available.")
        return

    keyword = input(
        "Search by ID, document name, owner, or category: "
    ).strip().lower()

    if not keyword:
        print("Please enter a search value.")
        return

    results = [
        document for document in documents
        if keyword in document.get("document_id", "").lower()
        or keyword in document.get("name", "").lower()
        or keyword in document.get("owner", "").lower()
        or keyword in document.get("category", "").lower()
        or keyword in document.get("document_number", "").lower()
    ]

    if not results:
        print("No matching documents found.")
        return

    print(f"\nFound {len(results)} document(s).")

    for document in results:
        display_document(document)


def edit_document():
    documents = load_documents()
    document_id = input("Enter document ID to edit: ").strip().upper()

    for document in documents:
        if document.get("document_id", "").upper() != document_id:
            continue

        print("\nLeave a field blank to keep its current value.")

        name = input(f"Document name [{document['name']}]: ").strip()
        owner = input(f"Owner [{document['owner']}]: ").strip()
        number = input(
            f"Document number [{document['document_number']}]: "
        ).strip()

        if name:
            document["name"] = name

        if owner:
            document["owner"] = owner

        if number:
            document["document_number"] = number

        change_category = input(
            f"Change category? Current: {document['category']} (y/n): "
        ).strip().lower()

        if change_category == "y":
            document["category"] = get_choice(
                "Select category: ",
                DOCUMENT_CATEGORIES
            )

        document["issue_date"] = get_optional_date(
            "Issue date",
            document["issue_date"]
        )

        document["expiry_date"] = get_optional_date(
            "Expiry date",
            document["expiry_date"]
        )

        parsed_issue = datetime.strptime(
            document["issue_date"], DATE_FORMAT
        ).date()

        parsed_expiry = datetime.strptime(
            document["expiry_date"], DATE_FORMAT
        ).date()

        if parsed_expiry < parsed_issue:
            print("Expiry date cannot be earlier than issue date.")
            print("Changes were not saved.")
            return

        notes = input(
            f"Notes [{document.get('notes', '')}]: "
        ).strip()

        if notes:
            document["notes"] = notes

        save_documents(documents)
        print("Document updated successfully.")
        return

    print("Document ID not found.")


def delete_document():
    documents = load_documents()
    document_id = input("Enter document ID to delete: ").strip().upper()

    for index, document in enumerate(documents):
        if document.get("document_id", "").upper() == document_id:
            display_document(document)

            confirm = input(
                "Are you sure you want to delete this document? (y/n): "
            ).strip().lower()

            if confirm == "y":
                documents.pop(index)
                save_documents(documents)
                print("Document deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Document ID not found.")


def list_expired_documents():
    documents = load_documents()

    expired = [
        document for document in documents
        if calculate_days_remaining(document["expiry_date"]) < 0
    ]

    print("\n--- Expired Documents ---")

    if not expired:
        print("No expired documents found.")
        return

    for document in expired:
        display_document(document)

    print(f"Total expired documents: {len(expired)}")


def list_expiring_soon():
    documents = load_documents()

    expiring = [
        document for document in documents
        if 0 <= calculate_days_remaining(document["expiry_date"]) <= 30
    ]

    expiring.sort(key=lambda item: item["expiry_date"])

    print("\n--- Documents Expiring Within 30 Days ---")

    if not expiring:
        print("No documents expiring within the next 30 days.")
        return

    for document in expiring:
        display_document(document)

    print(f"Total documents expiring soon: {len(expiring)}")
