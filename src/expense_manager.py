from file_handler import FileHandler
from datetime import datetime

class ExpenseManager:
    def __init__(self):
        self.file_handler = FileHandler()
        self.categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]
    
    def add_expense(self, amount, description, category):
        """Add a new expense"""
        if category not in self.categories:
            return False, "Invalid category"
        
        try:
            amount = float(amount)
            if amount <= 0:
                return False, "Amount must be positive"
        except ValueError:
            return False, "Invalid amount"
        
        expenses = self.file_handler.read_expenses()
        
        new_expense = {
            "id": len(expenses) + 1,
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        expenses.append(new_expense)
        self.file_handler.write_expenses(expenses)
        return True, "Expense added successfully"
    
    def view_expenses(self, category_filter=None):
        """View all expenses, optionally filtered by category"""
        expenses = self.file_handler.read_expenses()
        
        if category_filter:
            expenses = [exp for exp in expenses if exp['category'] == category_filter]
        
        return expenses
    
    def delete_expense(self, expense_id):
        """Delete an expense by ID"""
        expenses = self.file_handler.read_expenses()
        original_count = len(expenses)
        
        expenses = [exp for exp in expenses if exp['id'] != expense_id]
        
        if len(expenses) < original_count:
            self.file_handler.write_expenses(expenses)
            return True, "Expense deleted successfully"
        else:
            return False, "Expense not found"
    
    def get_categories(self):
        """Get list of available categories"""
        return self.categories