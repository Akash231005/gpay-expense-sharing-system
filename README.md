# GPay Expense Sharing System

## Project Overview

The GPay Expense Sharing System is a Python-based expense management application that allows multiple users to share and track expenses efficiently.

This project simulates the expense-sharing functionality available in applications like Google Pay and Splitwise.

The application supports:
- Equal expense splitting
- Custom expense splitting
- Settlement calculation
- Suggested payment transactions
- Transaction history management
- SQLite database storage
- Expense matrix visualization

---

# Features

## 1. Add Equal Split Expenses
Users can split expenses equally among multiple beneficiaries.

Example:
- Alice pays ₹1200 for Alice, Bob, and Carol
- Each person owes ₹400

---

## 2. Add Custom Split Expenses
Users can define custom amounts for each participant.

Example:
- Alice: ₹500
- Bob: ₹300
- Carol: ₹200

---

## 3. Settlement Calculation
The system automatically calculates:
- Who should receive money
- Who owes money

---

## 4. Suggested Payments
The system minimizes transactions by suggesting optimized payments between users.

Example:
Bob should pay ₹400 to Alice

---

## 5. Transaction History
All expenses are stored permanently using SQLite database.

---

## 6. Expense Matrix
The project maintains an expense matrix to track:
- Who paid
- Who owes

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main Programming Language |
| NumPy | Matrix calculations |
| PrettyTable | Tabular display |
| SQLite3 | Database management |

---

# Project Structure

```text
expense-sharing-project/
│
├── expense_sharing.py
├── expenses.db
├── README.md
└── screenshots/
```

---

# Installation

## Step 1: Install Python
Install Python 3.10 or above.

Download:
https://www.python.org/downloads/

---

## Step 2: Install Required Packages

Run the following command:

```bash
pip install numpy prettytable
```

---

# How to Run the Project

Run the following command:

```bash
python expense_sharing.py
```

---

# Menu Options

```text
1. Add Equal Split Expense
2. Add Custom Split Expense
3. Display Settlements
4. Suggest Payments
5. Show Transaction History
6. Show Expense Matrix
7. Exit
```

---

# Input Format

## Equal Split Expense

Example:

```text
Enter payer name:
Alice

Enter beneficiaries separated by comma:
Alice,Bob,Carol

Enter amount:
1200
```

---

## Custom Split Expense

Example:

```text
Enter payer name:
Alice

How many beneficiaries?
3

Enter friend name:
Alice

Enter amount for Alice:
500

Enter friend name:
Bob

Enter amount for Bob:
300

Enter friend name:
Carol

Enter amount for Carol:
200
```

---

# Sample Output

## Final Settlements

```text
+--------+--------------------------+
| Friend | Settlement               |
+--------+--------------------------+
| Alice  | Should Receive ₹400.00   |
| Bob    | Owes ₹400.00             |
| Carol  | Should Receive ₹400.00   |
| David  | Owes ₹400.00             |
+--------+--------------------------+
```

---

# Database Used

The project uses SQLite database:

```text
expenses.db
```

Table Name:
```text
transactions
```

Database Fields:
- id
- payer
- beneficiaries
- amount
- split_type

---

# Core Concepts Used

- Arrays and matrices
- Expense balancing
- Settlement algorithms
- Database operations
- Python functions
- Loops and conditional statements

---

# Future Enhancements

- GUI using Tkinter
- Dynamic user addition
- Export reports to PDF/Excel
- Graphical analytics
- Cloud database integration
- Mobile app version

---

# Conclusion

This project demonstrates how digital payment applications manage shared expenses efficiently using algorithms and database systems.

The project improves understanding of:
- Expense management systems
- Python programming
- Database integration
- Real-world financial logic

---

# Author

Akash  
SSN College of Engineering