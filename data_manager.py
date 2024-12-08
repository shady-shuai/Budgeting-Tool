import csv
from datetime import datetime
import os
import requests

class BudgetData:
    def __init__(self, file_name="budget_data.csv"):
        self.file_name = file_name
        self.data = []
        self.load_data()
        self.base_currency = "CAD"  # Default base currency

    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, mode='r') as file:
                    reader = csv.DictReader(file)
                    self.data = [row for row in reader]
                    if not self.data:
                        print("No data found. Please add income or expenses to get started.")
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print("File not found. Starting with an empty budget.")

    def save_data(self):
        try:
            with open(self.file_name, mode='w', newline='') as file:
                fieldnames = ['date', 'type', 'category', 'amount', 'currency']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)
            print(f"Data saved successfully to {self.file_name}.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def add_entry(self, entry_type, category, amount, date, currency):
        try:
            if entry_type not in ['Income', 'Expense']:
                raise ValueError("Type must be 'Income' or 'Expense'.")
            if amount <= 0:
                raise ValueError("Amount must be positive.")

            # Convert amount to base currency (CAD)
            amount_in_cad = self.convert_currency(amount, currency, self.base_currency)

            entry = {
                'date': date,
                'type': entry_type,
                'category': category,
                'amount': f"{amount_in_cad:.2f}",  # Store as CAD
                'currency': currency
            }
            self.data.append(entry)
            self.save_data()
            self.load_data()  # Reload the data after saving
            print(f"{entry_type} of {amount:.2f} {currency} (converted to {amount_in_cad:.2f} CAD) added successfully in category '{category}' on {date}.")
        except Exception as e:
            print(f"Error adding entry: {e}")

    def convert_currency(self, amount, from_currency, to_currency):
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url)
            data = response.json()
            rates = data['rates']
            if to_currency in rates:
                return amount * rates[to_currency]
            else:
                raise ValueError(f"Currency {to_currency} not supported.")
        except Exception as e:
            print(f"Error converting currency: {e}")
            return amount  # Fallback to original amount if API fails

    def get_categories(self, entry_type):
        return sorted({entry['category'] for entry in self.data if entry['type'] == entry_type})
