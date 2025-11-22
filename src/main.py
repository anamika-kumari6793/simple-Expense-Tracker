from expense_manager import ExpenseManager
from analytics import ExpenseAnalytics
from report_generator import ReportGenerator

def main():
    expense_manager = ExpenseManager()
    analytics = ExpenseAnalytics()
    report_gen = ReportGenerator()
    
    while True:
        print("\n" + "="*30)
        print("    SIMPLE EXPENSE TRACKER")
        print("="*30)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Delete Expense")
        print("5. View Analytics")
        print("6. Generate Report")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            print("\n--- Add New Expense ---")
            amount = input("Amount: $")
            description = input("Description: ")
            print("Categories:", ", ".join(expense_manager.get_categories()))
            category = input("Category: ").capitalize()
            
            success, message = expense_manager.add_expense(amount, description, category)
            print(f"\n{message}")
        
        elif choice == '2':
            print("\n--- All Expenses ---")
            expenses = expense_manager.view_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                for exp in expenses:
                    print(f"ID: {exp['id']} | ${exp['amount']:.2f} | {exp['category']} | {exp['description']} | {exp['date']}")
        
        elif choice == '3':
            print("\n--- View by Category ---")
            print("Categories:", ", ".join(expense_manager.get_categories()))
            category = input("Enter category: ").capitalize()
            
            expenses = expense_manager.view_expenses(category)
            if not expenses:
                print(f"No expenses found in {category} category.")
            else:
                total = sum(exp['amount'] for exp in expenses)
                for exp in expenses:
                    print(f"${exp['amount']:.2f} | {exp['description']} | {exp['date']}")
                print(f"\nTotal for {category}: ${total:.2f}")
        
        elif choice == '4':
            print("\n--- Delete Expense ---")
            expenses = expense_manager.view_expenses()
            if not expenses:
                print("No expenses to delete.")
            else:
                for exp in expenses:
                    print(f"ID: {exp['id']} | ${exp['amount']:.2f} | {exp['category']} | {exp['description']}")
                
                try:
                    expense_id = int(input("\nEnter expense ID to delete: "))
                    success, message = expense_manager.delete_expense(expense_id)
                    print(message)
                except ValueError:
                    print("Please enter a valid number.")
        
        elif choice == '5':
            print("\n--- Analytics ---")
            total = analytics.get_total_spending()
            print(f"Total Spending: ${total:.2f}")
            
            breakdown = analytics.get_category_breakdown()
            print("\nCategory Breakdown:")
            for category, amount in breakdown.items():
                print(f"  {category}: ${amount:.2f}")
            
            # Show ASCII chart
            report_gen.generate_console_chart()
        
        elif choice == '6':
            print("\n--- Generating Report ---")
            report = report_gen.generate_text_report()
            print("Report generated and saved to 'reports/expense_report.txt'")
            print("\n" + report)
        
        elif choice == '7':
            print("Thank you for using Simple Expense Tracker!")
            break
        
        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()