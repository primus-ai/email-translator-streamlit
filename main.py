import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
import os

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the imput text to a specific tone
    - Convert the input text to a specific dialect
    
    Here are some examples differet Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.
    
    Here are some examples of words in different dialects:
    - American English: French Fries, cotton candy, apartment, garbage, cookie.
    - British English: chips, candyfloss, flag, rubbish, biscuit, green fingers.
    
    Below is the email, tone and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR RESPONSE
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template
)

def load_LLM():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature=.5, openai_api_key=os.environ.get('OPENAI_API_KEY'))
    return llm

llm = load_LLM()

st.set_page_config(page_title="Globalize Email", page_icon=":robot:")
st.header("Globalize Text")

col1, col2 = st.columns(2) 

with col1:
    st.markdown("This application is powered by ChatGPT and build by Primus. You can ask questions to your documents")

with col2:
    st.image(image="logoprimus.png", width=500)

st.markdown("Enter your Email to convert")

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like you email to have?',
        ('Formal', 'Informal'))

with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American English', 'British English')
    )

def get_text():
    input_text = st.text_area(label="", placeholder="Your Email...", key="email_input")
    return(input_text)

email_input= get_text()

st.markdown("### Your Converted Email:")

if email_input:
    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    
    formatted_email = llm(prompt_with_email) 
    
    st.write(formatted_email)


