#won't run due to no credits with anthropic


from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model_name="claude-3.5-sonnet-20241022")


result = model.invoke("Explain the theory of relativity in simple terms.")

print(result.content)