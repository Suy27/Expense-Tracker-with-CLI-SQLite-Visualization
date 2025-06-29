# Expense-Tracker-with-CLI-SQLite-Visualization
Python Mini Project [**IDC**](https://indiandataclub.notion.site/30DaysOfPython-1f9a16c0422f8074bf29eee315a6802a) 30days Python Challenge)

# 💰 Expense Tracker CLI App (Python + SQLite + Matplotlib)
A simple yet powerful command-line application to **track your daily expenses**, where we can view category-wise summaries, and visualise our spendings using bar charts.

Built as part of my 30 Days Of Python Challenge, this project applies real-world Python skills including:
- File I/O
- SQLite database handling
- CLI interaction
- Data visualization (matplotlib)

---

##  Features

  - Add new expense records (date, category, amount, note)  
  - View all recorded expenses  
  - Get total spending by category  
  - Export all records to a CSV file  
  - Visualize category-wise spending with bar charts  
  - Uses persistent SQLite storage  
  - Clean modular functions — easy to read & maintain
---
## 🛠 Tech Stack
- Python 3.9+
- SQLite3
- matplotlib
---

## 📁 Project Structure
**exp_tracker/**
```bash
├── exp_tracker_main.py # Main CLI logic

├── database.py # Database connection + table setup

├── expenses.db # SQLite database (auto-created)

├── expenses_export.csv # Exported CSV file (after choosing option 4)

├── expense_chart.png # visualisation
```
---
## ⚙️ Setup & Run
### 1. Clone this repository or download the files
```bash
https://github.com/Suy27/Expense-Tracker-with-CLI-SQLite-Visualization.git
cd Expense-Tracker-with-CLI-SQLite-Visualization
```
### 2. Install required packages
   - If using Anaconda:
     ```bash
       conda install matplotlib

  - Or with pip:

    ```bash
    pip install matplotlib

### 3. Run the app
```bash
python exp_tracker_main.py
```
---
## How to Use
### Menu Options:
```bash
1. Add Expense               ➜ Add a new entry with date, category, amount, note  
2. View Expenses             ➜ List all stored expenses  
3. Total by Category         ➜ Show total spend per category  
4. Export to CSV             ➜ Save all records to 'expenses_export.csv'  
5. Visualize Expenses        ➜ Display a bar chart by category  
6. Exit                      ➜ Close the app
```
---

## Screenshots

**CLI Interface:**

<img width="838" alt="CLI_interface" src="https://github.com/Suy27/Expense-Tracker-with-CLI-SQLite-Visualization/blob/main/Snaps/CLI_interface.jpg" />

**Visualisation:**

<img width="838" alt="CLI_interface" src="https://github.com/Suy27/Expense-Tracker-with-CLI-SQLite-Visualization/blob/main/Snaps/ViZ_Bar_Chart.jpg" />

---

## 📌 Learning Highlights
   - SQL queries in Python (SELECT, INSERT, GROUP BY)

   - Using matplotlib for data visualization

   - Clean CLI interaction using loops and user input

   - Functions with parameters, return values, and scope 

   - Real-world data modeling with SQLite

---
## 📌 Upcoming Improvements

   - Date-based filtering (monthly, weekly)

   - Convert to web app using Flask/Streamlit

   - Add category management (create/edit/delete)

   - Add login/user-specific data
     
---
##  Credits
Challenge: ***#30DaysOfPython*** by [**Indian Data Club**](https://www.indiandataclub.com/)
