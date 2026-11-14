from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

load_dotenv()

pdf_path = Path(__file__).parent / "Nodejs.pdf"

# Load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
# file is loaded by langchain and it will give you documents page by page
documents = loader.load() 

print(documents[12])

# Split the document into chunks of text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    # overlap means how many characters will be get reeated in next chunk, so that we can maintain the context of the document
    # E.g. if you have 3 paragrams and you are reading 1 by 1, somehow you will loose the context of then previous paragraph
    # That's why 200 characters we need to get the context of next paragraph. 
    # e.g. 1 chunk, 2 chunk and 3 chunk --> in 2nd chunk 200 characters will get add from 1st chunk to maintain the context
    chunk_overlap=400,
)

# Split the document into chunks of text
chunks = text_splitter.split_documents(documents=documents)

# Vector embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

# We need to add bridge for vector embeddings to store in qdrant DB.
# Here we have used QdrantVectorStore from langchain_qdrant to store the vector embeddings in qdrant DB.
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

print("Indexing of documents done...")
