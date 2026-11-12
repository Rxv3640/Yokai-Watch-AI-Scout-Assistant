# Yokai-Watch-AI-Scout-Assistant

## Project Overview
This Retrieval Augmented Generation(RAG) Project is based on a tv show called Yokai Watch. This project acts as a chatbot for the user to ask questions about specific Yokai characters. The chatbot will generate information related to the specific Yokai character to the user.



## Project Structure

```text
yokai-rag-assistant/
│
├── data/
│   └── yokai_database.json    # Yokai knowledge base
│
├── ingestion/
│   ├── load_data.py           # Loads and preprocesses the JSON data
│   └── vector_store.py        # Builds and stores embeddings
│
├── rag/
│   ├── retriever.py           # Retrieves relevant yokai entries
│   └── generator.py           # Generates answers from retrieved context
│
├── app.py                     # Main application entry point
├── evaluate.py                # Evaluates retrieval/answer quality
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
└── README.md
```
## Technologies used

- Python
- LangChain
- ChromaDB
- Hugging Face embeddings
- Streamlit
- Git
- Github
- VSCode
- Retrieval Augmented Generation (RAG)
