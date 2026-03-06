from newspaper import Article

def scrape_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()

        text = article.text

        # ignore very small / empty articles
        if len(text) < 200:
            return None

        return text

    except Exception as e:
        return None