# Yokai-Watch-AI-Scout-Assistant

- Project Overview
This Retrieval Augmented Generation(RAG) Project is based on a tv show called Yokai Watch. This project acts as a chatbot for the user to ask questions about specific Yokai characters. The chatbot will generate information related to the specific Yokai character to the user.



- Project Structure

yokai-rag-assistant/
│
├── data/
│   └── yokai_database.json
│
├── ingestion/
│   ├── load_data.py
│   └── vector_store.py
│
├── rag/
│   ├── retriever.py
│   └── generator.py
│
├── app.py
├── evaluate.py
├── requirements.txt
├── .env
└── README.md

