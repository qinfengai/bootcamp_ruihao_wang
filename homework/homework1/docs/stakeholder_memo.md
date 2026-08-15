# Stakeholder Memo: Stock Portfolio Risk Prediction

**To:** Portfolio Risk Manager  
**From:** Ruihao Wang  
**Date:** August 15, 2026  
**Subject:** Scoping a one-day-ahead portfolio risk warning system

## Executive Summary

This project proposes a daily risk-warning system for an equal-weighted portfolio of five liquid U.S. large-cap stocks from different sectors. Using information available after each market close, the system will forecast next-day portfolio volatility, estimate one-day 95% Value at Risk (VaR), and produce a low/medium/high risk flag before the next trading session.

The output supports, rather than automates, exposure and hedging decisions. The first version will be compared with a 20-day rolling-volatility baseline. A useful model should improve out-of-sample volatility MAE by at least 5%, report RMSE and VaR exceedances, and run in less than five minutes.

## Stakeholder Persona & User

- **Decision owner:** Portfolio Risk Manager.
- **Tool/operator:** Analyst responsible for running and validating the workflow.
- **End users:** Portfolio Manager and Traders.
- **Decision time:** After market close and before the next trading session.

Current pain points include backward-looking reports, hidden risk concentrations, inconsistent calculations, and model outputs that do not translate into a clear action.

## Useful Answer & Proposed Workflow

The required answer is predictive. The workflow validates data, calculates portfolio risk measures, generates next-day volatility and 95% VaR estimates, assigns a risk flag, and identifies the main risk contributors. The stakeholder-facing artifact is a short risk table and chart set supported by a reproducible Jupyter Notebook.

## Success Criteria

- Volatility MAE at least 5% lower than the 20-day benchmark.
- RMSE reported alongside MAE.
- 95% VaR exceedance rate monitored against 5%, initially using a 3%-7% review range.
- No use of future information in forecasting or evaluation.
- Complete run time below five minutes.
- Every risk flag includes an explanation of its main drivers.

## Assumptions & Constraints

- Five liquid U.S. large-cap stocks from different sectors with equal weights.
- Legally usable adjusted daily price data.
- No intraday, options, news, or order-book data in the first version.
- Chronological or walk-forward evaluation instead of random splitting.
- Decision-support output only; no automated trading.

## Known Unknowns / Risks & Monitoring

- Monitor performance across market regimes.
- Track rolling correlations and concentration.
- Validate missing values, duplicates, and extreme returns.
- Preserve forecast timestamps to prevent look-ahead bias.
- Report losses beyond VaR and monitor model drift.

## Decisions Requested from the Stakeholder

1. Does the one-day horizon match the decision cycle?
2. Is 95% VaR sufficient, or is 99% VaR also required?
3. Which actions correspond to low, medium, and high risk?
4. Is the five-stock equal-weighted portfolio representative enough?
5. Is a Notebook summary, daily table, or dashboard most useful?
