#won't run , first of all GCP authe problems!! (i do not have time :( to debug it now)), and maybe then quota limits ! ahh!!!


from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

result = model.invoke("Provide a brief summary of the history of artificial intelligence.")

print(result)
