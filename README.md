# 📊 Stock Analyse AI – Financial News Sentiment Analyzer

**Stock Analyse AI** is an AI-powered Python tool that collects real-time financial news about major global companies and analyzes the potential market sentiment impact of those news articles using NLP models like **FinBERT** and **BART**. It summarizes, scores, and generates a report with the most positive and negative news for each company.

---

## 🎯 Objective

To help investors, analysts, and researchers **automatically assess** the potential impact of financial news on major companies using modern NLP techniques.

---

## 🔍 What It Does

- 🔎 Collects recent business news from **NewsData.io API**
- 🧠 Optionally summarizes articles using **BART** (`facebook/bart-large-cnn`)
- 📈 Performs sentiment analysis with **FinBERT** (`yiyanghkust/finbert-tone`)
- 📊 Calculates **weighted impact scores** based on:
  - Company name in title (`×1.2`)
  - CEO name in title (`×1.1`)
  - Critical keywords like "regulation", "lawsuit", "earnings" (`×1.5`)
- 📄 Generates a `.docx` report including:
  - Total sentiment score per company
  - Top 5 most positive & negative articles

---

## 🧪 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core programming |
| [NewsData.io API](https://newsdata.io/) | News source |
| Hugging Face Transformers | FinBERT & BART models |
| FinBERT (`yiyanghkust/finbert-tone`) | Financial sentiment analysis |
| BART (`facebook/bart-large-cnn`) | Summarization (optional) |
| PyTorch | Model execution |
| SciPy (softmax) | Probability normalization |
| requests | API calls |
| python-docx | Word report generation |

---

## 🏢 Tracked Companies

- Apple (Tim Cook)  
- Tesla (Elon Musk)  
- Google (Sundar Pichai)  
- Amazon (Andy Jassy)  
- Microsoft (Satya Nadella)

You can easily add or remove companies from the configuration.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-analyse-ai.git
   cd stock-analyse-ai
   ```
2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Set your NewsData.io API key in the script:

4. Run the Project:
   ```
   python stock_analyse_ai.py
   ```

---

## 📄 Sample Report Output

- **Total news articles analyzed**
- **Final sentiment score per company**
- **Top 5 Positive News**
- **Top 5 Negative News**
- Report saved as: `Stock_Analyse_Rapor_YYYYMMDD_HHMMSS.docx`

---

## 📃 License

This project is intended for **educational and research purposes** only.  
Please review and respect the individual licenses of any third-party APIs and models used (e.g., NewsData.io, Hugging Face Transformers).

---
![Stock_Analyse_Rapor_20250619_123200-1](https://github.com/user-attachments/assets/03a9520d-73eb-4735-829e-9e1c96936ae5)
