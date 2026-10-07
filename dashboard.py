
# ------------------------------------------------------------------
# Quick-Commerce Delivery and Customer Satisfaction Dashboard
# Team 11 - BBA Honours (Business Analytics) - BBA303B-5 - CIA-3
# Run this file with:   streamlit run dashboard.py
# ------------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px

# Make the page use the full width of the browser
st.set_page_config(page_title="Quick-Commerce Dashboard", layout="wide")

# ---------- Load the data saved by the notebook ----------
df = pd.read_csv("dashboard_data.csv")

# ---------- Page heading ----------
st.title("Quick-Commerce Delivery and Customer Satisfaction Dashboard")
st.write("Team 11 - Azhar Malik, Anjana Mohandas, Sai Shyaam, Suditi Mallik, "
         "Vamsi Krishna, Bharath Kishore Reddy")
st.write("CHRIST (Deemed to be University) - BBA Honours (Business Analytics) - CIA-3")

# ---------- Filters in the sidebar ----------
st.sidebar.header("Filters")

all_platforms = sorted(df["Platform"].unique())
all_categories = sorted(df["Category"].unique())
all_buckets = ["On Time", "Minor Delay", "Moderate Delay", "Severe Delay"]

chosen_platforms = st.sidebar.multiselect("Platform", all_platforms, default=all_platforms)
chosen_categories = st.sidebar.multiselect("Product category", all_categories, default=all_categories)
chosen_buckets = st.sidebar.multiselect("Delay group", all_buckets, default=all_buckets)

# Keep only the rows that match every filter
data = df[df["Platform"].isin(chosen_platforms)]
data = data[data["Category"].isin(chosen_categories)]
data = data[data["Delay_Bucket"].isin(chosen_buckets)]

# Stop politely if the user clears all the filters
if len(data) == 0:
    st.warning("No orders match these filters. Please select at least one option in each filter.")
    st.stop()

# ---------- Four summary boxes ----------
box1, box2, box3, box4 = st.columns(4)
box1.metric("Orders", len(data))
box2.metric("Average rating", round(data["Rating"].mean(), 2))
box3.metric("Refund rate", str(round(data["Refund"].mean() * 100, 1)) + " %")
box4.metric("Average delay", str(round(data["Delay"].mean(), 1)) + " min")

st.markdown("---")

# ---------- Row 1: two bar charts side by side ----------
left, right = st.columns(2)

with left:
    platform_summary = data.groupby("Platform")["Rating"].mean().reset_index()
    platform_summary = platform_summary.sort_values("Rating", ascending=False)
    fig1 = px.bar(platform_summary, x="Platform", y="Rating",
                  title="Average rating by platform",
                  labels={"Rating": "Average rating (stars)"})
    st.plotly_chart(fig1)

with right:
    theme_summary = data.groupby("Theme")["Refund"].mean().reset_index()
    theme_summary["Refund"] = theme_summary["Refund"] * 100
    theme_summary = theme_summary.sort_values("Refund", ascending=False)
    fig2 = px.bar(theme_summary, x="Theme", y="Refund",
                  title="Refund rate by feedback theme",
                  labels={"Refund": "Refund rate (%)"})
    st.plotly_chart(fig2)

# ---------- Row 2: the satisfaction cliff ----------
band_summary = data.groupby(["Band_Order", "Delay_Band"])["Rating"].mean().reset_index()
band_summary = band_summary.sort_values("Band_Order")
fig3 = px.line(band_summary, x="Delay_Band", y="Rating", markers=True,
               title="The satisfaction cliff: average rating by delay band",
               labels={"Delay_Band": "Delivery delay (minutes)",
                       "Rating": "Average rating (stars)"})
st.plotly_chart(fig3)

# ---------- Row 3: platform delay against platform rating ----------
scatter_data = data.groupby("Platform").agg(
    Avg_Delay=("Delay", "mean"),
    Avg_Rating=("Rating", "mean"),
    Orders=("Order_ID", "count")
).reset_index()

fig4 = px.scatter(scatter_data, x="Avg_Delay", y="Avg_Rating",
                  color="Platform", size="Orders",
                  title="Platforms with longer delays get lower ratings",
                  labels={"Avg_Delay": "Average delay (minutes)",
                          "Avg_Rating": "Average rating (stars)"})
st.plotly_chart(fig4)

# ---------- Row 4: satisfaction mix ----------
mix = data.groupby(["Platform", "Satisfaction"])["Order_ID"].count().reset_index()
mix = mix.rename(columns={"Order_ID": "Orders"})
fig5 = px.bar(mix, x="Platform", y="Orders", color="Satisfaction",
              title="Satisfied, neutral and dissatisfied orders on each platform")
st.plotly_chart(fig5)

# ---------- The filtered table ----------
st.markdown("---")
st.subheader("Filtered orders")
st.write("Showing", len(data), "orders")
st.dataframe(data.head(200))
