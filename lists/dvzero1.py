# Portfolio information
portfolio_value = 1000000
modified_duration = 5

# 1 basis point = 0.01% = 0.0001
one_basis_point = 0.0001

# Calculate DV01
dv01 = portfolio_value * modified_duration * one_basis_point

print(f"DV01: ${dv01:,.2f}")

# Assume interest rates increase by 1 basis point
new_portfolio_value = portfolio_value - dv01

print(f"Original portfolio: ${portfolio_value:,.2f}")
print(f"New portfolio value: ${new_portfolio_value:,.2f}")