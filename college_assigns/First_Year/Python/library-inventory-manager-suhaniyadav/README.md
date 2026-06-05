

# Library Inventory Manager

A simple command-line application to manage a campus library's book catalog. Built with Python using Object-Oriented Programming principles.

<img width="482" height="236" alt="Screenshot 2025-11-22 182148" src="https://github.com/user-attachments/assets/216aa1c3-b10a-4228-b6b7-84bdb7036f69" />


---

## Features

- **Add Books** – Add new books to the library catalog
- **Issue Books** – Mark books as issued to students/staff
- **Return Books** – Mark issued books as available again
- **Search Books** – Find books by title or ISBN
- **View All Books** – Display the entire catalog

---

## Project Structure

```
library-inventory-manager-suhaniyadav/
│
├── cli/
│   └── main.py              # Command-line interface
├── library_manager/
│   ├── book.py              # Book class definition
│   └── inventory.py         # Inventory management logic
├── catalog.csv              # Book data storage (auto-generated)
└── README.md                # This file
```

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/suhaniyadav-netizen/library-inventory-manager-suhaniyadav.git
   cd library-inventory-manager-suhaniyadav
   ```

2. **Run the application**
   ```bash
   python -m cli.main
   ```

---

## Usage

When you run the program, you'll see this menu:

```
--- Library Inventory Manager ---
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit
```

### Example Workflow

**Adding a book:**
```
Choose option: 1
Title: Harry Potter and the Goblet Of Fire
Author: J.K Rowling
ISBN: 101
✓ Book added successfully
```

**Issuing a book:**
```
Choose option: 2
Enter ISBN: 101
✓ Issued: Harry Potter and the Goblet Of Fire
```

**Searching books:**
```
Choose option: 5
1. Search by Title
2. Search by ISBN
Enter choice: 1
Enter title: Python
'Harry Potter and the Goblet Of Fire' by J.K Rowling (ISBN: 101, Status: issued)
```

---

## Data Storage

- Books are saved in `catalog.csv` with columns: `title`, `author`, `isbn`, `status`
- The file is created automatically on first run
- All changes are saved immediately

---

## Technical Details

**Built with:**
- Python 3.10+
- CSV for data storage
- Object-Oriented Programming (OOP)

**Key Classes:**
- `Book` – Represents a single book with title, author, ISBN, and status
- `LibraryInventory` – Manages the collection of books and file operations

---

## Requirements

- Python 3.7 or higher
- No external libraries required (uses standard library only)

---

## Assignment Tasks Completed

-  Task 1: Book Class Design
-  Task 2: Inventory Manager
-  Task 3: File Persistence (CSV)
-  Task 4: Menu-Driven CLI
-  Task 5: Exception Handling & Logging
-  Task 6: Project Packaging

---

## Author

- Suhani Yadav
- 2501410032
- B.Tech CSE Cyber Security(First Semester)
- 22nd November 2025
- Programming With Python - Lab Assignment 3
