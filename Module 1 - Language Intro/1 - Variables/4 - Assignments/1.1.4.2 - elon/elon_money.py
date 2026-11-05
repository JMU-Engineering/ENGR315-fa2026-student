"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
P = 44_000_000_000  # principal amount in dollars = 44_000_000_000  # principal amount in dollars
R1 = 3.96  # interest rate for 10-year bonds in percent
R2 = 4.32  # interest rate for 20-year bonds in percent
T1 = 10  # time in years for 10-year bonds
T2 = 20  # time in years for 20-year bonds
N = 1  # number of times interest is compounded per year
x = P * (1 + (R1 / 100)) ** (N * T1)
y = P * (1 + (R2 / 100)) ** (N * T2)

# final answer for 10-year
ten_year_final = x

# final answer for 20-year
twenty_year_final = y

print("Final value of 10-year bonds: ", ten_year_final)
print("Final value of 20-year bonds: ", twenty_year_final) 