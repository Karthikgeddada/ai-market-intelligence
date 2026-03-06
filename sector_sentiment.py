import pandas as pd
from fetch_news import get_news
from sentiment_analysis import analyze_sentiment


def calculate_sector_sentiment(sectors):

    sector_results = []

    for sector in sectors:

        articles = get_news(sector)

        positive = 0
        negative = 0
        neutral = 0

        for article in articles[:100]:

            text = article["title"] + " " + article["summary"]

            sentiment, score = analyze_sentiment(text)

            if sentiment == "positive":
                positive += 1
            elif sentiment == "negative":
                negative += 1
            else:
                neutral += 1

        total = positive + negative + neutral

        if total == 0:
            label = "Neutral"
        else:

            if positive > negative:
                label = "Bullish"
            elif negative > positive:
                label = "Bearish"
            else:
                label = "Neutral"

        sector_results.append({
            "Sector": sector,
            "Sentiment": label
        })

    return pd.DataFrame(sector_results)