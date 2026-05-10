# 📚 Library Management System

A Python-based command-line application for managing library operations. This system allows users to search for books, borrow items, return books with automatic fine calculation, and manage borrowing records.

## 🎯 Features

- **User Authentication**: Secure login system with credentials verification
- **Book Search**: Search through a comprehensive database of books by title
- **Borrow Books**: Check out books with customizable borrowing duration
- **Return Books**: Process book returns with automatic late fee calculation
- **Fine System**: Automatic fine calculation at ₹10 per day for overdue books
- **CSV-based Storage**: Persistent data storage using CSV files

## 📋 Prerequisites

- Python 3.x
- pandas library

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ArihantK15/Library-Management-System.git
cd Library-Management-System
```

2. Install required dependencies:
```bash
pip install pandas
```

## 🚀 Usage

1. Run the main application:
```bash
python main.py
```

2. Login with your credentials (default username and password are stored in `cred.csv`)

3. Use the menu to:
   - **Search for a book**: Enter the book title or partial title to find books
   - **Borrow a book**: Enter the ISBN and borrower details with allowed borrowing days
   - **Return a book**: Enter the ISBN and actual days kept to process the return
   - **Logout**: Exit the system

### Example Workflow

```
1. Login to the system
2. Search for a book: "Python"
3. Note the ISBN from search results
4. Borrow the book by entering ISBN and borrowing period
5. Return the book and enter actual days kept
6. System automatically calculates any fines if overdue
```

## 📁 Project Structure

```
Library-Management-System/
├── main.py                 # Main application file
├── cleaner.py              # Data cleaning utility script
├── books_cleaned.csv       # Processed book database
├── clean_books.csv         # Sample cleaned books data
├── borrow.csv              # Active borrowing records
├── cred.csv                # User credentials
└── README.md              # This file
```

## 📊 Data Files

### books_cleaned.csv
Contains the library's book catalog with columns:
- ISBN
- Book-Title
- Book-Author

### borrow.csv
Tracks active borrowing records with columns:
- ISBN
- Name (Borrower)
- Days (Allowed borrowing period)

### cred.csv
User login credentials with columns:
- Username
- Password

## 🔧 How It Works

### Book Search
- Searches the `books_cleaned.csv` file for matching titles
- Uses case-insensitive partial string matching
- Displays ISBN, Title, and Author of matching books

### Borrowing Process
1. User enters the ISBN of the book to borrow
2. System verifies the book exists and isn't already borrowed
3. Collects borrower name and allowed borrowing period
4. Records the transaction in `borrow.csv`

### Return Process
1. User enters the ISBN of the book being returned
2. System retrieves the allowed borrowing period from records
3. User enters actual days the book was kept
4. If days exceed allowed period:
   - Calculates fine: (extra_days × ₹10)
   - Displays the fine amount
5. Removes the record from `borrow.csv`

## 💰 Fine Calculation

Late fees are calculated at **₹10 per day** for any days exceeding the allowed borrowing period.

**Example:**
- Allowed days: 14
- Actual days: 18
- Extra days: 4
- Fine: 4 × ₹10 = **₹40**

## 🔐 Security Notes

- Credentials are currently stored in plain text CSV (consider upgrading for production)
- ISBN values are stripped and standardized to prevent formatting issues
- Input validation prevents duplicate book borrowing

## 📝 Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User interface upgrade (GUI with tkinter or Flask web app)
- Admin panel for book management and user creation
- Email notifications for overdue books
- Advanced search filters (author, ISBN, publication year)
- Fine payment tracking
- Book reservation system

## 👤 Author

**ArihantK15**

## 📄 License

This project is currently unlicensed. Feel free to use and modify as needed.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## 🐛 Troubleshooting

### "No books found" error
- Ensure `books_cleaned.csv` is in the same directory as `main.py`
- Check that the CSV file has proper formatting with semicolon separators

### Login fails
- Verify credentials in `cred.csv` are correct
- Ensure no extra whitespace in credentials file

### "ISBN not found" when borrowing
- Double-check the ISBN from the book search results
- Ensure ISBN is entered correctly without extra spaces

## 📧 Support

For issues or questions, please create an issue in the repository.

---

**Happy Reading! 📖**
