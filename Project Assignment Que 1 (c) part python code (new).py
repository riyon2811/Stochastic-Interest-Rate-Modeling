import numpy as np
import pandas as pd 

# -------------------------------
# Vasicek Model Parameters
# -------------------------------
a = 0.3        # Speed of mean reversion
b = 0.05       # Long-term mean short rate
sigma = 0.03   # Volatility of short rate
T = 5          # Maximum maturity (years)
r = 0.08       # Current short rate

# Containers for term structure quantities
B = []              # Sensitivity coefficient B(t,T)
A = []              # Adjustment coefficient A(t,T)
ZCB_prices = []     # Zero-coupon bond prices across maturities

# -------------------------------
# Term Structure Construction
# Analytical Vasicek Bond Pricing
# -------------------------------
for i in range(5):
    
    # Compute B(0,T_i)
    # Captures impact of mean reversion on rate sensitivity
    Bi = (1 - np.exp(-a * (i + 1))) / a
    B.append(Bi)
    
    # Compute A(0,T_i)
    # Adjusts for convexity and volatility effects
    Ai = np.exp(
        ((B[i] - (i + 1)) * (a * a * b - 0.5 * sigma * sigma)) / (a * a)
        - ((sigma * sigma * B[i] * B[i]) / (4 * a))
    )
    A.append(Ai)
    
    # Closed-form zero-coupon bond price:
    # P(0,T) = A(0,T) * exp(-B(0,T) * r_0)
    ZCBi = A[i] * np.exp(-B[i] * r)
    ZCB_prices.append(ZCBi)

# Display term structure quantities
print(B)
print(A)
print(ZCB_prices)

# -------------------------------
# 5-Year Par Swap Rate Calculation
# Swap Rate = (1 - P(0,T)) / Σ P(0,t_i)
# -------------------------------
swap_rate = (1 - ZCB_prices[4]) / (
    ZCB_prices[0] + ZCB_prices[1] + ZCB_prices[2] +
    ZCB_prices[3] + ZCB_prices[4]
)

# Convert to percentage
print(swap_rate * 100)