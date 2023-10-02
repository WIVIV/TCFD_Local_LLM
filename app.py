import os
import tempfile
import streamlit as st 

from PIL import Image
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

#Create Vector store
db_path = r'vectorstore\db_faiss'

#Function to clear vector Store on every run. 
def delete_files_in_directory(directory_path):
    files=os.listdir(directory_path)
    for file in files:
        file_path=os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
delete_files_in_directory(db_path)

#Streamlit - image file paths
image = Image.open(r"images\image.jpg")
favicon = Image.open(r"images\favicon.png")

#Streamlit - Page title
st.set_page_config(page_title="TCFD Report Analyser",
                   page_icon=favicon,
                   initial_sidebar_state="collapsed",
                   layout="wide"
                   )
st.image(image, width=1500)
st.title("TCFD Disclosure Analyser")

#Streamlit - file upload
uploaded_files = st.sidebar.file_uploader("Upload your pdf Documents", accept_multiple_files=True, type="pdf")

#Streamlit - TCFD Overview
st.write("[TCFD Overview](https://assets.bbhub.io/company/sites/60/2022/12/tcfd-2022-overview-booklet.pdf)")

#Streamlit - Tabs
tab1, tab2 = st.tabs(["TCFD Questions","Custom Questions"])

#Local LLM
def load_llm():
    # Load the locally downloaded model here
    config = {'gpu_layers':50, 'max_new_tokens':500, 'repetition_penalty':1.1, 'temperature':0}
    llm = CTransformers(
        model = r"D:\Python\Models\TheBlokeLlama-2-13B-Chat-GGML\llama-2-13b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        config=config
    )
    return llm

#Function to generate LLM responses when button is clicked in ST App
def generate_response(uploaded_files, llm, query_text):
    if uploaded_files is not None:
        #Read pdf docs uploaded in ST app
        docs = []
        temp_dir = tempfile.TemporaryDirectory()
        for file in uploaded_files:
            temp_filepath = os.path.join(temp_dir.name, file.name)
            with open(temp_filepath, 'wb') as f:
                f.write(file.getvalue())
            loader = PyPDFLoader(temp_filepath)
            docs.extend(loader.load())
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800, 
            chunk_overlap=20,
            length_function=len,
            separators=['\n']
            )
        texts = text_splitter.split_documents(docs)
        # Embeddings
        embeddings =  HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2',
                                            model_kwargs={'device': 'cuda'})
        # Create a vectorstore from documents
        delete_files_in_directory(db_path)
        vectordb = FAISS.from_documents(texts, embeddings)
        vectordb.save_local(db_path)
        llm = load_llm()

        # Create QA chain
        retriever=vectordb.as_retriever(search_type='mmr', searcch_kwargs={'fetch_k':4, 'lamda_multi':0.05})
        compressor=LLMChainExtractor.from_llm(llm)
        compression_retriever=ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)
        qa = RetrievalQA.from_chain_type(llm=llm, 
                                         chain_type='stuff', 
                                         retriever=compression_retriever,
                                         return_source_documents=True
                                        )
        return qa(query_text)

#TCFD Questions
q1 = "Describe the board’s oversight of climate-related risks and opportunities."
q2 = "Describe management’s role in assessing and managing climate-related risks and opportunities."
q3 = "Describe the climate-related risks and opportunities the organisation has identified over the short, medium, and long term."
q4 = "Describe the impact of climate-related risks and opportunities on the organisation’s businesses, strategy, and financial planning."
q5 = "Describe the resilience of the organisation’s strategy, taking into consideration different climate-related scenarios, including a 2°C or lower scenario."
q6 = "Describe the organisation’s processes for identifying and assessing climate-related risks."
q7 = "Describe the organisation’s processes for managing climate-related risks."
q8 = "Describe how processes for identifying, assessing, and managing climate-related risks are integrated into the organisation’s overall risk management."
q9 = "Describe the metrics used by the organisation to assess climate-related risks and opportunities in line with its strategy and risk management process."
q10 ="Detail the Scope 1, Scope 2, and, if appropriate, Scope 3 greenhouse gas (GHG) emissions, and the related risks."
q11 ="Describe the targets used by the organisation to manage climate-related risks and opportunities and performance against targets."
questions=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11]

#Funciton to display source docs in ST App
def pretty_print_docs(docs):
    print(f"\n{'-' * 100}\n".join([f"Document {i+1}:\n\n\ " + d.page_content for i, d in enumerate(docs)]))

#TCFD LLM Responses
with tab1:
    if st.button('Generate TCFD Resppnses', disabled=not(uploaded_files)):
        for question in questions:
            st.write(f"{question}")
            with st.spinner('Processing...'):
                response = generate_response(uploaded_files, load_llm, question)
                st.info(f"LLM Answer: \n\n {response['result']}") 
                with st.expander("Source data used by LLM:"):
                    extracted_data = [(doc.page_content, doc.metadata) for doc in response["source_documents"]]
                    for page_content, metadata in extracted_data:
                        metadata_souce=metadata.get("source")
                        metadata_source_split=metadata_souce.rsplit('/',1)
                        page_number=metadata.get("page")
                        st.write(f"Text Slice: \n\n{page_content} \n\nDocument: {metadata_source_split}\n\n Page Number: {page_number}\n\n{'-' * 100}")
    else:
        for question in questions:
            st.write(f"{question}")
        
#Custom Questions
with tab2:
    #query text
    result = []
    with st.form('myform', clear_on_submit=False):
        query_text = st.text_input('Enter your question', disabled=not(uploaded_files))
        submitted = st.form_submit_button('Submit', disabled=not(uploaded_files))
        if submitted:
            with st.spinner('Processing...'):
                response = generate_response(uploaded_files, load_llm, query_text)
                result.append(response['result'])
    if len(result):
        st.info(response['result'])