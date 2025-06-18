import requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch

# 🔧 NewsData.io API Ayarları
NEWSDATA_API_KEY = "pub_9a71357a29ca40c88e66b6058fd85d15"  # <-- BURAYA kendi API anahtarını yaz
NEWSDATA_ENDPOINT = "https://newsdata.io/api/1/news"

# 🔧 Şirketler ve CEO'lar
companies = {
     "Apple": "Tim Cook",
    "Tesla": "Elon Musk",
    "Google": "Sundar Pichai",
    "Amazon": "Andy Jassy",
    "Microsoft": "Satya Nadella"
}
geopolitics_keywords = ["us-china", "tariff", "regulation", "sanction", "conflict", "war", "embargo", "EU"]

# 🧠 FinBERT modeli
tokenizer = AutoTokenizer.from_pretrained("yiyanghkust/finbert-tone")
model = AutoModelForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone")

def analyze_sentiment(text):
    if not text.strip():
        return 0.0
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        probs = softmax(outputs.logits.numpy()[0])
        score = float(probs[0] - probs[2])
        return round(score, 2)
    except Exception as e:
        print("Sentiment analizi hatası:", e)
        return 0.0

def extract_related_companies(text):
    text = text.lower()
    matched = set()
    for name, ceo in companies.items():
        if name.lower() in text or ceo.lower() in text:
            matched.add(name)
    for keyword in geopolitics_keywords:
        if keyword in text:
            matched.update(companies.keys())
    return matched

def fetch_news(query, max_pages=1):
    articles = []
    next_page = None
    base_params = {
        "apikey": NEWSDATA_API_KEY,
        "q": query,
        "language": "en"
    }

    for page_num in range(max_pages):
        print(f"[fetch_news] → Sayfa {page_num + 1} için istek gönderiliyor")

        params = base_params.copy()
        if next_page:
            params["page"] = next_page

        response = requests.get(NEWSDATA_ENDPOINT, params=params)
        print(f"[fetch_news] Yanıt kodu: {response.status_code}")
        print(f"[fetch_news] Yanıt içeriği: {response.text[:300]}...")

        if response.status_code != 200:
            print("API Hatası:", response.text)
            break

        data = response.json()
        results = data.get("results", [])
        if not results:
            print("[fetch_news] ⚠️ Hiç haber bulunamadı.")
            break

        articles.extend(results)
        next_page = data.get("nextPage")
        if not next_page:
            break

    return articles



def fetch_and_score():
    scores = {name: 0.0 for name in companies}

    for company, ceo in companies.items():
        query = f"{company} OR {ceo}"
        print(f"\n🔍 Haber aranıyor: {query}")
        articles = fetch_news(query, max_pages=1)  # her şirket için ayrı sayfa

        for art in articles:
            title = art.get("title", "")
            desc = art.get("description", "")
            url = art.get("link", "")
            content = f"{title}. {desc}"

            related = extract_related_companies(content)
           # if company not in related:
            #    continue

            score = analyze_sentiment(content)

            print(f"\n📰 {title}")
            print(f"🔗 {url}")
            print(f"🎯 Sentiment: {score:+.2f} — Affected: {', '.join(related)}")

            scores[company] += score

    print("\n📊 Şirket Bazlı Toplam Skorlar:")
    for c, s in scores.items():
        print(f"{c}: {s:+.2f}")

if __name__ == "__main__":
    fetch_and_score()