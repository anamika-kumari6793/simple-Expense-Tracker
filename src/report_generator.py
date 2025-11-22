from analytics import ExpenseAnalytics
import os

class ReportGenerator:
    def __init__(self):
        self.analytics = ExpenseAnalytics()
    
    def generate_text_report(self):
        """Generate a simple text report"""
        total = self.analytics.get_total_spending()
        breakdown = self.analytics.get_category_breakdown()
        recent = self.analytics.get_recent_expenses(3)
        
        report = "=== EXPENSE TRACKER REPORT ===\n\n"
        report += f"Total Spending: ${total:.2f}\n\n"
        
        report += "Category Breakdown:\n"
        for category, amount in breakdown.items():
            percentage = (amount / total * 100) if total > 0 else 0
            report += f"  {category}: ${amount:.2f} ({percentage:.1f}%)\n"
        
        report += "\nRecent Expenses:\n"
        for expense in recent:
            report += f"  {expense['date']}: ${expense['amount']:.2f} - {expense['description']} ({expense['category']})\n"
        
        # Save to file
        os.makedirs('reports', exist_ok=True)
        with open('reports/expense_report.txt', 'w') as f:
            f.write(report)
        
        return report
    
    def generate_console_chart(self):
        """Generate a simple ASCII chart for category breakdown"""
        breakdown = self.analytics.get_category_breakdown()
        total = sum(breakdown.values())
        
        print("\n=== SPENDING CHART ===")
        for category, amount in breakdown.items():
            percentage = (amount / total * 100) if total > 0 else 0
            bars = '█' * int(percentage / 5)  # Each █ represents 5%
            print(f"{category:15} {bars} ${amount:.2f} ({percentage:.1f}%)")