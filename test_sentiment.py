from sentiment_analysis import analyze_sentiment

text = """
Nvidia stock surged after the company reported strong earnings and increased demand for AI chips.
"""

label, score = analyze_sentiment(text)

print("Sentiment:", label)
print("Confidence:", score)