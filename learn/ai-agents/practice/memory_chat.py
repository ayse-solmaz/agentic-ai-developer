from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

llm= ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite",temperature=0)

# short-term memory = bu listedeki mesajları saklar

history = [
    SystemMessage(content="sen yardımcı bir asistansın. kısa türkçe cevap ver. ")

]

print("çıkmak için: exit")

while True:
    user =input("sen: ").strip()
    if user.lower() in {"exit","quit"}:
        break

    history.append(HumanMessage(content=user))
    reply =llm.invoke(history)
    history.append(AIMessage(content =reply.content))

    print("agent: ",reply.content)