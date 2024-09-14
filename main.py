import streamlit as st
from langchain_helper import create_vectordb, get_qa_chain


st.title("QnA Bot 🤖")

st.subheader("This bot answer question which can be infered using a given FAQs document")

btn = st.button("Create Knowledgebase")

if btn:
    create_vectordb()
    st.warning("Created DB!")

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain.invoke({"input": question})
    print(response)
    st.header("Answer:")
    st.write(response["answer"])