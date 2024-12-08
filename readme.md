# Budgeting Tool

This is a Python-based budgeting tool designed to help users track income and expenses, visualize spending trends, and manage budgets effectively. The application features a graphical user interface (GUI) for easy interaction and data visualization.

---

## Features

- **Add Income and Expenses:**

  - Easily add and categorize your income and expenses with a simple GUI.

- **Visualizations:**

  - View spending and income breakdown by category using pie charts.
  - Analyze income and expense trends over time with stacked bar charts.

- **Data Persistence:**

  - All data is stored in a CSV file for persistent tracking.

---

## Installation

### Prerequisites

Ensure you have Python 3.7 or above installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone or Download the Repository:**

   - If using Git:
     ```bash
     git clone https://github.com/shady-shuai/Budgeting-Tool.git
     cd budgeting_tool
     ```
   - If provided as a ZIP file, extract the contents and navigate to the extracted folder.

2. **Install Dependencies:**
   Run the following command to install all necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Execute the following command to launch the application:

   ```bash
   python main.py
   ```

---

## File Structure

```
budgeting_tool/
├── main.py               # Entry point for the application
├── gui.py                # GUI logic and interactions
├── data_manager.py       # Data management (load/save CSV)
├── visualization.py      # Visualization logic
├── requirements.txt      # List of dependencies
└── budget_data.csv       # Data file (auto-created if not present)
```

---

## Usage

1. **Launch the App:** Follow the installation steps to start the application.
2. **Add Income or Expenses:**
   - Click "Add Income" or "Add Expense."
   - Fill in the form with category, amount, date, and currency.
3. **View Visualizations:**
   - Select "Visualize by Category" to see pie charts of income and expenses.
   - Select "Visualize Trends" to see stacked bar charts of monthly trends.

---

## Troubleshooting

### Missing Dependencies

If you encounter a module not found error, ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

### Python Version Issues

Ensure you are using Python 3.7 or above:

```bash
python --version
```

---

---

