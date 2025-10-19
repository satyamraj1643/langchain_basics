from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain.schema import HumanMessage
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='google/gemma-3-270m',
    task='text-generation',
    pipeline_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 256
    }
)

model = ChatHuggingFace(llm=llm)

# Wrap the input in a HumanMessage
result = model.invoke("Explain the theory of relativity in simple terms.")

# Print the text
print(result)
