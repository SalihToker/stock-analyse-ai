# Stock Analyse AI

NewsData.io API'den çekilen finans haberlerini FinBERT ile duygu analizine tabi tutarak şirket bazlı genel bir piyasa duygu skoru hesaplamakta.

## Özellikler

Finans haberlerini otomatik olarak API üzerinden çekme

Haber metinlerinde şirket isimleri ve CEO'larına göre filtreleme

FinBERT tabanlı duygu analizi ile haberlerin finansal tonunu belirleme

Şirket bazlı duygu skorlarını hesaplayarak piyasa duyarlılığını ölçme

Çoklu sayfa (pagination) desteği ile daha fazla haber çekebilme

---

## Kullanılan Teknolojiler ve Kütüphaneler

- **Python 3.8+**
- `requests` — HTTP istekleri için
- `transformers` — Huggingface Transformers ile FinBERT modeli için
- `scipy` — Softmax fonksiyonu için
- `torch` (PyTorch) — Modelin çalışması için
- **NewsData.io API** — Finans haberleri çekmek için

---

# Depoyu klonla ve dizine geç
git clone https://github.com/SalihToker/stock-analyse-ai.git
cd stock-analyse-ai

# Sanal ortam oluştur ve aktif et
# Windows için:
python -m venv venv
venv\Scripts\activate

# macOS/Linux için:
# python3 -m venv venv
# source venv/bin/activate

# Gerekli paketleri yükle
pip install -r requirements.txt

# main.py içindeki NEWSDATA_API_KEY değişkenine kendi API anahtarını ekle

# Programı çalıştır
python main.py

