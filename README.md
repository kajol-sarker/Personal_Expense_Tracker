# Personal_Expense_Tracker

A simple Python application for tracking and analyzing personal expenses.

## Features

- **Expense Tracking**: Store expenses with categories and amounts
- **Total Calculation**: Automatically sums all expenses
- **Category Analysis**: Breaks down spending by category
- **Savings Calculation**: Compares expenses against income
- **Highest Expense Identification**: Finds the category with maximum spending

## Usage

Run the application:
```bash
python main.py
```

## Sample Output
The application provides:
- Complete expense report
- Total expenses sum
- Category-wise breakdown
- Savings/loss calculation
- Highest spending category

## Data Structure
Expenses are stored as a list of dictionaries:
```python
[
    {"category": "Food", "amount": 2500},
    {"category": "Transport", "amount": 1200},
    # ... more expenses
]
```

## Technologies
- Basic data structures (lists, dictionaries)

## Future Enhancements
- User input for dynamic expense entry
- Data persistence (file/database)
- Graphical interface
- Budget setting and alerts
- Export functionality
