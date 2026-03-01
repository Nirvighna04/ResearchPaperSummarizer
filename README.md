# 📄 Research Paper Summarizer

A Streamlit web app that summarizes research papers (PDFs) using **LangChain** and **DeepSeek-R1** via Together AI.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features

- Upload any research paper as a PDF
- Automatically extracts and chunks long documents
- Summarizes using DeepSeek-R1 (via Together AI + LangChain)
- Download the summary as a `.txt` file
- Clean, simple UI built with Streamlit

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **PDF Parsing:** PyMuPDF (fitz)
- **LLM Orchestration:** LangChain
- **AI Model:** DeepSeek-R1 via Together AI

---

## ⚙️ Setup & Installation

1. **Clone the repo**
```bash
   git clone https://github.com/Nirvighna04/ResearchPaperSummarizer.git
   cd research-paper-summarizer
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Set your API key**

   Create a `.env` file in the root directory:
```
   TOGETHER_API_KEY=your_api_key_here
```
   Or set it directly as an environment variable.

4. **Run the app**
```bash
   streamlit run app.py
```

---

## 📁 Project Structure
```
research-paper-summarizer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Files to exclude from Git
└── README.md           # Project documentation
```

---

## 🔑 Getting a Together AI API Key

1. Sign up at [together.ai](https://www.together.ai/)
2. Navigate to API Keys in your dashboard
3. Copy your key and add it to your `.env` file

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---
