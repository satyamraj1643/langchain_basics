from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
)

embedding_result = embedding.embed_query("Delhi is the capital of India")

print(str(embedding_result))

