# Wholesale Loan ALM Report
# -------------------------
# Total_Wholesale_Loans: 2250000
# Total_Funding: 1900000
# Funding Gap: 350000
# Status: Funding Shortfall
# loan_rate = 0.06
# funding_rate = 0.04
# Calculate:
# Loan Interest Income = Total Loans × Loan Rate
# Funding Interest Expense = Total Funding × Funding Rate
# Net Interest Income = Interest Income - Interest Expense
Total_Wholesale_Loans= 2250000
Total_Funding= 1900000
#Funding Gap = Total Loans - Total Funding
def calc_funding(Total_Wholesale_Loans,Total_Funding):
    print("Wholesale Loan ALM Report")
    Funding_Gap = Total_Wholesale_Loans - Total_Funding
    print(f"Funding Gap = {Funding_Gap}")
    if Funding_Gap > 0:
        print("Funding Shortfall")
    else:
        print("Funding To High")

calc_funding(Total_Wholesale_Loans,Total_Funding)

