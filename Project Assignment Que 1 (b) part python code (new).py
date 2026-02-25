import numpy as np

# -------------------------------
# Vasicek Model Parameters
# -------------------------------
r_0 = 0.08     # Initial short rate r(0)
a = 0.3        # Speed of mean reversion
b = 0.05       # Long-term mean level
sigma = 0.03   # Volatility of short rate
T = 5          # Time horizon (years)

timesteps = 1825              # Number of time steps (daily discretization ~5*365)
numberofsimulations = 1825    # Number of Monte Carlo paths

dt = T / numberofsimulations  # Time step size
print(dt)

# -------------------------------
# Monte Carlo Simulation of
# Vasicek Short-Rate Paths
# Using Euler-Maruyama Discretization
# -------------------------------
simulations = []

for _ in range(numberofsimulations):
    interestRates = [r_0]  # Initialize path with r(0)
    
    for _ in range(timesteps):
        # Brownian increment dW ~ N(0, sqrt(dt))
        dw = np.random.normal(0, np.sqrt(dt))
        
        # Vasicek SDE:
        # dr = a(b - r_t)dt + sigma dW
        dr = a * (b - interestRates[-1]) * dt + sigma * dw
        
        # Update short rate
        interestRates.append(interestRates[-1] + dr)
    
    simulations.append(interestRates)

# -------------------------------
# Zero-Coupon Bond Pricing via
# Risk-Neutral Expectation
# P(0,T) = E[ exp(- ∫ r(t) dt ) ]
# -------------------------------
zcb_prices = []
rates_paths = []

for path in simulations:
    
    # Numerical integration of short rate path
    # Approximates ∫ r(t) dt using trapezoidal rule
    rate_path = np.trapz(path, dx=dt)
    rates_paths.append(round(rate_path, 2))
    
    # Discount factor along each simulated path
    zcb_price = np.exp(-rate_path)
    zcb_prices.append(round(zcb_price, 2))

# Monte Carlo estimator of bond price
average_ZCB_price = np.mean(zcb_prices)
print(average_ZCB_price)