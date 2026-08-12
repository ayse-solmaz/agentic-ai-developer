from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def unstable_weather_api(city: str) -> str:
    """Get live weather. If response starts with ERROR, call backup_weather_info."""
    # Simulate offline API as a returned error (not a process crash)
    return f"ERROR: weather api offline for {city}"

@tool
def backup_weather_info(city: str) -> str:
    """Fallback when main weather API fails or returns ERROR."""
    return f"{city}: yedek kaynak — değişken bulutlu (güven: düşük)"

tools = [unstable_weather_api, backup_weather_info]
llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Resilient weather assistant. "
     "1) Call unstable_weather_api first. "
     "2) If it returns ERROR, immediately call backup_weather_info. "
     "3) Never invent live weather. Answer in Turkish."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=6,
)

if __name__ == "__main__":
    q = input("soru: ")
    try:
        print(executor.invoke({"input": q})["output"])
    except Exception as e:
        print("kontrollu hata:", e)
