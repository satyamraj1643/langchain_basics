#won't run due to no credit with openai


from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(model="gpt-3.5-turbo-instruct")

llm_output = llm.invoke("Tell me a joke on diwali")

print(llm_output)


