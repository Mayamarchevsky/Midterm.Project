# streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title("Fashion Boost Analysis")

# Load dataset
CSV_PATH = "summer-products.csv"

@st.cache_data
def load_data():
    return pd.read_csv(CSV_PATH)

df = load_data()

# Preview dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Plot 1: Boxplot - Units Sold by Ad Boost
st.subheader("Units Sold by Ad Boost Usage")
fig1, ax1 = plt.subplots(figsize=(9, 9))
sns.boxplot(x='uses_ad_boosts', y='units_sold', data=df, palette="Set2", ax=ax1)
ax1.set_title("Units Sold by Ad Boost Usage")
ax1.set_xlabel("Used Ad Boost")
ax1.set_ylabel("Units Sold")
st.pyplot(fig1)

# Plot 2: Violinplot - Product Rating by Ad Boost
st.subheader("Product Rating Distribution by Ad Boost")
fig2, ax2 = plt.subplots(figsize=(9, 9))
sns.violinplot(x='uses_ad_boosts', y='rating', data=df, palette="Set3", ax=ax2)
ax2.set_title("Product Rating Distribution by Ad Boost")
ax2.set_xlabel("Used Ad Boost")
ax2.set_ylabel("Rating")
st.pyplot(fig2)

# Plot 3: Scatterplot - Rating vs Units Sold, hue by Ad Boost
st.subheader("Rating vs Units Sold by Ad Boost")
fig3, ax3 = plt.subplots(figsize=(9, 9))
sns.scatterplot(data=df, x='rating', y='units_sold', hue='uses_ad_boosts', palette="coolwarm", alpha=0.6, ax=ax3)
ax3.set_title("Rating vs Units Sold by Ad Boost")
ax3.set_xlabel("Product Rating")
ax3.set_ylabel("Units Sold")
st.pyplot(fig3)
