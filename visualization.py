import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Initialize data and create the class
class Visualization:
    def __init__(self, budget_data):
        self.budget_data = budget_data

    # Visualize categorized data as pie charts
    def visualize_by_category(self, parent):
        # Aggregate expense and income data by category
        expense_categories = {}
        income_categories = {}

        # Process each entry in budget data
        for entry in self.budget_data.data:
            amount = float(entry['amount'])
            if entry['type'] == 'Expense':
                # Sum expenses by category
                expense_categories[entry['category']] = expense_categories.get(entry['category'], 0) + amount
            elif entry['type'] == 'Income':
                # Sum income by category
                income_categories[entry['category']] = income_categories.get(entry['category'], 0) + amount


        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        # Helper function to format percentage and value in the pie chart
        def format_autopct(pct, all_vals):
            total = sum(all_vals)
            amount = int(round(pct * total / 100.0))
            return f'{pct:.1f}%\n(${amount})'

        # Plot pie chart for expenses
        if expense_categories:
            expense_values = list(expense_categories.values())
            axes[0].pie(
                expense_values,
                autopct=lambda pct: format_autopct(pct, expense_values),
                startangle=140,
                labeldistance=1.1
            )
            axes[0].set_title("Expenses by Category (in CAD)")
            axes[0].legend(expense_categories.keys(), loc="center left", bbox_to_anchor=(1, 0.5))

        # Plot pie chart for income
        if income_categories:
            income_values = list(income_categories.values())
            axes[1].pie(
                income_values,
                autopct=lambda pct: format_autopct(pct, income_values),
                startangle=140,
                labeldistance=1.1
            )
            axes[1].set_title("Income by Category (in CAD)")
            axes[1].legend(income_categories.keys(), loc="center left", bbox_to_anchor=(1, 0.5))

        # Adjust layout for better visualization
        fig.subplots_adjust(left=0.05, right=0.85, top=0.9, bottom=0.1)
        plt.tight_layout()

        # Embed the pie charts in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

    # Visualize income and expense trends over time
    def visualize_trends(self, parent):
        data = []
        # Transform budget data into a suitable format for visualization
        for entry in self.budget_data.data:
            data.append({
                'Date': entry['date'][:7],
                'Type': entry['type'],
                'Amount': float(entry['amount'])
            })

        df = pd.DataFrame(data)
        if df.empty:
            print("No data to visualize.")
            return

        # Group data by date and type, and calculate monthly totals
        df_grouped = df.groupby(['Date', 'Type'])['Amount'].sum().unstack().fillna(0)

        # Create a side-by-side layout for line and bar charts
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Line chart for trends over time
        df_grouped.plot(kind='line', marker='o', ax=ax1)
        ax1.set_title("Income and Expense Trends")
        ax1.set_xlabel("Month")
        ax1.set_ylabel("Amount (CAD)")
        ax1.legend(title="Type")
        ax1.grid(True)

        # Bar chart for monthly income vs expense
        df_grouped.plot(kind='bar', ax=ax2, width=0.8)
        ax2.set_title("Monthly Income vs Expense")
        ax2.set_xlabel("Month")
        ax2.set_ylabel("Amount (CAD)")
        ax2.legend(title="Type")
        plt.xticks(rotation=45)

        # Adjust layout for better visualization
        plt.tight_layout()
        plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

        # Embed the charts in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

