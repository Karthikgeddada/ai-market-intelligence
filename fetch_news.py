import requests
import feedparser


def get_news(category):

    queries = [
        category,
        category + " news",
        category + " industry",
        category + " market",
        category + " business"
    ]

    headers = {"User-Agent": "Mozilla/5.0"}

    articles = []

    for q in queries:

        query = q.replace(" ", "+")

        url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"

        try:
            response = requests.get(url, headers=headers)
            feed = feedparser.parse(response.content)

            for entry in feed.entries:

                title = entry.title

                summary = ""

                if hasattr(entry, "summary"):
                    summary = entry.summary

                articles.append({
                    "title": title,
                    "summary": summary,
                    "url": entry.link
                })

        except:
            continue

    return articles