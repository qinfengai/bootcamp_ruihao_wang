# Stock Portfolio Risk Prediction

**Author:** Ruihao Wang  
**Stage:** Problem Framing & Scoping (Stage 01)  
**Assignment location:** `homework/homework1/`

## Problem Statement

Portfolio risk can change quickly when market volatility, cross-stock correlations, and sector conditions shift. Reports based only on recent realized returns are backward-looking and may not give a portfolio manager enough warning before a high-risk trading day. This project will develop a one-day-ahead risk forecast for an equal-weighted portfolio of five liquid U.S. large-cap stocks selected from different sectors.

The project will estimate next-day portfolio volatility and one-day 95% Value at Risk (VaR), then convert the estimates into a low/medium/high risk flag. The result will support decisions about whether to maintain exposure, reduce positions, add a hedge, or investigate unusual risk drivers. The model will be tested out of sample against a 20-day rolling-volatility baseline.

## Stakeholder & User

- **Decision owner:** The portfolio risk manager, who determines whether expected risk is consistent with portfolio limits and whether additional controls are needed.
- **Tool/operator:** The analyst who runs and validates the daily workflow. The portfolio manager and traders use the result when changing positions or hedges.
- **Timing and workflow context:** The forecast is produced after the market close and reviewed before the next trading session.

## Useful Answer

- **Answer type:** Predictive.
- **Metrics:** Volatility MAE, RMSE, and the 95% VaR exceedance rate.
- **Artifacts:** A reproducible Jupyter Notebook, reusable Python functions, a risk-summary table, supporting charts, and a low/medium/high risk flag.
- **Decision supported:** Maintain exposure, reduce or rebalance positions, add a hedge, or request additional review.
- **Initial success criterion:** Out-of-sample volatility MAE at least 5% lower than the 20-day rolling-volatility benchmark; a 95% VaR exceedance rate reasonably close to 5% (initial range: 3%-7%); and a run time below five minutes.

## Assumptions & Constraints

- Adjusted daily price data are available and correctly account for splits and dividends.
- The initial portfolio contains five liquid U.S. large-cap stocks from different sectors and uses equal weights.
- Portfolio weights are known before each forecast.
- Daily data are sufficient for the first version; intraday, options, news, and order-book data are outside the initial scope.
- Each prediction uses only information available before the forecast date.
- The workflow runs on a standard laptop using Python.
- The project is a decision-support prototype, not investment advice or an automated trading system.
- Data licensing and redistribution rules must be respected.

## Known Unknowns / Risks

- **Market regime change:** Report results across calm and stressed periods.
- **Changing correlations:** Monitor rolling correlations and concentration.
- **Data quality:** Check missing values, duplicate dates, and corporate-action adjustments.
- **Model leakage:** Use chronological or walk-forward testing rather than random splitting.
- **Tail risk:** Report actual tail losses in addition to VaR exceedances.
- **Portfolio sensitivity:** Test alternative stock selections and weighting schemes.
- **Decision thresholds:** Review risk-flag boundaries with the stakeholder.

## Lifecycle Mapping

Goal -> Stage -> Deliverable

- Define a measurable risk problem -> Problem Framing & Scoping (Stage 01) -> README and stakeholder memo.
- Obtain reliable prices -> Data Acquisition & Ingestion -> Raw data, source log, and validation report.
- Store reproducible data -> Data Storage -> Raw/processed folders and data dictionary.
- Understand risk drivers -> Exploratory Data Analysis -> Volatility, correlation, drawdown, and concentration charts.
- Produce a forecast -> Modeling -> Baseline model, candidate model, and Python functions.
- Test usefulness -> Evaluation -> Walk-forward backtest, error metrics, and VaR exceedance analysis.
- Communicate results -> Delivery -> Final Notebook, risk summary, and recommendation.

## Repo Plan

- `data/raw/`: Original data.
- `data/processed/`: Cleaned and model-ready data.
- `src/`: Reusable Python functions.
- `notebooks/`: Numbered analysis and modeling notebooks.
- `docs/`: Stakeholder memo and project documentation.
- `reports/`: Generated tables, charts, and written results.
- `model/`: Saved models and metadata, if needed.

The repository will be updated after each course stage and every meaningful milestone.

## Next Steps

1. Confirm the five-stock portfolio and forecast horizon.
2. Obtain and validate adjusted daily prices.
3. Build the 20-day rolling-volatility benchmark.
4. Define chronological train, validation, and test periods.
5. Evaluate models using MAE, RMSE, and VaR exceedances.
6. Review risk-flag thresholds and reporting format with the stakeholder.
