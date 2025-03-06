from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
import os
import json
# glob="*.md"


with open("exclude_files.json", "r") as f:
    exclude_files = json.load(f)

allowed_dirs = {"1. Projects", "2. Areas", "3. Resources", "4. Archives"}
base_dir = "/Users/bogle/Dev/obsidian/Bogle"


documents = []
for sub_dir in allowed_dirs:
    full_path = os.path.join(base_dir, sub_dir)
    loader = DirectoryLoader(full_path, glob="**/*.md", recursive=True)
    try:
        docs = loader.load()
        filtered_docs = [
            doc for doc in docs
            if os.path.relpath(doc.metadata.get("source", ""), base_dir) not in exclude_files
        ]
        documents.extend(filtered_docs)
    except Exception as e:
        print(f"Error loading from {full_path}: {e}")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings)

def search(query):
  docs = vectorstore.similarity_search(query, k=1)
  return docs[0].page_content

# asked this question 
# loader = DirectoryLoader("/Users/bogle/Dev/obsidian/Bogle/3. Resources/0. note idea draft", glob="job - Rockstar Games - my questions.md")
# print(search("what did i skip in Real-Word Chat Development with O3 Mini & RAG"))
