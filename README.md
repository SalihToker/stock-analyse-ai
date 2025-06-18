# Stock Analyse AI

NewsData.io API'den çekilen finans haberlerini FinBERT ile duygu analizine tabi tutarak şirket bazlı genel bir piyasa duygu skoru hesaplamakta.

---

## Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3.8+**
- `requests` — HTTP istekleri için
- `transformers` — Huggingface Transformers ile FinBERT modeli için
- `scipy` — Softmax fonksiyonu için
- `torch` (PyTorch) — Modelin çalışması için
- **NewsData.io API** — Finans haberleri çekmek için

---

## Kurulum

1. Projeyi klonla:

git clone https://github.com/SalihToker/stock-analyse-ai.git
cd stock-analyse-ai

2. Sanal ortam oluşturup aktif et:
python -m venv venv
venv\Scripts\activate

3. Gerekli paketler
pip install -r requirements.txt

