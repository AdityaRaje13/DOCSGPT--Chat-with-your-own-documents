import streamlit as st
from dotenv import load_dotenv 
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceEndpoint
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


# Create vectorstore from chunks
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")
    return FAISS.from_texts(texts=text_chunks, embedding=embeddings)


# Create conversation chain using HuggingFaceEndpoint
def get_conversation_chain(vector_store):
    hf_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

    llm = HuggingFaceEndpoint(
        repo_id="google/flan-t5-base",
        task="text2text-generation",
        huggingfacehub_api_token=hf_token,
        temperature=0.5,
        max_new_tokens=256
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )

    return conversation_chain


# Handle user query
def handle_userInput(query):
    if st.session_state.conversation:
        response = st.session_state.conversation({'question': query})
        st.write(bot_template.replace("{{MSG}}", response['answer']), unsafe_allow_html=True)


def main():
    load_dotenv()

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    st.set_page_config(page_title="DocsGPT- Chat with your documents", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    st.header("DocsGPT- Chat with your documents :books:")
    st.write("Upload your files and ask whatever you want....")

    query = st.text_input("Ask me a Question : ")

    if query and st.session_state.conversation:
        handle_userInput(query)
        st.write(user_template.replace("{{MSG}}", query), unsafe_allow_html=True)

    with st.sidebar:
        st.header("Upload your documents here")
        docs = st.file_uploader("Upload Files : ", accept_multiple_files=True)

        if st.button("Process", key="process") and docs:
            with st.spinner("Processing..."):
                raw_text = get_textFrom_pdfs(docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vector_store)
                st.success("Documents processed! You can now ask questions.")


if __name__ == '__main__':
    main()
