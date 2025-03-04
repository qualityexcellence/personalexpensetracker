import csv
import os

def load_expenses(filename='expenses.csv'):
    expenses = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    'date': row['date'],
                    'category': row['category'],
                    'amount': float(row['amount']),
                    'description': row['description']
                })
    return expenses

def save_expenses(expenses, filename='expenses.csv'):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")
    description = input("Enter description: ")
    expenses.append({'date': date, 'category': category, 'amount': amount, 'description': description})
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nExpenses:")
    for expense in expenses:
        if not all(key in expense and expense[key] for key in ['date', 'category', 'amount', 'description']):
            print("Skipping incomplete expense entry.")
            continue
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")

def track_budget(expenses):
    budget = float(input("Enter your monthly budget: "))
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"Total spent: ${total_spent:.2f}")
    if total_spent > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print(f"You have ${budget - total_spent:.2f} remaining for the month.")

def main():
    expenses = load_expenses()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            track_budget(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Expenses saved successfully!")
        elif choice == '5':
            save_expenses(expenses)
            print("Exiting... Your expenses have been saved.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
