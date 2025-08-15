# DOCSGPT--Chat-with-your-own-documents

* Description

  DocsGPT is an interactive web application that allows users to upload PDF documents and ask questions about their content. Powered by AI, it processes uploaded PDFs, extracts text, and provides detailed answers   to user queries using natural language processing and vector search. The application features a modern, user-friendly interface with a welcome message, a sidebar for document uploads, and a question-answer        display with a thinking animation for a seamless user experience.
  This project is ideal for users who need to extract insights from large documents efficiently, such as researchers, students, or professionals working with text-heavy PDFs.

* Technologies Used

Python: Core programming language for backend logic and processing.
Streamlit: Framework for building the interactive web interface.
Google Generative AI: Provides embeddings and language model capabilities for text processing and question answering.
LangChain: Facilitates the creation of conversational AI chains and vector stores.
FAISS: Efficient library for similarity search and vector storage.
PyPDF2: Used for extracting text from PDF files.
Python-dotenv: Manages environment variables for secure API key handling.

* Python Modules Used
The following Python modules are imported in the project:

os: For accessing environment variables.
streamlit: For building the web application interface.
google.generativeai: For interacting with Google's AI models.
langchain_google_genai: Provides LangChain integrations for Google Generative AI (specifically GoogleGenerativeAIEmbeddings and ChatGoogleGenerativeAI).
dotenv: For loading environment variables from a .env file.
PyPDF2: For reading and extracting text from PDF files.
langchain.vectorstores: For creating and managing vector stores with FAISS.
langchain.text_splitter: For splitting text into chunks for processing.
langchain.chains.question_answering: For loading the question-answering chain.
langchain.prompts: For creating prompt templates for the AI model.

* Example requirements.txt:

streamlit==1.39.0
google-generativeai==0.8.3
langchain-google-genai==2.0.0
python-dotenv==1.0.1
PyPDF2==3.0.1
langchain==0.3.0
faiss-cpu==1.8.0

* Usage

Upload PDFs: Use the sidebar to upload one or more PDF files.
Process Documents: Click the "Process Documents" button to extract and index the text.
Ask Questions: Enter a question in the text input field to receive detailed answers based on the uploaded documents.
View Answers: Questions and answers are displayed clearly, with a thinking animation shown during processing.

* Features

1. Upload multiple PDFs and extract text for querying.
2. Modern UI with a welcome box, styled header with books emoji (📚), and a responsive design.
3. Thinking animation during query processing for better user experience.
4. Sidebar with PDF upload tips that disappear after document processing.
5. Efficient vector search using FAISS for fast and accurate answers.

Project Structure
docsgpt/
├── app.py              # Main application file
├── htmlTemplates.py    # CSS and HTML templates for styling
├── .env                # Environment variables (not tracked in Git)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── faiss_index/        # Directory for FAISS vector store (generated)

