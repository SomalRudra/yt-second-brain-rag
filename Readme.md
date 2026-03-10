second_brain_rag/
├── app.py           # FastAPI backend entry point
├── rag_engine.py    # Core RAG logic
├── chunking.py      # Text chunking code
├── embedding.py     # Embedding logic
├── vector_store.py  # Chroma / FAISS integration
├── prompts.py       # Prompt templates for LLM
├── transcripts/     # Folder for text files
├── requirements.txt # List Python packages
└── README.md        # Project documentation


Run command

uvicorn app:app --reload
