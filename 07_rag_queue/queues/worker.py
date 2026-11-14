from openai import OpenAI
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()

openai_client = OpenAI()

# Vector embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
)

# Get the vector DB data from existing collection in qdrant DB.
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

def process_query(user_query):
    print(f"Processing query: {user_query}")
    search_results = vector_db.similarity_search(query=user_query)

    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}" for result in search_results])

    SYSTEM_PROMPT = f"""You are a helpful assistant that answers user queries based on the available context retrieved from a PDF file
    along with page_contents and page_number.

    You should only answer the user based on the following context and navigate the user to open the right page number to know more.

    Context: 
    {context}
    """

    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    print(f"Answer: {response.choices[0].message.content}")
    return response.choices[0].message.content
