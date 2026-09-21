#Interest Rates & Bond Prices
bond_face_value = 1000
coupon = 50
years = 1
market_rate = float(input("Enter market interest rate: "))
print(f"you entered MARKET INTREST RATE: {market_rate}")
#What is the $50 coupon I'll receive one year from now worth today, if the market rate is 6%?
#Can I calculate the present value of ONE future payment?
def present_value_of_ONE_future_payment(bond_face_value,coupon,years):
    #pv = coupon / (__________)
    pv = coupon / (1+market_rate)**years
    print(f"pv = {pv}")

present_value_of_ONE_future_payment(bond_face_value,coupon,years)
    