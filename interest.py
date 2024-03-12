import math
def interest(rate):
    # Formula of compound interest!!!
    years = math.log(2) / math.log(1 + rate)
    print(f"Years to double investment: {math.ceil(years):.2f}")
interest(0.07)
