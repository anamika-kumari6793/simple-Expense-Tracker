import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from expense_manager import ExpenseManager

def test_add_expense():
    """Test adding a valid expense"""
    manager = ExpenseManager()
    success, message = manager.add_expense("25.50", "Test lunch", "Food")
    assert success == True, "Should successfully add valid expense"
    print("✅ Add expense test passed")

def test_invalid_amount():
    """Test adding expense with invalid amount"""
    manager = ExpenseManager()
    success, message = manager.add_expense("invalid", "Test", "Food")
    assert success == False, "Should reject invalid amount"
    print("✅ Invalid amount test passed")

def test_invalid_category():
    """Test adding expense with invalid category"""
    manager = ExpenseManager()
    success, message = manager.add_expense("50", "Test", "InvalidCategory")
    assert success == False, "Should reject invalid category"
    print("✅ Invalid category test passed")

def test_view_expenses():
    """Test viewing expenses"""
    manager = ExpenseManager()
    expenses = manager.view_expenses()
    assert isinstance(expenses, list), "Should return list of expenses"
    print("✅ View expenses test passed")

if __name__ == "__main__":
    test_add_expense()
    test_invalid_amount()
    test_invalid_category()
    test_view_expenses()
    print("\n🎉 All tests passed!")