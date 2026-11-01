#pass a duration and portfoio worth and basispoint value and see the dv01
def dvo1(portfolio,duration):
    one_bas_pnt = .0001
    two_bas_pnt = .0002
    three_bas_pnt = .0003
    four_bas_pnt = .0004
    five_bas_pnt = .0005

    dv01_1_for_this_portfolio = one_bas_pnt*portfolio*duration
    basis_pnt_mv_1_worth = portfolio - dv01_1_for_this_portfolio
    print(f"if basis points move 1 point aka {one_bas_pnt} portfilo worth = {basis_pnt_mv_1_worth}")
    dv01_2_for_this_portfolio = two_bas_pnt*portfolio*duration
    basis_pnt_mv_2_worth = portfolio - dv01_2_for_this_portfolio
    print(f"if basis points move 1 point aka {two_bas_pnt} portfilo worth = {basis_pnt_mv_2_worth}")
    dv01_3_for_this_portfolio = three_bas_pnt*portfolio*duration
    basis_pnt_mv_3_worth = portfolio - dv01_3_for_this_portfolio
    print(f"if basis points move 1 point aka {three_bas_pnt} portfilo worth = {basis_pnt_mv_3_worth}")
    dv01_4_for_this_portfolio = four_bas_pnt*portfolio*duration
    basis_pnt_mv_4_worth = portfolio - dv01_4_for_this_portfolio
    print(f"if basis points move 1 point aka {four_bas_pnt} portfilo worth = {basis_pnt_mv_4_worth}")
    dv01_5_for_this_portfolio = five_bas_pnt*portfolio*duration
    basis_pnt_mv_5_worth = portfolio - dv01_5_for_this_portfolio
    print(f"if basis points move 1 point aka {five_bas_pnt} portfilo worth = {basis_pnt_mv_5_worth}")
    dv01_for_this_portfolio = "?"
    return dv01_for_this_portfolio

dvo1(100000,5)
