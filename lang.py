from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://www.moneycontrol.com")
loader.requests_kwargs = {'verify':False}
docs=loader.load()
print(docs[0])

