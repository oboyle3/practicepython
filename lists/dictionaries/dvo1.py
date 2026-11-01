# Portfolio information
portfolio_value = 1000000
modified_duration = 3
# 1 basis point = 0.01% = 0.0001
one_basis_point = 0.0001
# Calculate DV01
dv01 = portfolio_value * modified_duration * one_basis_point
print(f"DV01: ${dv01:,.2f}")
# Assume interest rates increase by 1 basis point
new_portfolio_value = portfolio_value - dv01
print(f"Original portfolio: ${portfolio_value:,.2f}")
print(f"New portfolio value: ${new_portfolio_value:,.2f}")
#Every 1 basis point increase in interest rates produces approximately a $300 loss in portfolio value.
print(f"one_basis_point {one_basis_point} increse in interest rates produces apprx. {dv01} loss in portfolio value")

#pass a duration and portfoio worth and basispoint value and see the dv01
def dvo1(basispoint,portfolio,duration):
    dv01_for_this_portfolio = basispoint*portfolio*duration
    print(f"dv01_for_this_portfolio = {dv01_for_this_portfolio}")
    print(f"your portfolio {portfolio} would lose {dv01_for_this_portfolio} $ over {duration} years")
    return dv01_for_this_portfolio

dvo1(.0003,9000,3)