Stochastic Interest Rate Modelling.

Author: Riyon Sunil Tuscano

Project Type: Quantitative Finance / Financial Engineering

Models Used: Vasicek Model, Monte Carlo Simulation, Term Structure Modelling, Derivatives Pricing

Overview:-
This repository contains a comprehensive set of implementations for stochastic interest rate modelling, focusing on the Vasicek mean-reverting short-rate model.
The project covers:

 1.Zero-Coupon Bond (ZCB) pricing

 2.Monte Carlo simulation of interest rate paths

 3.Swap rate computation

 4.Pricing an option on a bond


 

1.Vasicek Model — Zero-Coupon Bond Pricing (Part A)

Notebook: Project Assignment Que 1 (a) part python code.ipynb

This section computes:

 .The B(t, T) and A(t, T) functions of the Vasicek model

 .The analytical price of a Zero-Coupon Bond for a 5-year maturity

 .Sensitivity to model parameters:- a,b,σ,r

Key Concepts:

* Mean reversion of interest rates

* Analytical bond pricing formula

* Term structure modelling


2.Monte Carlo Simulation of Short Rate Paths (Part B)

Notebook: Project Assignment Que 1 (b) python code.ipynb

This notebook:

 .Simulates daily short-rate paths using the Vasicek stochastic differential equation

 .Uses Euler discretization

 .Computes the Monte Carlo estimate of a ZCB price

 .Compares simulation-based estimate vs analytical price

Techniques Used:

 -Stochastic process discretization

 -Numerical integration

 -Convergence analysis

3.Swap Rate Computation (Part C)

Notebook: Project Assignment Que 1 (c) python code.ipynb

This section:

 .Computes ZCB prices for maturities 1–5

 .Uses them to compute the fixed rate of a plain vanilla interest rate swap

 .Presents the swap par rate in percentage terms

Core Idea:-

A swap rate is the fixed rate that equates the present value of floating vs fixed payments
using discount factors derived from model-based ZCB prices.


4.Option Pricing on a Bond (Part D)

Notebook: Project Assignment Que 1 (d) python code.ipynb

This notebook prices a European call option on a 4-year Zero Coupon Bond:

 .Computes forward bond price

 .Computes option volatility under the Vasicek model

 .Applies the Black formula for bond options

 .Returns the theoretical fair value of the option

Skills Demonstrated:

 .Term structure derivative pricing

 .Analytic volatility expression

 .Lognormal forward-price dynamics

 .Discounted risk-neutral expectation





📘 1. Vasicek Model — Zero-Coupon Bond Pricing (Part A)

📄 Notebook: Project Assignment Que 1 (a) part python code.ipynb

This section computes the analytical price of a Zero-Coupon Bond under the Vasicek model.

Vasicek Model Dynamics
𝑑
𝑟
𝑡
=
𝑎
(
𝑏
−
𝑟
𝑡
)
𝑑
𝑡
+
𝜎
𝑑
𝑊
𝑡
dr
t
	​

=a(b−r
t
	​

)dt+σdW
t
	​


Where:

𝑎
a = speed of mean reversion

𝑏
b = long-term mean rate

𝜎
σ = volatility

𝑟
𝑡
r
t
	​

 = short rate

Bond Pricing Form
𝑃
(
𝑡
,
𝑇
)
=
𝐴
(
𝑡
,
𝑇
)
⋅
𝑒
−
𝐵
(
𝑡
,
𝑇
)
𝑟
𝑡
P(t,T)=A(t,T)⋅e
−B(t,T)r
t
	​


Where:

𝐵
(
𝑡
,
𝑇
)
=
1
−
𝑒
−
𝑎
(
𝑇
−
𝑡
)
𝑎
B(t,T)=
a
1−e
−a(T−t)
	​

𝐴
(
𝑡
,
𝑇
)
=
exp
⁡
[
(
𝑏
−
𝜎
2
2
𝑎
2
)
(
𝐵
(
𝑡
,
𝑇
)
−
(
𝑇
−
𝑡
)
)
−
𝜎
2
𝐵
(
𝑡
,
𝑇
)
2
4
𝑎
]
A(t,T)=exp[(b−
2a
2
σ
2
	​

)(B(t,T)−(T−t))−
4a
σ
2
B(t,T)
2
	​

]
This notebook computes

𝐴
(
𝑡
,
𝑇
)
A(t,T) and 
𝐵
(
𝑡
,
𝑇
)
B(t,T)

Analytical ZCB price for a 5-year maturity

Sensitivity of the price to 
𝑎
,
𝑏
,
𝜎
,
𝑟
a,b,σ,r
