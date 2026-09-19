import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
# .env dosyası yükle
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    print("API key is not found.")

model = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite"
)
prompt= ChatPromptTemplate.from_messages(
    [
    ("system",
      "Sen teknik konuları anlatan bir eğitim asistanısın"),
    ("human", 
     """Konu: {topic}"""),
])

messages = prompt.format_messages(
    topic= "Büyük dil modelleri nedir, 1 cümle ile cevap ver.")
# promptu modele gönder
response = model.invoke(messages)

print(response.content)