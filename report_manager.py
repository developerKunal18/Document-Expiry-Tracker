from collections import Counter
from document_manager import get_document_status
from storage import load_documents
from utils import calculate_days_remaining


def expiry_report():
    documents = load_documents()

    if not documents:
        print("No documents available for reporting.")
        return

    counts = Counter(
        get_document_status(document)
        for document in documents
    )

    total = len(documents)
    expired = counts.get("Expired", 0)
    expires_today = counts.get("Expires Today", 0)
    expiring_soon = counts.get("Expiring Soon", 0)
    valid = counts.get("Valid", 0)

    print("\n========== DOCUMENT EXPIRY REPORT ==========")
    print(f"Total documents         : {total}")
    print(f"Valid documents         : {valid}")
    print(f"Expiring within 30 days : {expiring_soon}")
    print(f"Expiring today          : {expires_today}")
    print(f"Expired documents       : {expired}")
    print("=" * 45)


def category_report():
    documents = load_documents()

    if not documents:
        print("No documents available.")
        return

    counts = Counter(
        document.get("category", "Other")
        for document in documents
    )

    print("\n--- Documents by Category ---")

    for category, count in sorted(counts.items()):
        print(f"{category}: {count}")

    print(f"\nTotal documents: {len(documents)}")


def owner_report():
    documents = load_documents()

    if not documents:
        print("No documents available.")
        return

    owners = {}

    for document in documents:
        owner = document.get("owner", "Unknown")
        owners[owner] = owners.get(owner, 0) + 1

    print("\n--- Documents by Owner ---")

    for owner, count in sorted(owners.items()):
        print(f"{owner}: {count}")

    print(f"\nTotal owners: {len(owners)}")


def upcoming_expiry_report():
    documents = load_documents()

    upcoming = [
        document for document in documents
        if 0 <= calculate_days_remaining(document["expiry_date"]) <= 90
    ]

    upcoming.sort(key=lambda item: item["expiry_date"])

    print("\n--- Documents Expiring Within 90 Days ---")

    if not upcoming:
        print("No documents expiring within 90 days.")
        return

    for document in upcoming:
        days = calculate_days_remaining(document["expiry_date"])

        print(
            f"{document.get('document_id')} | "
            f"{document.get('name')} | "
            f"Owner: {document.get('owner')} | "
            f"Expiry: {document.get('expiry_date')} | "
            f"{days} day(s) remaining"
        )

    print(f"\nTotal upcoming expiries: {len(upcoming)}")
