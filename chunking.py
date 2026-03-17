from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# This function takes a list of raw snippets and chunks them into smaller pieces using the RecursiveCharacterTextSplitter from the langchain library.
def chunk_text(raw_snippets, chunk_size=400, chunk_overlap=100):
    text = "\n".join([s.text for s in raw_snippets])
    docs = [
        Document(
            page_content=s.text,
            metadata={"start": s.start}
        )
        for s in raw_snippets
    ]
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size, 
        chunk_overlap= chunk_overlap,
        separators=["\n\n", "\n", "."," ", ""])

    # while it is splitting, it will also keep track of the metadata (start time) for each chunk, so that we can later use it to retrieve the original timestamp of the chunk.
    chunk_docs = splitter.split_documents(docs)
    return chunk_docs
    