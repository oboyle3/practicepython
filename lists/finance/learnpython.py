#Face value → the $1,000 you originally lend
face_value_of_bond = 1000
#Coupon → the interest payments you receive
coupon_payment = 50
#Maturity → when the company gives your $1,000 back
years = 5
#new market intrest rate
market_interest_rate = 0.06
# calc intrest rate
original_interest_rate = coupon_payment / face_value_of_bond
print(f"{original_interest_rate} : original_interest_rate")
#calculate how much it will be worth
print()
total_back = face_value_of_bond + (years * coupon_payment)
print(f"you can expect {total_back}$ after {years} years")
# Original bond
# $1,000
# $50/year
# 5 years
# = $1,250 total cash received

# The next thing we want your program to answer is:

# "If the market now pays 6%, what is my existing $50/year bond worth today?"