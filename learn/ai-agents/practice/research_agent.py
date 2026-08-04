from dotenv import load_dotenv
load_dotenv() #.env içindeki apikeyi yükler

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

#beyin (llm)
llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0)

#el (tool) - ücretsiz web araması
search =DuckDuckGoSearchRun()
tools =[search]

#prompt template -llm'e rolunu söyler
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "you are a research assistant. "
            "when you need current or factual info from the web,use the search tool. "
            "then answer clearly in turkish. "
            ),
            ("human","{input}"),
            ("placeholder","{agent_scratchpad}")
    ]
)

#agent +executor (observe -> think -> act döngüsünü çalıştırır)

agent =create_tool_calling_agent(llm,tools,prompt)
executor = AgentExecutor(agent=agent,tools=tools,verbose=True)

if __name__=="__main__":
    question=input("sorunu yaz: ")
    result = executor.invoke({"input" : question})
    print("\n--- cevap ---")
    print(result["output"])