import streamlit as st
from langchain_helper import get_qa_chain
st.title("Ed-Tech Course QA ")
btn=st.button("create Knowlegebase ")

if btn:
    pass


question=st.text_input("question : ")
if question:
    chain=get_qa_chain()
    response=chain(question)
   
    st.header("Answer : ")
    st.write(response["result"])