from fastapi import FastAPI

from chunking import chunk_text
from get_transcript import getVideoTranscript
from embedding import generate_embeddings
from vector_store import add_to_vector_store
from retrieve_context import retrieve_context
from generate_answer import generate_answer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Second brain RAG is live!"}

@app.get("/answer")
def answer():
    (transcript, video_id) = getVideoTranscript()
    chunks = chunk_text(transcript)
    embeddings = generate_embeddings(chunks)
    add_to_vector_store(embeddings, video_id)
    query = input("write your query here: ")
    context, metadatas = retrieve_context(query)
    generated_answer = generate_answer(query, context)
    return {"chunks": "got it", "generated_answer": generated_answer}
