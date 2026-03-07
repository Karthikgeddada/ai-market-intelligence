import streamlit as st
import pandas as pd

from company_detector import get_trending_companies
from fetch_news import get_news
from sentiment_analysis import analyze_sentiment


st.set_page_config(page_title="AI Market Intelligence", layout="wide")

st.title("📊 AI Market Intelligence Dashboard")

st.write("Analyze market sectors using AI-powered news sentiment")


# -----------------------------
# Sector Selection
# -----------------------------

categories = [

    "Finance","Banking","Insurance","Healthcare","Pharmaceuticals",
    "Biotechnology","Agriculture","Food Industry","Energy",
    "Oil and Gas","Renewable Energy","Technology","Artificial Intelligence",
    "Cybersecurity","Semiconductors","Aviation","Space Industry",
    "Automotive","Electric Vehicles","Logistics","Retail","E-commerce",
    "Real Estate","Construction","Telecommunications","Media",
    "Entertainment","Sports Industry","War","Defense","Geopolitics","Cryptocurrency"
]

selected_category = st.selectbox("Choose Sector", categories)


# -----------------------------
# Fetch News
# -----------------------------

articles = get_news(selected_category)

st.write(f"Articles fetched: {len(articles)}")


# -----------------------------
# Trending Companies
# -----------------------------



# -----------------------------
# Sentiment Analysis
# -----------------------------

results = []

for article in articles[:300]:

    text = article["title"] + " " + article["summary"]

    sentiment, score = analyze_sentiment(text)

    results.append({
        "Title": article["title"],
        "Sentiment": sentiment,
        "Confidence": round(score, 2)
    })

df = pd.DataFrame(results)


# -----------------------------
# News Analytics
# -----------------------------

st.header("📰 News Analytics")

st.subheader("Latest News")

st.dataframe(df, use_container_width=True)


# -----------------------------
# Sentiment Distribution
# -----------------------------

st.subheader("📊 Sentiment Distribution")

sentiment_counts = df["Sentiment"].value_counts()

st.bar_chart(sentiment_counts)


# -----------------------------
# Sector Heatmap Button
# -----------------------------

st.header("📊 Sector Heatmap")

if st.button("Generate Sector Heatmap"):

    with st.spinner("Analyzing sector sentiment..."):

        heatmap_sectors = [
            "Finance",
            "Technology",
            "Healthcare",
            "Energy",
            "Automotive",
            "Cryptocurrency"
        ]

        sector_sentiments = []

        for sector in heatmap_sectors:

            sector_articles = get_news(sector)

            positive = 0
            negative = 0
            neutral = 0

            for article in sector_articles[:25]:

                text = article["title"] + " " + article["summary"]

                sentiment, score = analyze_sentiment(text)

                if sentiment == "positive":
                    positive += 1
                elif sentiment == "negative":
                    negative += 1
                else:
                    neutral += 1

            if positive > negative:
                label = "Bullish"
                emoji = "🟢"
            elif negative > positive:
                label = "Bearish"
                emoji = "🔴"
            else:
                label = "Neutral"
                emoji = "🟡"

            sector_sentiments.append({
                "Sector": sector,
                "Sentiment": f"{emoji} {label}"
            })

        sector_df = pd.DataFrame(sector_sentiments)

    st.dataframe(sector_df, use_container_width=True)
