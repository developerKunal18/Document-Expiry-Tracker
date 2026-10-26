from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DOCUMENTS_FILE = DATA_DIR / "documents.json"

DATE_FORMAT = "%Y-%m-%d"
EXPIRY_WARNING_DAYS = 30

DOCUMENT_CATEGORIES = [
    "Identity",
    "Vehicle",
    "Insurance",
    "Education",
    "Employment",
    "Business",
    "Other"
]
