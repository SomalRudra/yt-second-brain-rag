#  when the user asks a question or a query, 
#  we will convert the question into a vector using the 
#  same embedding model, and 
#  then we will search for the most similar vectors 
#  in the vector store, and then we will retrieve the 
#  corresponding chunks of text that are associated
#   with those vectors, and then we will use those chunks of text 
#   as context to answer the user's question.
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')
db_client = chromadb.PersistentClient(path="./chroma_db")
collection = db_client.get_or_create_collection(name="youtube_transcripts")

def retrieve_context(query, n_result=10):
    query_embedding = model.encode(query).tolist()

    #find the most similar vectors in the vector store using the query embedding, and retrieve the corresponding chunks of text.
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_result,
    )
    text_that_has_context = results['documents'][0]
    context = "\n---\n".join(text_that_has_context)

    metadatas = results['metadatas'][0]

    return context, metadatas