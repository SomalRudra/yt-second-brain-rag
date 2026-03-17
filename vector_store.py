import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="youtube_transcripts")

def add_to_vector_store(embeddings, video_id):
    ids = []
    text_list = []
    metadatas = []
    embeddings_list = []

    for i, item in enumerate(embeddings):
        ids.append(f"{video_id}_{i}")
        text_list.append(item["text"])
        metadatas.append(item["metadata"])
        embeddings_list.append(item["embedding"])
    
    
    collection.add(
        ids=ids,
        documents=text_list,
        metadatas=metadatas,
        embeddings=embeddings_list
    )

    print(f"Added {len(embeddings)} chunks to the vector store for video ID: {video_id}")