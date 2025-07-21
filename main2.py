from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=api_key
)


def main():
    system_message = SystemMessage(
        content="You are a helpful assistant. Answer all questions to the best of your ability")

    history = InMemoryChatMessageHistory()
    history.add_message(system_message)

    print("Çıkmak için 'exit' yazabilirsiniz.")

    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Sohbet sonlandırıldı.")
            break

        human_message = HumanMessage(content=user_input)
        history.add_message(human_message)

        messages = history.messages
        response = model.invoke(messages)

        assistant_message = response
        print("Asistan:", assistant_message.content)

        history.add_message(assistant_message)


if __name__ == "__main__":
    main()
