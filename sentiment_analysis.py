from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

model_name = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

sentiment_model = pipeline(
    "sentiment-analysis",
    model=model,
    tokenizer=tokenizer
)

def analyze_sentiment(text):

    if text is None or len(text.strip()) == 0:
        return "neutral", 0

    try:
        result = sentiment_model(text[:512])[0]

        label = result["label"].lower()
        score = float(result["score"])

        return label, score

    except:
        return "neutral", 0