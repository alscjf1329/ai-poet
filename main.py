from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
content = "코딩"

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2")

chain = prompt | model

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
  with st.spinner('시 작성 중...'):
    result = chain.invoke({"question": content + "에 대한 시를 써줘."})
    st.write(result)


# chain.invoke()의 결과를 받아서 출력




