import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from data_manager import BudgetData
from visualization import Visualization

class BudgetingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budgeting Tool")
        self.root.geometry("900x800")

        # Initialize data and visualization modules
        self.tool = BudgetData("budget_data.csv")
        self.visual = Visualization(self.tool)

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Budgeting Tool", font=("Arial", 16))
        title_label.pack(pady=10)

        # Buttons
        income_button = ttk.Button(self.root, text="Add Income", command=self.add_income)
        income_button.pack(pady=5)

        expense_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)
        expense_button.pack(pady=5)

        category_button = ttk.Button(self.root, text="Visualize by Category", command=self.display_category_visualization)
        category_button.pack(pady=5)

        trend_button = ttk.Button(self.root, text="Visualize Trends", command=self.display_trends_visualization)
        trend_button.pack(pady=5)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=5)

    def add_income(self):
        self.add_entry("Income")

    def add_expense(self):
        self.add_entry("Expense")

    def add_entry(self, entry_type):
        # Create a pop-up window for entry input
        popup = tk.Toplevel(self.root)
        popup.title(f"Add {entry_type}")
        popup.geometry("300x400")

        # Category input
        categories = self.tool.get_categories(entry_type)
        category_label = tk.Label(popup, text="Category:")
        category_label.pack(pady=5)

        category_var = tk.StringVar()

        category_entry = ttk.Entry(popup, textvariable=category_var)
        category_entry.pack(pady=5)

        if categories:
            category_dropdown = ttk.Combobox(popup, values=categories, state="readonly")
            category_dropdown.pack(pady=5)

            def update_category_var(event):
                category_var.set(category_dropdown.get())

            category_dropdown.bind("<<ComboboxSelected>>", update_category_var)

        # Date input
        date_label = tk.Label(popup, text="Date:")
        date_label.pack(pady=5)
        date_entry = DateEntry(popup, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_entry.pack(pady=5)

        # Amount input
        amount_label = tk.Label(popup, text="Amount:")
        amount_label.pack(pady=5)
        amount_entry = ttk.Entry(popup)
        amount_entry.pack(pady=5)

        # Currency input
        currency_label = tk.Label(popup, text="Currency:")
        currency_label.pack(pady=5)
        currency_var = tk.StringVar(value="CAD")
        currency_dropdown = ttk.Combobox(popup, textvariable=currency_var, values=["CAD", "USD", "EUR", "CNY", "GBP"], state="readonly")
        currency_dropdown.pack(pady=5)

        def save_entry():
            try:
                category = category_var.get()
                if not category:
                    raise ValueError("Category cannot be empty.")
                amount = float(amount_entry.get())
                date = date_entry.get_date().strftime('%Y-%m-%d')
                currency = currency_var.get()
                self.tool.add_entry(entry_type, category, amount, date, currency)
                messagebox.showinfo("Success", f"{entry_type} added successfully!")
                popup.destroy()
            except ValueError as e:
                if "could not convert string to float" in str(e):
                    messagebox.showerror("Error", "Please enter a valid number for the amount.")
                else:
                    messagebox.showerror("Error", str(e))

        save_button = ttk.Button(popup, text="Save", command=save_entry)
        save_button.pack(pady=10)

    def display_category_visualization(self):
        # Create a new window to display the visualization
        viz_window = tk.Toplevel(self.root)
        viz_window.title("Category Visualization")
        viz_window.geometry("800x600")
        self.visual.visualize_by_category(viz_window)

    def display_trends_visualization(self):
        # Create a new window to display the trends visualization
        viz_window = tk.Toplevel(self.root)
        viz_window.title("Trends Visualization")
        viz_window.geometry("800x600")
        self.visual.visualize_trends(viz_window)
