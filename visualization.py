import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class Visualization:
    def __init__(self, budget_data):
        self.budget_data = budget_data

    def visualize_by_category(self, parent):
        expense_categories = {}
        income_categories = {}

        for entry in self.budget_data.data:
            amount = float(entry['amount'])
            if entry['type'] == 'Expense':
                expense_categories[entry['category']] = expense_categories.get(entry['category'], 0) + amount
            elif entry['type'] == 'Income':
                income_categories[entry['category']] = income_categories.get(entry['category'], 0) + amount

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        # Plot expenses pie chart
        if expense_categories:
            axes[0].pie(expense_categories.values(), labels=expense_categories.keys(), autopct='%1.1f%%', startangle=140)
            axes[0].set_title("Expenses by Category (in CAD)")
        else:
            axes[0].text(0.5, 0.5, "No Expenses", horizontalalignment='center', verticalalignment='center')

        # Plot income pie chart
        if income_categories:
            axes[1].pie(income_categories.values(), labels=income_categories.keys(), autopct='%1.1f%%', startangle=140)
            axes[1].set_title("Income by Category (in CAD)")
        else:
            axes[1].text(0.5, 0.5, "No Income", horizontalalignment='center', verticalalignment='center')

        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def visualize_trends(self, parent):
        data = []
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

        # Group data by date and type
        df_grouped = df.groupby(['Date', 'Type'])['Amount'].sum().unstack().fillna(0)

        # Create the figure and subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        # Plot the line chart on the first subplot
        df_grouped.plot(kind='line', marker='o', ax=ax1)
        ax1.set_title("Income and Expense Trends")
        ax1.set_xlabel("Month")
        ax1.set_ylabel("Amount (CAD)")
        ax1.legend(title="Type")
        ax1.grid(True)

        # Plot the bar chart on the second subplot with income and expenses side by side
        df_grouped.plot(kind='bar', ax=ax2, width=0.8)
        ax2.set_title("Monthly Income vs Expense")
        ax2.set_xlabel("Month")
        ax2.set_ylabel("Amount (CAD)")
        ax2.legend(title="Type")
        plt.xticks(rotation=45)

        plt.tight_layout()

        # Embed the figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack()

