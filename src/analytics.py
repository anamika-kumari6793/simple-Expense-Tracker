from file_handler import FileHandler

class ExpenseAnalytics:
    def __init__(self):
        self.file_handler = FileHandler()
    
    def get_total_spending(self):
        """Calculate total spending"""
        expenses = self.file_handler.read_expenses()
        return sum(expense['amount'] for expense in expenses)
    
    def get_category_breakdown(self):
        """Get spending by category"""
        expenses = self.file_handler.read_expenses()
        breakdown = {}
        
        for expense in expenses:
            category = expense['category']
            breakdown[category] = breakdown.get(category, 0) + expense['amount']
        
        return breakdown
    
    def get_monthly_summary(self):
        """Get monthly spending summary"""
        expenses = self.file_handler.read_expenses()
        monthly_data = {}
        
        for expense in expenses:
            month = expense['date'][:7]  # Get YYYY-MM
            monthly_data[month] = monthly_data.get(month, 0) + expense['amount']
        
        return monthly_data
    
    def get_recent_expenses(self, count=5):
        """Get most recent expenses"""
        expenses = self.file_handler.read_expenses()
        return sorted(expenses, key=lambda x: x['date'], reverse=True)[:count]