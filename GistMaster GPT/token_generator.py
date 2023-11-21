from langchain.llms import OpenAI
import os
import time
import openai
import streamlit as st

openai.api_base = 'https://genai-api.uberinternal.com/v1'

# Function to save the token to a file
def save_token(token, file_path='token.txt'):
    with open(file_path, 'w') as file:
        file.write(token)
    return f"Token saved to {file_path}"

def new_token_gen():
    with st.form(key='token_form'):
        token = st.text_input('Enter your token here:')
        submit_button = st.form_submit_button('Save OpenAI API Key')

    if submit_button:
        message = save_token(token)
        st.success(message)
        time.sleep(2)
        st.rerun() 
        
def fetch_token_from_file(file_path='token.txt'):
    """
    This function reads a file to fetch a token.
    
    :param file_path: The path to the file containing the token.
    :return: The token as a string.
    """
    with open(file_path, 'r') as file:
        token = file.read().strip()  # Read the token and strip any whitespace
    return token

def token_wrapper():
    try:
        usso_token = fetch_token_from_file(file_path='token.txt')
        os.environ["OPENAI_API_KEY"] = usso_token
        llm_check = OpenAI()
        llm_check.predict('Heyy!')
        return usso_token
    except:
        new_token_gen()