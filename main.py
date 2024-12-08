# Directory Structure Suggestion:
# budgeting_tool/
# ├── main.py               # main
# ├── data_manager.py       # data manger
# ├── visualization.py      # visualization
# ├── gui.py
from gui import BudgetingApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetingApp(root)
    root.mainloop()
