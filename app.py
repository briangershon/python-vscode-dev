from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0.9, model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Create a haiku from:\n\n{content}")
chain = prompt | llm

response = chain.invoke({"content": "The quick brown fox jumps over the lazy dog."})
print(response.content)
