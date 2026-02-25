import numpy as np
import pandas as pd  

# -------------------------------
# Vasicek Model Parameters
# -------------------------------
a = 0.3      # Speed of mean reversion
b = 0.05     # Long-term mean level of short rate
sigma = 0.03 # Volatility of short rate
t = 5        # Time to maturity (in years)
r = 0.08     # Current short rate

# -------------------------------
# Compute B(t,T)
# B(t,T) captures the sensitivity 
# of bond price to the current short rate
# -------------------------------
B = (1 - np.exp(-a * t)) / a
print(B)

# -------------------------------
# Compute A(t,T)
# A(t,T) adjusts for mean reversion,
# volatility, and convexity effects
# in the Vasicek closed-form solution
# -------------------------------
A = np.exp(
    (((B - t) * ((a * a * b) - (sigma * sigma) / 2)) / (a * a))
    - ((sigma * sigma * B * B) / (4 * a))
)
print(A)

# -------------------------------
# Zero-Coupon Bond Pricing Formula
# P(t,T) = A(t,T) * exp(-B(t,T) * r_t)
# Closed-form analytical solution
# under the risk-neutral measure
# -------------------------------
ZCB = A * np.exp(-B * r)
print(ZCB)