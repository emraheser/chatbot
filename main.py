from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


templete = """
Answer the following question:

    Here is the conversation history: {context}

    Question: {question}

    Answer:

"""

model = OllamaLLM(model="llama3.1")

promt = ChatPromptTemplate.from_template(templete)
chain = promt | model

# result = model.invoke(input="Hello, how are you?")

def handle_conversation():
    context = ""
    print("Start a conversation:")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break

        result = chain.invoke({"context": context , "question": user_input})
        print("Bot:", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()

