import matplotlib.pyplot as plt
import csv
import sqlite3
from database import connect

# Call to set up the table
connect()

def add_expenses(date, category, amount, note):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (date, category, amount, note) VALUES (?, ?, ?, ?)",
                (date, category, amount, note))
    conn.commit()
    conn.close()
    
def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    conn.close()
    return rows
    
def total_by_category():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cur.fetchall()
    conn.close()
    
    print("\n Total Spent by Category: \n")
    for row in rows:
            print(f"{row[0]}: ₹{row[1]:.2f}")

def export_to_csv(filename="expenses_export.csv"):
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM expenses")
        rows = cur.fetchall()
        conn.close()
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category", "Amount", "Note"])
            writer.writerows(rows)
            
        print(f"\n Data exported to {filename}")
        
def visualise_expense_by_category():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cur.fetchall()
    conn.close()
    
    if not data:
        print("No data to visualise.")
        return
        
    categories =[row[0] for row in data]
    amounts = [row[1] for row in data]
    
    #plot a bar chat
    plt.figure(figsize=(8,5))
    bars = plt.bar(categories, amounts, color='skyblue')
    
    # Adding value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, height, f'₹{height:.2f}', ha='center', va='bottom')
        
    plt.xlabel("Category")
    plt.ylabel("Total Spent (₹)")
    plt.title("Expenses by Category")
    plt.tight_layout()
    plt.show()
        
 # CLI Menu
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total by Category")
    print("4. Export to CSV")
    print("5. Visualise Expense by Category")
    print("6. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category (e.g. Food, Transport): ")
        amount = float(input("Amount: "))
        note = input("Note: ")
        add_expenses(date, category, amount, note)
        print("Expense added!")
        
    elif choice == '2':
        for row in view_expenses():
            print(row)
    
    elif choice == '3':
        total_by_category()
        
    elif choice == "4":
        export_to_csv()
    
    elif choice == "5":
        visualise_expense_by_category()
    
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")