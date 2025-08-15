# 📚 DocsGPT — Chat with Your Own Documents

**DocsGPT** is an interactive web application that lets you upload PDF documents and ask questions about their content.  
Powered by AI, it processes uploaded PDFs, extracts text, and provides detailed answers using **natural language processing** and **vector search**.

This tool is perfect for **researchers, students, or professionals** who need to quickly extract insights from large, text-heavy PDFs.

---

## 🚀 Features

- 📂 **Upload multiple PDFs** and extract their text for querying.
- 🎨 **Modern UI** with a welcome message, styled header, and responsive design.
- ⏳ **Thinking animation** during query processing for a smooth experience.
- 📝 **Sidebar with PDF upload tips**, which disappear after processing.
- ⚡ **Efficient vector search** using **FAISS** for fast and accurate answers.

---

## 🛠️ Technologies Used

- **Python** — Core backend logic and processing.
- **Streamlit** — Interactive web application framework.
- **Google Generative AI** — Embeddings & language model capabilities.
- **LangChain** — Conversational AI chains and vector stores.
- **FAISS** — Efficient similarity search and vector storage.
- **PyPDF2** — Extract text from PDF files.
- **python-dotenv** — Manage environment variables securely.

---

## 📦 Python Modules Used

- `os` — Access environment variables.
- `streamlit` — Build the UI.
- `google.generativeai` — Interact with Google AI models.
- `langchain_google_genai` — LangChain integrations for Google Generative AI.
- `dotenv` — Load environment variables from `.env`.
- `PyPDF2` — Read and extract PDF text.
- `langchain.vectorstores` — Create/manage FAISS vector stores.
- `langchain.text_splitter` — Split text into chunks.
- `langchain.chains.question_answering` — Load the Q&A chain.
- `langchain.prompts` — Create AI model prompts.

---

## 📂 Project Structure

docsgpt/
├── app.py # Main Streamlit application
├── htmlTemplates.py # HTML & CSS templates for custom styling
├── .env # Environment variables (not tracked in Git)
├── requirements.txt # List of Python dependencies
├── README.md # Project documentation
├── faiss_index/ # Generated FAISS vector store for embeddings
