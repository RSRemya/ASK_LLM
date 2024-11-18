#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import ollama
# set the model
desiredModel = 'hermes3:8b'

st.title("Our First LLM Web Application Based on Llama and Streamlit")

def generate_response(questionToAsk):
    response = ollama.chat(model=desiredModel, messages=[
        {
            'role': 'user',
            'content': questionToAsk,
        },
    ])
    st.info(response['message']['content'])

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Over here, ask a question and press the Submit button. ",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)


# In[ ]:




