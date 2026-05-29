import os
from pathlib import Path
from langchain.document_loaders import (TextLoader, PyPDFLoader)
from dotenv import load_dotenv
load_dotenv()
import tempfile

def load_text_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a sample text file for testing.")
        temp_file_path = temp_file.name
    
    try:
        loader = TextLoader(temp_file_path)
        documents = loader.load()

        for doc in documents:
            print(f"Document content: {doc.page_content}")
    finally:
        os.remove(temp_file_path)  

load_text_file()

def load_pdf_file():
    loader = PyPDFLoader("Week1.pdf")
    documents = loader.load()
    print(f"Number of pages loaded: {len(documents)}")
    for i, doc in enumerate(documents):
        print(f"Page {i+1} content: {doc.page_content[:100]}...")  # Print first 100 characters of each page
        print(f"Metadata: {doc.metadata}")
        
load_pdf_file()
