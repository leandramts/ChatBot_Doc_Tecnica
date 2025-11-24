from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = PyMuPDFLoader(
    r"C:\Users\SAMSUNG\OneDrive\Documentos\ChatBot_Doc_Tecnica\aula11.pdf"
)
docs = loader.load()

print(len(docs))
print(docs[3].page_content[:100])

splitter = RecursiveCharacterTextSplitter(
    separators = ["\n",],
    chunk_size = 100,
    chunk_overlap = 10
)

chunks = splitter.split_documents(docs)
for c in chunks[:5]:
    print(len(c.page_content))

#for i, c in enumerate(chunks):
#    print(i, c.page_content)
