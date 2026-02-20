# Stochastic-Interest-Rate-Modeling
Implementation of the Vasicek short-rate model for bond, swap and bond option pricing using analytical and Monte Carlo methods.
import numpy as np
import matplotlib.pyplot as plt

# ============================
# Analytical Vasicek Formula
# ============================

def vasicek_bond_price_analytical(a, b, sigma, r0, T):
    B = (1 - np.exp(-a * T)) / a
    A = np.exp(
        ((B - T) * (a**2 * b - 0.5 * sigma**2)) / (a**2)
        - (sigma**2 * B**2) / (4 * a)
    )
    return A * np.exp(-B * r0)


# ============================
# Monte Carlo Simulation
# ============================

def vasicek_monte_carlo(a, b, sigma, r0, T, timesteps, n_sim):
    dt = T / timesteps
    rates = np.zeros((n_sim, timesteps + 1))
    rates[:, 0] = r0

    for t in range(1, timesteps + 1):
        dW = np.random.normal(0, np.sqrt(dt), n_sim)
        rates[:, t] = rates[:, t - 1] + a * (b - rates[:, t - 1]) * dt + sigma * dW

    # Approximate integral ∫ r(t) dt
    integral = np.trapz(rates, dx=dt, axis=1)
    bond_prices = np.exp(-integral)

    return np.mean(bond_prices)


# ============================
# Yield Curve
# ============================

def yield_curve(a, b, sigma, r0, maturities):
    prices = [vasicek_bond_price_analytical(a, b, sigma, r0, T) for T in maturities]
    yields = [-np.log(P)/T for P, T in zip(prices, maturities)]
    return yields


# ============================
# Parameters
# ============================

a = 0.3
b = 0.05
sigma = 0.03
r0 = 0.08
T = 5


# ============================
# 1️⃣ Analytical vs Monte Carlo
# ============================

analytical_price = vasicek_bond_price_analytical(a, b, sigma, r0, T)
mc_price = vasicek_monte_carlo(a, b, sigma, r0, T, timesteps=1000, n_sim=10000)

print("Analytical Price:", analytical_price)
print("Monte Carlo Price:", mc_price)
print("Absolute Error:", abs(analytical_price - mc_price))


# ============================
# 2️⃣ Convergence Study
# ============================

simulations = [100, 500, 1000, 5000, 10000]
mc_prices = []

for n in simulations:
    price = vasicek_monte_carlo(a, b, sigma, r0, T, timesteps=1000, n_sim=n)
    mc_prices.append(price)

plt.figure()
plt.plot(simulations, mc_prices)
plt.axhline(analytical_price)
plt.title("Monte Carlo Convergence")
plt.xlabel("Number of Simulations")
plt.ylabel("Bond Price")
plt.show()


# ============================
# 3️⃣ Yield Curve
# ============================

maturities = np.linspace(0.5, 30, 60)
yc = yield_curve(a, b, sigma, r0, maturities)

plt.figure()
plt.plot(maturities, yc)
plt.title("Vasicek Yield Curve")
plt.xlabel("Maturity")
plt.ylabel("Yield")
plt.show()


# ============================
# 4️⃣ Sensitivity Analysis
# ============================

sigmas = [0.01, 0.03, 0.07]

plt.figure()
for s in sigmas:
    yc = yield_curve(a, b, s, r0, maturities)
    plt.plot(maturities, yc)

plt.title("Yield Curve Sensitivity to Volatility")
plt.xlabel("Maturity")
plt.ylabel("Yield")
plt.show()
