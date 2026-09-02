from langchain_community.document_loaders import UnstructuredURLLoader
loader =  UnstructuredURLLoader(urls=["https://www.moneycontrol.com"],show_progress_bar=True)
loader.requests_kwargs = {'verify':False}
docs=loader.load()
print(len(docs))
print(docs[0])

