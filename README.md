# 🕸️ AI Web Scraper & Summarizer

A powerful automation tool that scrapes dynamic web content using Selenium, processes the data with LangChain, and generates intelligent summaries via Google Gemini API. Ideal for researchers, analysts, and developers who need structured summaries of real-time web content.

## 🚀 Features

- 🌐 **Web Scraping with Selenium**  
  Dynamically loads and extracts content from JavaScript-heavy websites.

- 🧠 **Natural Language Processing with LangChain**  
  Modular chain-based architecture to process and structure the scraped content.

- ✨ **Summarization via Gemini API**  
  Generates concise, high-quality summaries from large unstructured text using Google’s Gemini LLM.

- 📦 **Modular & Scalable**  
  Easily extendable for new websites, multiple summarization strategies, and content types.
- 🖥️ **Streamlit Dashboard**
  Beautiful streamlit based UI!

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **BeautifulSoup**
- **Selenium** for dynamic web scraping
- **LangChain** for language model orchestration
- **Google Gemini API** for summarization
- **Chromedriver** or headless browser (e.g., Chrome, Firefox)
- **dotenv / argparse** for environment configuration
- **Streamlit** For UI!

---

## 📁 Project Structure

```bash
.
├── app.py                # Entry point i.e Streamlit app
├── scraper.py            # Selenium,BeautifulSoup-based scraping logic
├── parcer.py             # LangChain + Gemini API summarizer
├── .env                  # Environment variables (API keys, config)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
