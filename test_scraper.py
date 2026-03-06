from scrape_articles import scrape_article

url = "https://finance.yahoo.com/"

text = scrape_article(url)

print(text[:1000])