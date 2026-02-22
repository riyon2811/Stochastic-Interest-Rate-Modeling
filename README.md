# Stochastic Interest Rate Modelling.

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


 
# 1. Vasicek Model — Zero-Coupon Bond Pricing (Part A)

Notebook: Project Assignment Que 1 (a) part python code.ipynb

This section computes:

 .The B(t, T) and A(t, T) functions of the Vasicek model

 .The analytical price of a Zero-Coupon Bond for a 5-year maturity

 .Sensitivity to model parameters:- a,b,σ,r

Key Concepts:

* Mean reversion of interest rates

* Analytical bond pricing formula

* Term structure modelling


# 2. Monte Carlo Simulation of Short-Rate Paths (Part B)

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

# 3. Swap Rate Computation (Part C)

Notebook: Project Assignment Que 1 (c) python code.ipynb

This section:

 .Computes ZCB prices for maturities 1–5

 .Uses them to compute the fixed rate of a plain vanilla interest rate swap

 .Presents the swap par rate in percentage terms

Core Idea:-

A swap rate is the fixed rate that equates the present value of floating vs fixed payments
using discount factors derived from model-based ZCB prices.


# 4. Option Pricing on a Zero-Coupon Bond (Part D)

Notebook: Project Assignment Que 1 (d) python code.ipynb

This notebook prices a European call option on a 4-year Zero Coupon Bond:

 .Computes forward bond price

 .Computes option volatility under the Vasicek model

 .Applies the Black formula for bond options

 .Returns the theoretical fair value of the option

# Skills Demonstrated:

 .Term structure derivative pricing

 .Analytic volatility expression

 .Lognormal forward-price dynamics

 .Discounted risk-neutral expectation



