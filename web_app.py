import streamlit as st
import sys
import os

# Add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from expense_manager import ExpenseManager
from analytics import ExpenseAnalytics
from report_generator import ReportGenerator

# Set page title
st.set_page_config(page_title="Expense Tracker", page_icon="💰")

# Title
st.title("💰 Simple Expense Tracker")
st.markdown("Track your expenses easily!")

# Initialize managers
expense_manager = ExpenseManager()
analytics = ExpenseAnalytics()
report_gen = ReportGenerator()

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", [
    "Add Expense", 
    "View Expenses", 
    "Analytics", 
    "Generate Report"
])

if menu == "Add Expense":
    st.header("Add New Expense")
    
    with st.form("expense_form"):
        amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
        description = st.text_input("Description")
        category = st.selectbox("Category", expense_manager.get_categories())
        
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            success, message = expense_manager.add_expense(amount, description, category)
            if success:
                st.success(message)
            else:
                st.error(message)

elif menu == "View Expenses":
    st.header("All Expenses")
    
    expenses = expense_manager.view_expenses()
    if not expenses:
        st.info("No expenses found.")
    else:
        # Display as table
        import pandas as pd
        df = pd.DataFrame(expenses)
        st.dataframe(df)
        
        # Total spending
        total = sum(exp['amount'] for exp in expenses)
        st.metric("Total Spending", f"${total:.2f}")

elif menu == "Analytics":
    st.header("Spending Analytics")
    
    total = analytics.get_total_spending()
    st.metric("Total Spending", f"${total:.2f}")
    
    # Category breakdown
    breakdown = analytics.get_category_breakdown()
    if breakdown:
        st.subheader("Category Breakdown")
        
        # Display as bar chart
        import pandas as pd
        chart_data = pd.DataFrame({
            'Category': list(breakdown.keys()),
            'Amount': list(breakdown.values())
        })
        st.bar_chart(chart_data.set_index('Category'))
        
        # Display as table
        st.table(chart_data)

elif menu == "Generate Report":
    st.header("Generate Report")
    
    if st.button("Generate Expense Report"):
        report = report_gen.generate_text_report()
        st.success("Report generated successfully!")
        
        # Display report
        st.subheader("Expense Report")
        st.text(report)
        
        # Download button
        st.download_button(
            label="Download Report",
            data=report,
            file_name="expense_report.txt",
            mime="text/plain"
        )