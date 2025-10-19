#won't run due to no credit with openai


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents =  [
    "Paris is the capital of France",
    "Berlin is the capital of Germany",
    "Madrid is the capital of Spain"
    "A dog is cute"
    "Cats are lovely pets"
    "The sun rises in the east"
    "Water boils at 100 degrees Celsius"
    "Wow! Such a long sentence to embed into a vector representation!"
]

#embedding_result = embedding.embed_query("Delhi is the capital of India")

embedding_result = embedding.embed_documents(documents)

print(str(embedding_result))

