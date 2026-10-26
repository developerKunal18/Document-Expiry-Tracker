# Document Expiry Tracker

A simple Python application for managing important documents and tracking their expiry dates. It helps users identify expired documents and documents that need renewal soon.

## Features

- Add, view, search, edit, and delete documents
- Generate unique document IDs
- Track document owners and categories
- Record issue dates and expiry dates
- Identify expired documents
- Highlight documents expiring within 30 days
- Generate reports for upcoming expiries within 90 days
- View category-wise and owner-wise summaries
- Store records in JSON format

## Technologies Used

- Python 3
- JSON
- datetime
- collections

## Project Structure

```text
Document-Expiry-Tracker/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── document_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    └── documents.json
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Document-Expiry-Tracker.git
```

### 2. Open the project folder

```bash
cd Document-Expiry-Tracker
```

### 3. Run the application

```bash
python main.py
```

No third-party packages are required.

## Date Format

Enter all dates in this format:

```text
YYYY-MM-DD
```

Example:

```text
2027-05-25
```

## How to Use

1. Select **Add Document**.
2. Enter the document name, owner, category, reference number, issue date, and expiry date.
3. Note the generated document ID.
4. Search for or edit documents when required.
5. Use the expired and upcoming expiry menus to identify documents needing attention.
6. Generate reports to review your document records.

## Data Storage

Records are stored locally in `data/documents.json`. Back up this file regularly to avoid losing your records.

## Learning Outcomes

- Python functions and modules
- JSON file handling
- Lists, dictionaries, and collections
- Date validation and calculations
- Searching, sorting, and filtering
- Exception handling
- Command-line application development

## Future Improvements

- Add a graphical user interface
- Integrate SQLite or MySQL
- Export reports to CSV or PDF
- Add email reminders
- Add document attachments
- Create separate user accounts

## Author

Python Project Challenge 

## License

Free to use for educational and personal learning purposes.
