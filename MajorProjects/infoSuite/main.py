from flask import Flask, request
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders import PDFPlumberLoader
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
FOLDER_PATH = "db"
MODEL_NAME = "gemini-pro"
TEMPERATURE = 0
gemini = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=TEMPERATURE)
embedding = FastEmbedEmbeddings()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024, chunk_overlap=80, length_function=len, is_separator_regex=False
)

prompt = PromptTemplate.from_template(
    """ 
    <s>
    [TRAIT]
    You are an awesome high IQ Document scanner, your keenness to information and your observation skills make you the best in finding out information from any piece of document, and your years of expertise grant you the power to expand the information as well so that common people can understand it.
    [/TRAIT]
    </s>
    
    [INSTRUCTIONS] 
    {input}
    Context: {context}
    Answer:
    [/INSTRUCTIONS]
    """
)

@app.route("/pdfHunt", methods=["POST"])
def ask_pdf_post():
    json_content = request.json
    query = json_content.get("query")

    vector_store = Chroma(persist_directory=FOLDER_PATH, embedding_function=embedding)
    # Guys, A retriever is a component that can search for and retrieve documents from the vector store based on a given query.

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        # `k`: This specifies the number of top documents to retrieve. Here, it is set to 5, meaning the retriever will return the top 5 documents that meet the similarity score threshold.
        # `score_threshold`: This sets the minimum similarity score a document must have to be considered relevant. Here, it is set to 0.1, meaning only documents with a similarity score of 0.1 or higher will be retrieved.
        search_kwargs={"k": 5, "score_threshold": 0.1},
    )

    document_chain = create_stuff_documents_chain(gemini, prompt)
    chain = create_retrieval_chain(retriever, document_chain)

    result = chain.invoke({"input": query})
    print(result)

    return {"answer": result["answer"]}

@app.route("/pdfUpload", methods=["POST"])
def pdf_post():
    all_pdfs = []  # I had listed all the pdfs stored in the pdf folder here with full path name inside the list, I have deleted the pdf/ folder since I didn't have use of it.
    all_docs = []
    all_chunks = []

    for pdf_path in all_pdfs:
        file_name = os.path.basename(pdf_path)
        save_file = os.path.join("pdf", file_name)
        print(f"Processing file: {file_name}")

        loader = PDFPlumberLoader(save_file)
        docs = loader.load_and_split()
        print(f"docs len={len(docs)}")

        chunks = text_splitter.split_documents(docs)
        print(f"chunks len={len(chunks)}")

        all_docs.extend(docs)
        all_chunks.extend(chunks)

    vector_store = Chroma.from_documents(
        documents=all_chunks, embedding=embedding, persist_directory=FOLDER_PATH
    )
    vector_store.persist()

    return {"status": "Successfully Uploaded"}

def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == "__main__":
    start_app()