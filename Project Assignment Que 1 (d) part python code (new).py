import numpy as np
import pandas as pd
from scipy.stats import norm

# -------------------------------
# Vasicek Model Parameters
# -------------------------------
a = 0.3        # Speed of mean reversion
b = 0.05       # Long-term mean short rate
sigma = 0.03   # Volatility of short rate
T = 5          # Maximum maturity (years)
r = 0.08       # Current short rate
K = 900        # Strike price of bond option

# -------------------------------------------------------
# Step 1: Construct Term Structure using Vasicek Model
# Compute ZCB prices for maturities 1 to 5 years
# -------------------------------------------------------
B = []              # Sensitivity coefficient B(0,T)
A = []              # Adjustment coefficient A(0,T)
ZCB_prices = []     # Zero-coupon bond prices

for i in range(5):

    # B(0,T) term captures rate sensitivity
    Bi = (1 - np.exp(-a * (i + 1))) / a
    B.append(Bi)

    # A(0,T) term captures convexity & volatility adjustment
    Ai = np.exp(
        ((B[i] - (i + 1)) * (a * a * b - 0.5 * sigma * sigma)) / (a * a)
        - ((sigma * sigma * B[i] * B[i]) / (4 * a))
    )
    A.append(Ai)

    # Analytical zero-coupon bond price
    ZCBi = A[i] * np.exp(-B[i] * r)
    ZCB_prices.append(ZCBi)

print(B)
print(A)
print(ZCB_prices)

# -------------------------------------------------------
# Step 2: Compute Spot Rates from ZCB Prices
# Using: (1 + R)^T = 1 / P(0,T)
# -------------------------------------------------------
spot_rate_list = []

for j in range(5):
    discount_factor = ZCB_prices[j]
    implied_growth = 1 / discount_factor
    spot_rate = implied_growth**(1 / (j + 1)) - 1
    spot_rate_list.append(spot_rate)
    print(spot_rate)

# -------------------------------------------------------
# Step 3: Price 4-Year Zero-Coupon Bond (Forward Bond)
# Using implied 4-year spot rate
# -------------------------------------------------------
B4 = (1 - np.exp(-a * 1)) / a
A4 = np.exp(
    (((B4 - 1)) * (a * a * b - 0.5 * sigma * sigma)) / (a * a)
    - ((sigma * sigma * B4 * B4) / (4 * a))
)

# Discount using 4-year spot rate
ZCB4 = A4 * np.exp(-B4 * spot_rate_list[3])
print(ZCB4 * 1000)

F0 = ZCB4 * 1000  # Forward bond price
print(F0)

# -------------------------------------------------------
# Step 4: Bond Option Pricing under Vasicek Model
# Using Black-style closed-form solution
# -------------------------------------------------------

# Effective option volatility under Vasicek framework
sigma_option = sigma * np.sqrt((1 - np.exp(-2 * a * 4)) / (2 * a)) * B4
print(sigma_option)

# Black formula components
Numerator = np.log(F0 / K) + 0.5 * sigma_option**2 * 4
Denominator = sigma_option * np.sqrt(4)

d1 = Numerator / Denominator
d2 = d1 - sigma_option * np.sqrt(4)

Nd1 = norm.cdf(d1)
Nd2 = norm.cdf(d2)

# Present value of European call option on bond
option_price = (F0 * Nd1 - K * Nd2) * np.exp(-4 * spot_rate_list[3])
print(option_price)