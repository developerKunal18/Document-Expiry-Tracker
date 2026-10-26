import json
from config import DATA_DIR, DOCUMENTS_FILE


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not DOCUMENTS_FILE.exists():
        with DOCUMENTS_FILE.open("w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_documents():
    initialize_storage()

    try:
        with DOCUMENTS_FILE.open("r", encoding="utf-8") as file:
            documents = json.load(file)

        if not isinstance(documents, list):
            print("Warning: Document data must be a JSON list.")
            return []

        return documents

    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load documents: {error}")
        return []


def save_documents(documents):
    initialize_storage()

    with DOCUMENTS_FILE.open("w", encoding="utf-8") as file:
        json.dump(documents, file, indent=4, ensure_ascii=False)
