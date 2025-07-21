from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # Google Gemini modelini seç
    temperature=0.7,  # Yanıt çeşitliliği
    google_api_key=api_key  # API anahtarı
)

messages = [
    HumanMessage(content="Hi!")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)
