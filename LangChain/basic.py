from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI()

prompt = ChatPromptTemplate.from_template("Explain {topic} simply")

chain = prompt | llm

response = chain.invoke({"topic": "AI"})
print(response)