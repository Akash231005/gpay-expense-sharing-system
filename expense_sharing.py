# =========================================================
# GPay Expense Sharing Project
# =========================================================

# Required Packages:
# pip install numpy prettytable

import numpy as np
from prettytable import PrettyTable
import sqlite3

# =========================================================
# DATABASE SETUP
# =========================================================

conn = sqlite3.connect("expenses.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    payer TEXT,
    beneficiaries TEXT,
    amount REAL,
    split_type TEXT
)
""")

conn.commit()

# =========================================================
# FRIENDS LIST
# =========================================================

friends = ["Alice", "Bob", "Carol", "David"]

# =========================================================
# EXPENSE MATRIX
# Rows    -> Who Paid
# Columns -> Who Expense Was For
# =========================================================

expense_matrix = np.zeros((len(friends), len(friends)))

# =========================================================
# ADD EQUAL SPLIT EXPENSE
# =========================================================

def add_expense(payer, beneficiaries, amount):

    payer_idx = friends.index(payer)

    share_per_person = amount / len(beneficiaries)

    for beneficiary in beneficiaries:

        beneficiary_idx = friends.index(beneficiary)

        expense_matrix[payer_idx][beneficiary_idx] += share_per_person

    # Save to database
    cursor.execute("""
    INSERT INTO transactions (payer, beneficiaries, amount, split_type)
    VALUES (?, ?, ?, ?)
    """, (
        payer,
        ",".join(beneficiaries),
        amount,
        "Equal Split"
    ))

    conn.commit()

    print("\nExpense Added Successfully!")


# =========================================================
# ADD CUSTOM SPLIT EXPENSE
# =========================================================

def add_custom_expense(payer, split_details):

    payer_idx = friends.index(payer)

    total_amount = 0

    for friend, amount in split_details.items():

        beneficiary_idx = friends.index(friend)

        expense_matrix[payer_idx][beneficiary_idx] += amount

        total_amount += amount

    # Save to database
    cursor.execute("""
    INSERT INTO transactions (payer, beneficiaries, amount, split_type)
    VALUES (?, ?, ?, ?)
    """, (
        payer,
        str(split_details),
        total_amount,
        "Custom Split"
    ))

    conn.commit()

    print("\nCustom Expense Added Successfully!")


# =========================================================
# CALCULATE SETTLEMENTS
# =========================================================

def calculate_settlements():

    # Total amount each person paid
    total_paid = np.sum(expense_matrix, axis=1)

    # Total amount each person owes
    total_owed = np.sum(expense_matrix, axis=0)

    # Net balance
    net_balance = total_paid - total_owed

    return net_balance


# =========================================================
# DISPLAY SETTLEMENTS
# =========================================================

def display_settlements():

    settlements = calculate_settlements()

    table = PrettyTable()

    table.field_names = ["Friend", "Settlement"]

    for i, friend in enumerate(friends):

        if settlements[i] > 0:

            table.add_row(
                [friend, f"Should Receive ₹{settlements[i]:.2f}"]
            )

        elif settlements[i] < 0:

            table.add_row(
                [friend, f"Owes ₹{-settlements[i]:.2f}"]
            )

        else:

            table.add_row(
                [friend, "Is Settled"]
            )

    print("\n================================================")
    print("FINAL SETTLEMENTS")
    print("================================================")

    print(table)


# =========================================================
# SUGGEST PAYMENTS
# =========================================================

def suggest_payments():

    settlements = calculate_settlements()

    creditors = [
        (friends[i], amt)
        for i, amt in enumerate(settlements)
        if amt > 0
    ]

    debtors = [
        (friends[i], -amt)
        for i, amt in enumerate(settlements)
        if amt < 0
    ]

    transactions = []

    while debtors and creditors:

        debtor, debt_amount = debtors.pop(0)

        creditor, credit_amount = creditors.pop(0)

        payment = min(debt_amount, credit_amount)

        transactions.append(
            (debtor, creditor, payment)
        )

        debt_amount -= payment

        credit_amount -= payment

        if debt_amount > 0:

            debtors.insert(0, (debtor, debt_amount))

        if credit_amount > 0:

            creditors.insert(0, (creditor, credit_amount))

    print("\n================================================")
    print("SUGGESTED TRANSACTIONS")
    print("================================================")

    if transactions:

        for debtor, creditor, amount in transactions:

            print(
                f"{debtor} should pay ₹{amount:.2f} to {creditor}"
            )

    else:

        print("No transactions needed.")


# =========================================================
# SHOW TRANSACTION HISTORY
# =========================================================

def show_transaction_history():

    cursor.execute("SELECT * FROM transactions")

    records = cursor.fetchall()

    table = PrettyTable()

    table.field_names = [
        "ID",
        "Payer",
        "Beneficiaries",
        "Amount",
        "Split Type"
    ]

    for row in records:

        table.add_row(row)

    print("\n================================================")
    print("TRANSACTION HISTORY")
    print("================================================")

    print(table)


# =========================================================
# DISPLAY EXPENSE MATRIX
# =========================================================

def show_matrix():

    print("\n================================================")
    print("EXPENSE MATRIX")
    print("================================================")

    print(expense_matrix)


# =========================================================
# MENU SYSTEM
# =========================================================

while True:

    print("\n================================================")
    print("GPay Expense Sharing System")
    print("================================================")

    print("1. Add Equal Split Expense")
    print("2. Add Custom Split Expense")
    print("3. Display Settlements")
    print("4. Suggest Payments")
    print("5. Show Transaction History")
    print("6. Show Expense Matrix")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # =====================================================
    # ADD EQUAL SPLIT
    # =====================================================

    if choice == "1":

        payer = input("Enter payer name: ")

        beneficiaries_input = input(
            "Enter beneficiaries separated by comma: "
        )

        beneficiaries = beneficiaries_input.split(",")

        amount = float(input("Enter amount: "))

        add_expense(
            payer,
            beneficiaries,
            amount
        )

    # =====================================================
    # ADD CUSTOM SPLIT
    # =====================================================

    elif choice == "2":

        payer = input("Enter payer name: ")

        n = int(input("How many beneficiaries? "))

        split_details = {}

        for i in range(n):

            friend = input("Enter friend name: ")

            amount = float(
                input(f"Enter amount for {friend}: ")
            )

            split_details[friend] = amount

        add_custom_expense(
            payer,
            split_details
        )

    # =====================================================
    # DISPLAY SETTLEMENTS
    # =====================================================

    elif choice == "3":

        display_settlements()

    # =====================================================
    # SUGGEST PAYMENTS
    # =====================================================

    elif choice == "4":

        suggest_payments()

    # =====================================================
    # SHOW HISTORY
    # =====================================================

    elif choice == "5":

        show_transaction_history()

    # =====================================================
    # SHOW MATRIX
    # =====================================================

    elif choice == "6":

        show_matrix()

    # =====================================================
    # EXIT
    # =====================================================

    elif choice == "7":

        print("\nExiting Program...")

        conn.close()

        break

    else:

        print("\nInvalid Choice!")