import streamlit as st
import fitz  # PyMuPDF for extracting text from PDF
import re
import time
from together import Together
from langchain_together import ChatTogether
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate

# Initialize Together AI API
TOGETHER_API_KEY = "a4bbfdc06c30d83c997ade406d4233cf6b26a9fbbf049324b022f39fb0af4f1a"
client = Together(api_key=TOGETHER_API_KEY)

# Initialize LangChain Chat Model
llm = ChatTogether(
    model_name="deepseek-ai/DeepSeek-R1",
    together_api_key=TOGETHER_API_KEY,
    temperature=0.6,
)

# LangChain Prompt Template
summary_prompt = PromptTemplate.from_template(
    """You are an AI assistant that summarizes documents concisely. 
    Given the following text, generate a summary:

    {text}

    Summary:"""
)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = "\n".join(page.get_text("text") for page in doc)
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""

# Function to chunk long texts
def chunk_text(text, chunk_size=5000):
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

# Function to summarize text using LangChain & Together AI
def summarize_text(text):
    chunks = chunk_text(text)
    summaries = []

    for i, chunk in enumerate(chunks):
        formatted_prompt = summary_prompt.format(text=chunk)
        try:
            with st.spinner(f"Processing chunk {i + 1} of {len(chunks)}..."):
                response = llm([HumanMessage(content=formatted_prompt)])
                summaries.append(response.content)
                time.sleep(200)  # Comply with rate limits
        except Exception as e:
            st.error(f"Error summarizing text: {e}")
            break

    return "\n\n".join(summaries)

# Function to clean summary output
def clean_summary(summary):
    summary = re.sub(r"<think>.*?</think>", "", summary, flags=re.DOTALL)
    summary = summary.replace("Summary:", "").strip()
    return summary

# Streamlit UI
st.set_page_config(page_title="PDF Summarization", layout="wide")
st.title("📄 PDF Summarization with LangChain + DeepSeek-R1")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    st.info("Extracting text from PDF...")
    pdf_text = extract_text_from_pdf(uploaded_file)

    if pdf_text:
        if len(pdf_text) > 5000:
            st.warning("Long document detected! Using chunked summarization.")

        st.success("Text extraction complete! Generating summary...")
        summary = summarize_text(pdf_text)
        if summary:
            summary = clean_summary(summary)
            st.subheader("🔹 Summarized Content")
            st.write(summary)

            # Download summarized text
            st.download_button("Download Summary", summary, "summary.txt", "text/plain")
        else:
            st.error("Failed to generate a summary. Please try again.")
