from langchain_community.document_loaders import PyMuPDFLoader


loader = PyMuPDFLoader(r"C:\Users\SAMSUNG\OneDrive\CmapToolsLogs\Documentos\ChatBot_Doc_Tecnica\aula11.pdf")
docs = loader.load()

print(len(docs))
print(docs[0].page_content[:500])