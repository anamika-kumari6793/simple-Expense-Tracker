import json
import os

class FileHandler:
    def __init__(self, filename="data/expenses.json"):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        """Create file and folder if they don't exist"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)
    
    def read_expenses(self):
        """Read all expenses from file"""
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def write_expenses(self, expenses):
        """Write expenses to file"""
        with open(self.filename, 'w') as f:
            json.dump(expenses, f, indent=2)