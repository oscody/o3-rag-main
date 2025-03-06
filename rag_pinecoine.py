from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_pinecone import PineconeVectorStore, Pinecone


loader = DirectoryLoader("/Users/bogle/Dev/obsidian/Bogle/3. Resources/0. note idea draft", glob="job - Rockstar Games - my questions.md")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

def create_vectorstore():
  vectorstore = Pinecone.from_documents(chunks, embeddings, index_name="markdownv2")
  return vectorstore

def search_bike_station(query):
  
  vectorstore = PineconeVectorStore(index_name="markdownv2", embedding=embeddings)
  docs = vectorstore.similarity_search(query, k=1)
  return docs[0].page_content

print(search_bike_station("what are two question i wanted to ask"))