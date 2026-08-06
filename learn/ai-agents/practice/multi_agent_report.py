from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

def run_agent(role: str, instruction: str, user_input: str) -> str:
    messages = [
        SystemMessage(content=f"Sen {role} ajanısın. {instruction} Kısa Türkçe cevap ver."),
        HumanMessage(content=user_input),
    ]
    return llm.invoke(messages).content

topic = input("Konu: ").strip()

research = run_agent(
    "Researcher",
    "Konuyu araştırır gibi madde madde önemli noktaları çıkar. Uydurma; bilmiyorsan belirsiz de.",
    topic,
)
print("\n--- Researcher ---\n", research)

draft = run_agent(
    "Writer",
    "Sadece verilen araştırma notlarından kısa bir paragraf yaz. Not dışı bilgi ekleme.",
    research,
)
print("\n--- Writer ---\n", draft)

review = run_agent(
    "Reviewer",
    "Yazıyı kontrol et: eksik, abartı veya belirsiz yer var mı? 3 madde feedback + düzeltilmiş kısa final ver.",
    draft,
)
print("\n--- Reviewer ---\n", review)