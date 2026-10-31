#DV01 tells you how many dollars you gain or lose when interest rates move by 0.01%.
portfolio_worth = 1000000 #100k
#lets calculate the dv01
#Interest rate movement =  Rates increase 1 basis point (0.01%)
one_basis_point_movement = 0.0001
#calulate movement
modified_duration = 5 #5 years

Approximate_portfolio_change_DV01 = portfolio_worth * one_basis_point_movement * modified_duration

print(f"DV01 = {Approximate_portfolio_change_DV01 }")

total = portfolio_worth - Approximate_portfolio_change_DV01

print(f" portfolio worth after applies dV01 {one_basis_point_movement} to portfolio worth {portfolio_worth} = total worth {total}")