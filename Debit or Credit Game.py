# Debit or Credit the game
import random

# list of common accounts and normal balances
accounts = [
    # assets (debit)
    ("Cash", "debit"),
    ("Accounts Receivable", "debit"),
    ("Inventory", "debit"),
    ("Prepaid Expenses", "debit"),
    ("Property, Plant and Equipment", "debit"),
    ("Intangible Assets", "debit"),
    ("Goodwill", "debit"),
    ("Investments (Non-current)", "debit"),
    ("Trade and Other Receivables", "debit"),
    ("Deferred Tax Asset", "debit"),
    ("Biological Assets", "debit"),

    # liabilities (credit)
    ("Accounts Payable", "credit"),
    ("Accrued Expenses", "credit"),
    ("Short-term Borrowings", "credit"),
    ("Long-term Borrowings", "credit"),
    ("Deferred Revenue", "credit"),
    ("Provisions", "credit"),
    ("Employee Benefits Liability", "credit"),
    ("Deferred Tax Liability", "credit"),
    ("Lease Liability", "credit"),

    # equity (credit, except contra-equity)
    ("Share Capital", "credit"),
    ("Retained Earnings", "credit"),
    ("Other Comprehensive Income", "credit"),
    ("Revaluation Surplus", "credit"),
    ("Non-controlling Interest", "credit"),
    ("Treasury Shares (contra-equity)", "debit"),

    # revenue (credit)
    ("Sales Revenue", "credit"),
    ("Interest Revenue", "credit"),
    ("Dividend Income", "credit"),
    ("Gain on Disposal of Assets", "credit"),
    ("Service Revenue", "credit"),

    # expenses (debit)
    ("Cost of Goods Sold", "debit"),
    ("Wages and Salaries Expense", "debit"),
    ("Rent Expense", "debit"),
    ("Utilities Expense", "debit"),
    ("Depreciation Expense", "debit"),
    ("Amortisation Expense", "debit"),
    ("Loss on Disposal of Assets", "debit"),
    ("Impairment Loss", "debit"),
    ("Insurance Expense", "debit"),
    ("Advertising Expense", "debit"),
    ("Repairs and Maintenance Expense", "debit"),
    ("Bad Debt Expense", "debit"),
    ("Telephone Expense", "debit"),
    ("Bank Charges", "debit"),
    ("Office Supplies Expense", "debit"),
    ("Travel Expense", "debit"),

    # contra accounts
    ("Accumulated Depreciation (contra-asset)", "credit"),
    ("Allowance for Doubtful Accounts (contra-asset)", "credit"),
    ("Sales Returns and Allowances (contra-revenue)", "debit"),
    ("Purchase Returns and Allowances (contra-expense)", "credit"),
]

def game():
    print("Debit or Credit the game. Type 'stop' to exit.")
    while True:
        account, normal = random.choice(accounts)
        answer = input(f"{account}: ").strip().lower()
        if answer == 'stop':
            print("Thank you for playing.")
            break
        if answer == normal:
            print("Correct!")
        else:
            print(f"Incorrect. {account} is normally a {normal} balance.")

if __name__ == '__main__':
    game()
