import os
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from htmlTemplates import css_template, bot_template, user_template
import time
import shutil


# Reading text from PDF
def get_textFrom_pdfs(docs):
    text = ""
    for doc in docs:
        pdf_reader = PdfReader(doc)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text    


# Split text into chunks
def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_splitter.split_text(raw_text)


# Create embeddings and vector store 
def get_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")  # unified folder name


# Create conversation chain
def get_conversation_chain():
    prompt_template = """
        Answer the question as detailed as possible from the provided context. Try to reply everything related to the question asked. Make sure to provide the all details
        regarding to that question. You can use bulleted points only if necessary. If there is no data available 
        just say "Answer/information is not available in context, please try with another questions". Don't provide
        the wrong information.\n\n
        Context:\n{context}\n
        Question:\n{question}\n
    """

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)

    return chain


# Handle user query with enhanced UX
def handle_userInput(query):
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.session_state.chat_history.append({"role": "user", "content": query})

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Enhanced thinking animation with placeholder
    thinking_placeholder = st.empty()
    with thinking_placeholder.container():
        st.markdown("""
        <div class="thinking">
            <div class="thinking-content">
                <div class="thinking-text">🤔 Analyzing your question...</div>
                <div class="thinking-dots">
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                </div>
                <div class="thinking-progress"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Add slight delay for better UX
    time.sleep(0.8)
    
    # Load vector store and search
    new_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    docs = new_db.similarity_search(query)

    # Update thinking message
    with thinking_placeholder.container():
        st.markdown("""
        <div class="thinking">
            <div class="thinking-content">
                <div class="thinking-text">🔍 Searching through documents...</div>
                <div class="thinking-dots">
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                </div>
                <div class="thinking-progress"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    time.sleep(0.5)
    
    # Generate response
    with thinking_placeholder.container():
        st.markdown("""
        <div class="thinking">
            <div class="thinking-content">
                <div class="thinking-text">✨ Generating your answer...</div>
                <div class="thinking-dots">
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                    <div class="thinking-dot"></div>
                </div>
                <div class="thinking-progress"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    chain = get_conversation_chain()
    response = chain(
        {"input_documents": docs, "question": query},
        return_only_outputs=True
    )

    # Clear thinking animation
    thinking_placeholder.empty()

    st.session_state.chat_history.append({"role": "assistant", "content": response["output_text"]})


# Entry point
def main():
    load_dotenv()

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    st.set_page_config(
        page_title="DocsGPT - Chat with your documents", 
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize theme in session state
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True  # Default to dark mode

    # Session state to track if documents are processed
    if "docs_processed" not in st.session_state:
        st.session_state.docs_processed = False

    # Set theme variables
    if st.session_state.dark_mode:
        theme_vars = """
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-tertiary: #334155;
            --text-primary: #f1f5f9;
            --text-secondary: #cbd5e0;
            --border: #475569;
            --shadow: rgba(0, 0, 0, 0.3);
            --accent: #60a5fa;
        """
    else:
        theme_vars = """
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-tertiary: #f1f5f9;
            --text-primary: #0f172a;
            --text-secondary: #64748b;
            --border: #e2e8f0;
            --shadow: rgba(0, 0, 0, 0.1);
            --accent: #3b82f6;
        """

    # Inject CSS with theme variables
    full_css = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        :root {{
            {theme_vars}
        }}
        
        /* Global Styles */
        {css_template}
    </style>
    """
    st.markdown(full_css, unsafe_allow_html=True)
    
    # Modern Header with gradient
    st.markdown("""
    <div class="modern-header">
        <h1>DocsGPT - Chat with Your Documents <span class="books-emoji">📚</span></h1>
        <p>Upload your PDF documents and get intelligent answers powered by AI</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create input form
    with st.form(key="query_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        with col1:
            query = st.text_input(
                "Ask your question",
                placeholder="What would you like to know about your documents?",
                key="query_input",
                label_visibility="collapsed"
            )
        with col2:
            submit_button = st.form_submit_button("Ask", use_container_width=True)
            
        # Handle form submission
        if submit_button and query.strip():
            if not os.path.exists("faiss_index"):
                st.error("⚠️ Please upload and process documents first!")
            else:
                handle_userInput(query)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Display chat history
    if "chat_history" in st.session_state and len(st.session_state.chat_history) > 0:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(user_template.replace("{message}", msg["content"]), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{message}", msg["content"]), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Auto-scroll to the answer
        st.markdown("""
        <script>
            setTimeout(function() {
                window.scrollTo(0, document.body.scrollHeight);
            }, 100);
        </script>
        """, unsafe_allow_html=True)
    else:
        # Welcome section
        st.markdown("""
        <div class="welcome-container">
            <h2>Welcome to DocsGPT! 👋</h2>
            <p>Transform your PDF documents into an intelligent knowledge base. Upload your documents and start asking questions to get detailed, accurate answers.</p>
            <div class="welcome-features">
                <div class="feature-card">
                    <div class="feature-icon">📄</div>
                    <div class="feature-title">Upload PDFs</div>
                    <div class="feature-desc">Support for multiple PDF files with text extraction</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🔍</div>
                    <div class="feature-title">Smart Search</div>
                    <div class="feature-desc">AI-powered semantic search through your documents</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💬</div>
                    <div class="feature-title">Natural Chat</div>
                    <div class="feature-desc">Ask questions in plain English and get detailed answers</div>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <div class="feature-title">Fast Results</div>
                    <div class="feature-desc">Get instant responses with relevant context</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Sidebar for document management
    with st.sidebar:
       
        # File uploader
        docs = st.file_uploader(
            "📂 Choose PDF Files",
            accept_multiple_files=True,
            type=["pdf"],
            help="Select one or more PDF files to upload"
        )

        # Process button
        if st.button("🚀 Process Documents", use_container_width=True, type="primary"):
            if docs:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                try:
                    # Step 1: Extract text
                    status_text.text("📄 Extracting text from PDFs...")
                    progress_bar.progress(25)
                    raw_text = get_textFrom_pdfs(docs)
                    
                    # Step 2: Create chunks
                    status_text.text("✂️ Creating text chunks...")
                    progress_bar.progress(50)
                    text_chunks = get_text_chunks(raw_text)
                    
                    # Step 3: Generate embeddings
                    status_text.text("🧠 Generating embeddings...")
                    progress_bar.progress(75)
                    get_vectorstore(text_chunks)
                    
                    # Step 4: Complete
                    status_text.text("✅ Processing complete!")
                    progress_bar.progress(100)
                    
                    st.session_state.docs_processed = True
                    time.sleep(1)
                    status_text.empty()
                    progress_bar.empty()
                    st.success(f"🎉 Successfully processed {len(docs)} document(s)! You can now ask questions.")
                    
                except Exception as e:
                    st.error(f"❌ Error processing documents: {str(e)}")
                    progress_bar.empty()
                    status_text.empty()
            else:
                st.warning("⚠️ Please upload at least one PDF file.")

        # Document status
        st.markdown("---")
        if os.path.exists("faiss_index"):
            st.success("✅ Documents ready for questions!")
            if st.button("🗑️ Clear All Documents", use_container_width=True):
                if os.path.exists("faiss_index"):
                    shutil.rmtree("faiss_index")
                    st.session_state.docs_processed = False
                    st.rerun()
        else:
            st.info("📋 No documents processed yet")

        # Tips section (only show when no documents are processed)
        if not st.session_state.docs_processed:
            st.markdown("""
            <div class="tips-section">
                <h3>Tips for Best Results</h3>
                <ul>
                    <li>Upload clear, text-based PDF files</li>
                    <li>Avoid scanned documents or images</li>
                    <li>Multiple files can be processed together</li>
                    <li>Remove password protection before upload</li>
                    <li>Larger files may take more time to process</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
