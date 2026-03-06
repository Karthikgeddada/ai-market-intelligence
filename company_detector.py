import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")


def get_trending_companies(articles):

    companies = []

    for article in articles:

        text = article["title"]

        doc = nlp(text)

        for ent in doc.ents:

            if ent.label_ == "ORG":
                companies.append(ent.text)

    company_counts = Counter(companies)

    return company_counts.most_common(10)