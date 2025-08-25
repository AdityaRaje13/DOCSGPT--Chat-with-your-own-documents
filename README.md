# 📚 DocsGPT — Chat with Your Own Documents

**DocsGPT** My project is called DocsGPT – Chat with Your Documents. It’s an intelligent document assistant where users can upload PDF files and ask questions in natural language, and the system provides accurate, context-based answers.

The main motivation behind this project was data security and integrity. Many companies don’t want to upload their confidential product documents or company data to third-party AI tools like ChatGPT. So I designed a solution where the processing happens locally with FAISS as the vector database and Google’s Generative AI APIs integrated via LangChain. This way, the company’s documents stay private and are never exposed externally.

Here’s how the system works technically:

* PDF Handling – I use PyPDF2 to extract raw text from uploaded documents.

* Text Chunking – The text is split into smaller overlapping chunks using LangChain’s CharacterTextSplitter to maintain context.

* Embeddings & Vector Store – Each chunk is converted into embeddings using Google Generative AI embeddings and stored in FAISS, which allows fast and secure similarity search.

* Question Answering – When a user asks a question, relevant chunks are retrieved from FAISS and passed into Gemini 1.5 Flash via LangChain’s QA chain, with a prompt that ensures only context-based answers are generated.

* Frontend & UI – I used Streamlit for the user interface, where I added styled Q&A cards, animations, and a responsive layout for a better user experience.

From a business perspective, this tool can be extremely useful for onboarding freshers or beginners in a company. Instead of asking seniors or manually searching long documents, they can simply upload training manuals, product documents, or internal guides, and get instant, accurate answers while ensuring the data never leaves the company’s environment.

In short, my project combines AI + Security + Usability — making it practical for real enterprise use cases while also demonstrating my skills in Python, Streamlit, LangChain, embeddings, FAISS, and Generative AI APIs.

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
```
docsgpt/
├── app.py # Main Streamlit application
├── htmlTemplates.py # HTML & CSS templates for custom styling
├── .env # Environment variables (not tracked in Git)
├── requirements.txt # List of Python dependencies
├── README.md # Project documentation
├── faiss_index/ # Generated FAISS vector store for embeddings
```
