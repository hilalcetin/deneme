import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
vector_store = FAISS.load_local("faiss_index", embeddings=embeddings, allow_dangerous_deserialization=True)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
prompt = ChatPromptTemplate.from_messages(
    [       
        ("system", """
        Sen teknik konuları anlatan bir eğitim asistanısın. 
        Kullanıcı sorularını sadece sana verilen context içerisindeki nilgileri kullanarak cevapla. 
        Eğer sorunun cevabı context içerisinde yoksa, "Üzgünüm, bu konuda yeterli bilgiye sahip değilim." şeklinde cevapla."""),
        ("human", 
         """CONTEXT: {context}
         Soru: {question}""")])

output_parser = StrOutputParser()
chain = prompt | model | output_parser
question = "Elektronik kontrol biriminin maksimum çalışma sıcaklığı kaç derecedir?"
documents = retriever.invoke(question)
context = "\n".join([doc.page_content for doc in documents])
response = chain.invoke({"context": context, "question": question})
print(response)
