#won't run due to no credit with openai


from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

embedding_result = embedding.embed_query("Delhi is the capital of India")

print(str(embedding_result))

