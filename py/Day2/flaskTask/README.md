# 📄 InfoSuite

Welcome to **InfoSuite**! This Flask application is designed to help you upload and query PDF documents using advanced AI techniques. 🚀

## Features

- 📤 **Upload PDFs**: Easily upload your PDF documents to the server.
- 🔍 **Query PDFs**: Ask questions about the content of your PDFs and get intelligent answers.
- 🤖 **AI-Powered**: Utilizes Google Generative AI and FastEmbed embeddings for accurate and efficient document retrieval and analysis.
- ⨯ **Vectored**: Makes use of vector databases like ChromaDB to upload and forget about pdfs hassle free.
- 🔄 **RAG (Retrieval-Augmented Generation)**: Combines retrieval of relevant document chunks with generative AI to provide precise and contextually accurate answers.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- 🐍 Python 3.7+
- 📦 Your own Gemini API Key
- 🌐 Flask
- 🛠 dotenv

### Installation

1. **Clone the repository**:
    If you don't know how to clone a repo yet, what are you doing?

2. **Install dependencies**:
    `pip3 install -r requirements.txt`

3. **Set up environment variables**:
    Create a `.env` file in the root directory and add your environment variables:
    ```env
    GOOGLE_API_KEY = <Your Google API Key>
    ```

### Running the Application

To start the Flask application, run:
    `python3 main.py`
The app will be available at `http://localhost:8080`. 🌐

## API Endpoints

### Upload PDFs

- **Endpoint**: `/pdfUpload`
- **Method**: `POST`
- **Description**: Uploads PDF documents to the server. (*Make sure you list down all the pdf in a pdf/ folder, and then copy-paste the paths in the allPdfs List.)

### Query PDFs

- **Endpoint**: `/pdfHunt`
- **Method**: `POST`
- **Description**: Queries the uploaded PDF documents and returns an intelligent answer.

## How It Works

1. 📥 **Upload PDFs**: When you upload PDFs, the application processes and splits them into manageable chunks using `RecursiveCharacterTextSplitter`.
2. 🧠 **Store Embeddings**: The chunks are then embedded using `FastEmbedEmbeddings` and stored in a `Chroma` vector store.
3. 🤔 **Query PDFs**: When you query the PDFs, the application retrieves the most relevant chunks using a similarity score threshold and generates an answer using `ChatGoogleGenerativeAI`.
4. 🔄 **RAG**: Combines the retrieval of relevant chunks with generative AI to provide precise and contextually accurate answers.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) 🌐
- [LangChain](https://github.com/langchain/langchain) 🔗
- [Google Generative AI](https://cloud.google.com/ai-platform) 🤖
- [Chroma](https://github.com/chroma-core/chroma) 🖌️

---

Made with ❤️ by [Arreyan Hamid](https://github.com/GriffinBlackbirdd)
For any inquiries or feedback, please contact [arreyanhamid@icloud.com](mailto:arreyanhamid@icloud.com).
