import chromadb
from google import genai
from src.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


db = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = db.get_or_create_collection(
    name="support_docs"
)



def embed(text):

    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return result.embeddings[0].values



def add_document(name, text):

    vector = embed(text)

    collection.add(
        ids=[name],
        documents=[text],
        embeddings=[vector],
        metadatas=[
            {
                "source": name
            }
        ]
    )



def search(query):

    vector = embed(query)


    result = collection.query(
    query_embeddings=[vector],
    n_results=1
)


    return result