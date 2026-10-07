# Quick-Commerce Delivery and Customer Satisfaction Analysis

An interactive dashboard analysing 813 orders across seven Indian quick-commerce platforms.

**CHRIST (Deemed to be University)** — School of Business and Management
BBA Honours (Business Analytics) · BBA303B-5 — Python Programming for Business Analytics · CIA-3 Mini Project

## Team 11

| Name | Register No. | Role |
|---|---|---|
| Azhar Malik | 2421117 | Project lead & business framing |
| Anjana Mohandas | 2421135 | Data cleaning & preprocessing |
| Sai Shyaam | 2421146 | Exploratory analysis & benchmarking |
| Suditi Mallik | 2421149 | Visualisation |
| Vamsi Krishna | 2421176 | Text analysis, hypothesis testing & insights |
| Bharath Kishore Reddy | 2421367 | Documentation, dashboard & deployment |

## What the project does

Quick-commerce platforms promise grocery delivery in 10 to 20 minutes. This project uses Python to
answer one question: **what actually decides whether a customer is satisfied** — speed, product
category, order value, the platform brand, or how complaints are handled?

The analysis loads the data, cleans it, engineers new columns, benchmarks all seven platforms,
reads the customers' written feedback, tests eight business hypotheses, and produces a ranked list
of recommended actions.

## Main findings

- **Delay is the strongest driver of satisfaction.** On-time orders average close to 4.7 stars;
  severely delayed orders fall below 2.
- **Satisfaction collapses at around 10 to 15 minutes past the promised time** — far earlier than
  expected. This is where an automatic apology or credit should trigger.
- **The gap between platforms is a delivery gap, not a brand gap.** The platforms with the longest
  delays are the same ones with the lowest ratings.
- **Negative feedback predicts refunds**, so the free-text comments work as an early warning system.
- **Three of eight hypotheses were not supported**, including two drawn from the team's own case
  study: perishable categories are not rated lower, and peak hours are not meaningfully more delayed.

## Files

| File | Description |
|---|---|
| `dashboard.py` | Streamlit dashboard application |
| `dashboard_data.csv` | Cleaned dataset (813 orders) |
| `requirements.txt` | Python dependencies |

## Running it locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

The dashboard opens at `http://localhost:8501`.

## Deploying

Hosted free on [Streamlit Community Cloud](https://share.streamlit.io): sign in with GitHub,
choose **Create app**, select this repository, set the main file to `dashboard.py`, and deploy.

## Dashboard features

- Filters for platform, product category and delay group
- Live summary figures: order count, average rating, refund rate, average delay
- Average rating by platform
- Refund rate by feedback theme
- The satisfaction cliff — average rating by delay band
- Platform delay against platform rating
- Satisfaction mix per platform
- Filtered order table

## Data source

Merged by Team 11 from public quick-commerce order and review datasets on
[Kaggle](https://www.kaggle.com/datasets). 813 order records covering seven platforms and
fifteen product categories.

## Tools used

Pandas · Matplotlib · Seaborn · Plotly Express · Streamlit
