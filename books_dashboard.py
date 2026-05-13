# Author  : Harsh Pandey
# Project : Books Dashboard — CodeAlpha Internship Task 1

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Books Dashboard — Harsh Pandey", page_icon="📚", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("books_dataset.csv")

df = load_data()

st.title("📚 Books Scraping Dashboard")
st.caption("CodeAlpha Internship — Task 1 | Author: Harsh Pandey")
st.divider()

st.sidebar.header("🔍 Filters")
price_min, price_max = st.sidebar.slider("Price Range (£)", float(df.price_gbp.min()), float(df.price_gbp.max()), (float(df.price_gbp.min()), float(df.price_gbp.max())))
rating_filter = st.sidebar.multiselect("Rating", sorted(df.rating.unique()), default=sorted(df.rating.unique()), format_func=lambda x: "⭐"*x)

filtered = df[(df.price_gbp >= price_min) & (df.price_gbp <= price_max) & (df.rating.isin(rating_filter))]

c1,c2,c3,c4 = st.columns(4)
c1.metric("📖 Total Books", len(filtered))
c2.metric("💰 Avg Price", f"£{filtered.price_gbp.mean():.2f}")
c3.metric("⭐ Avg Rating", f"{filtered.rating.mean():.1f}/5")
c4.metric("✅ In Stock", int(filtered.in_stock.sum()))

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("Rating Distribution")
    fig, ax = plt.subplots()
    rc = filtered.rating.value_counts().sort_index()
    ax.bar([str(r)+"★" for r in rc.index], rc.values, color=["#e74c3c","#e67e22","#f1c40f","#2ecc71","#27ae60"][:len(rc)])
    st.pyplot(fig)

with col2:
    st.subheader("Price Distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(filtered.price_gbp, bins=25, color="steelblue", edgecolor="white")
    ax2.axvline(filtered.price_gbp.mean(), color="red", linestyle="--", label=f"Avg: £{filtered.price_gbp.mean():.2f}")
    ax2.legend()
    st.pyplot(fig2)

st.divider()
st.subheader(f"📋 Books List ({len(filtered)} results)")
display = filtered.copy()
display["rating"] = display["rating"].apply(lambda x: "⭐"*x)
display["in_stock"] = display["in_stock"].apply(lambda x: "✅" if x else "❌")
display.columns = ["Title","Price (£)","Rating","In Stock","Page"]
st.dataframe(display, use_container_width=True, hide_index=True)
