from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def unstable_weather_api(city:str)->str:
    """ get live weather. may fail"""
    raise RuntimeError(f"weather api offline for {city}")

@tool
def backup_weather_info(city: str) -> str:
    """Fallback when main API fails."""
    return f"{city}: yedek kaynak — değişken bulutlu (güven: düşük)"

tools=[unstable_weather_api,backup_weather_info]
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Resilient assistant. Tool fails → try fallback. "
     "Both fail → explain in Turkish, don't invent live weather."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm,tools,prompt)
executor =AgentExecutor(
    agent=agent,tools=tools,verbose=True,
    handle_parsing_errors=True,max_iterations=6,
)

if __name__=="__main__":
    q=input("soru: ")
    try:
        print(executor.invoke({"input": q})["output"])
    except Exception as e:
        print("kontrollu hata:",e)