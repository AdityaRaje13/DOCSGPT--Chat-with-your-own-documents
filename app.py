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
from htmlTemplates import css, bot_template, user_template


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

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)  # fixed model name
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)

    return chain


# Handle user query
def handle_userInput(query):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Fixed: allow dangerous deserialization
    new_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    docs = new_db.similarity_search(query)

    chain = get_conversation_chain()

    # Display thinking animation using a placeholder
    thinking_placeholder = st.empty()
    with thinking_placeholder.container():
        st.markdown('<div class="thinking"><span></span><span></span><span></span></div>', unsafe_allow_html=True)
    
    response = chain(
        {"input_documents": docs, "question": query},
        return_only_outputs=True
    )

    # Clear thinking animation
    thinking_placeholder.empty()

    # Display question and answer directly
    st.markdown(f"""
    <div class="question-answer">
        <h3 class="question">Question: {query}</h3>
        <div class="answer">{response["output_text"]}</div>
    </div>
    """, unsafe_allow_html=True)


def main():
    load_dotenv()

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    st.set_page_config(page_title="DocsGPT- Chat with your documents", page_icon=":books:")

    st.markdown(css, unsafe_allow_html=True)

    # Session state to track if documents are processed
    if "docs_processed" not in st.session_state:
        st.session_state.docs_processed = False

    # Header with background color and books emoji
    st.markdown("""
    <div class="header-container">
        <h1>DocsGPT - Chat with Your Documents <span class="books-emoji">📚</span></h1>
        <p>Ask questions about your uploaded documents and get detailed answers.</p>
    </div>
    """, unsafe_allow_html=True)

    query = st.text_input("Ask your Question:", key="query_input")

    # Display welcome box only if no question has been asked
    if not query:
        st.markdown("""
        <div class="welcome-box">
            <h2>Welcome to DocsGPT</h2>
            <p>Upload your PDF documents in the sidebar and start asking questions to get insightful answers.</p>
        </div>
        """, unsafe_allow_html=True)

    if query:
        handle_userInput(query)

    with st.sidebar:
        st.header("Upload your documents here : ")

        docs = st.file_uploader("Upload PDF Files:", accept_multiple_files=True, type=["pdf"])

        if st.button("🚀 Submit & Process", key="process", help="Click to process uploaded documents"):
            if docs:
                with st.spinner("Processing documents..."):
                    # Extract text from pdfs
                    raw_text = get_textFrom_pdfs(docs)

                    # Create chunks of pdfs
                    text_chunks = get_text_chunks(raw_text)

                    # Create vector store and embeddings
                    get_vectorstore(text_chunks)

                    st.session_state.docs_processed = True
                    st.success("Documents processed successfully! You can now ask questions.")
            else:
                st.warning("Please upload at least one PDF file.")

        # Show tips section only if documents are not processed
        if not st.session_state.docs_processed:
            st.markdown("""
            <div class="tips-section">
                <h3>PDF Upload Tips</h3>
                <ul>
                    <li>Upload clear, text-based PDFs for best results.</li>
                    <li>Multiple files can be uploaded at once.</li>
                    <li>Ensure files are not password-protected.</li>
                    <li>Large files may take longer to process.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
