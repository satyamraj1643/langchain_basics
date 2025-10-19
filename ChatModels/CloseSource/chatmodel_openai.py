#won't run due to no credit with openai


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')

model_result = model.invoke("What is your name?")


print(model_result)
