import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load expenses CSV
def load_expenses(file_path="expenses.csv"):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("expenses.csv not found, creating a new file...")
        df = pd.DataFrame(columns=["Date", "Category", "Amount"])
        df.to_csv(file_path, index=False)
        return df

# Add a new expense
def add_expense(category, amount, file_path="expenses.csv"):
    df = load_expenses(file_path)
    new_row = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Category": category,
        "Amount": float(amount)
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(file_path, index=False)
    print("Expense added successfully!")

# Summary by category
def generate_summary(file_path="expenses.csv"):
    df = load_expenses(file_path)
    summary = df.groupby("Category")["Amount"].sum().reset_index()
    summary.to_csv("summary.csv", index=False)
    print("Summary saved as summary.csv")
    print(summary)
    return summary

# Plot graph
def plot_graph(file_path="expenses.csv"):
    df = load_expenses(file_path)
    summary = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(7, 5))
    summary.plot(kind="bar")
    plt.title("Expense Summary by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()

# Menu
def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary (Category wise)")
        print("3. Show Graph")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (Food, Travel, Bills, etc): ")
            amount = input("Enter amount: ")
            add_expense(category, amount)

        elif choice == "2":
            generate_summary()

        elif choice == "3":
            plot_graph()

        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid input! Try again.")

if __name__ == "__main__":
    menu()
