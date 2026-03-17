from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

#An embedding is essentially a long list of numbers (a vector) that represents the meaning of a chunk. 
# If two chunks discuss "Software Engineering," their vectors will be mathematically "close" to each other.
def generate_embeddings(chunks):
    processed_data = []

    text = [chunk.page_content for chunk in chunks]
    
    embeddings = model.encode(text)
    
    for i,doc in enumerate(chunks):
        processed_data.append({
            "text": doc.page_content,
            "metadata": doc.metadata,
            "embedding": embeddings[i].tolist()
        })
    
    return processed_data
