import langchain
import os
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = ""

llm = ChatGoogleGenerativeAI(
    model="gemini-1.0-pro",
    temperature=0.0
)

response = llm.invoke("Say hello in Korean.")
print(response.content)
