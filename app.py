from langchain_helper import get_few_shot_db_chain
import streamlit as st
st.title("SQL DATA FETCH")

question=st.text_input("Question: ")

if question:
    chain=get_few_shot_db_chain()
    answer=chain.run(question)

    st.header("Answer:")
    st.write(answer)
