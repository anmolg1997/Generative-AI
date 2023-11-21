#standard imports
import streamlit as st
import time
import os
import openai
from langchain.chat_models import ChatOpenAI

#customized imports
from utils import shadow_title, footer_design
from scripts.uploader import files_uploader
from scripts.summarizer import customLoaderGen, customSplitter, map_reduce_summarizerGen, stuff_summarizerGen
from token_generator import token_wrapper

# Setting config
st.set_page_config(
        page_title="sGPT",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )

#openai tokens
openai.api_base = 'https://genai-api.uberinternal.com/v1'

#Output box
box_markdown = """
    <div style="background-color: #f9f9f9; padding: 10px; border-radius: 10px; border: 1px solid #ccc;">
        <h2>Beautiful Title</h2>
        <p>This text is inside a "box" with a background color, padding, and a border.</p>
    </div>
"""
def app():
    #st.session_state
    ###################################################
    if 'usso_token' not in st.session_state:
        st.session_state.usso_token = token_wrapper()
    if 'is_submitted' not in st.session_state:
        st.session_state.is_submitted = False
    if 'customLoader' not in st.session_state:
        st.session_state.customLoader = False
    if 'loadedData' not in st.session_state:
        st.session_state.loadedData = None
    
    os.environ["OPENAI_API_KEY"] = st.session_state.usso_token
    # instantiate LLM
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
    ###################################################
    
    shadow_title('#000000', '#fff0f0', "📂 Upload 📂", 0.85, 35, 40, st.sidebar, False)
    shadow_title('#000000', '#fff0f0', "💼📘🔍 𝐆𝐏𝐓 𝐆𝐢𝐬𝐭𝐌𝐚𝐬𝐭𝐞𝐫 🔎📗💼", 0.85, 35, 40, st, True)

    ###################################################
    #1. Upload Container generation
    file, type, is_submitted = files_uploader()
    
    if st.session_state["is_submitted"] and not st.session_state.loadedData and not st.session_state.customLoader:
        #2. Instantiate Loader
        customLoader = customLoaderGen(file, type)
    
        #3. Instantiate Custom Splitter
        recursive_splitter = customSplitter(chunk_size=2000, chunk_overlap=200)
        
        #3. Load & Split docs
        with st.spinner('🔄 𝑬𝒙𝒆𝒄𝒖𝒕𝒊𝒏𝒈 𝑫𝒂𝒕𝒂 𝑨𝒄𝒒𝒖𝒊𝒔𝒊𝒕𝒊𝒐𝒏 & 𝑫𝒊𝒔𝒕𝒓𝒊𝒃𝒖𝒕𝒊𝒐𝒏...'):
            time.sleep(2)
            loadedData = customLoader.load_and_split(text_splitter=recursive_splitter)
            if not len(loadedData):
                st.error('🚫🚫🚫 The provided document is not extractable 🚫🚫🚫')
            else:
                st.session_state.loadedData = loadedData
            st.session_state.customLoader = True
        
    if st.session_state.customLoader and st.session_state.loadedData:
        loadedData = st.session_state.loadedData  
        total_doc = len(loadedData)
        st.write('🌱 𝚃𝚘𝚝𝚊𝚕 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚝𝚘 𝚌𝚘𝚗𝚜𝚞𝚖𝚎 : ', total_doc )

        col1, _, col2 = st.columns([13,3,4])
        #4. Consumer demand 
        consume_label = f"🌱 𝙷𝚘𝚠 𝚖𝚊𝚗𝚢 𝚍𝚘𝚌𝚞𝚖𝚎𝚗𝚝𝚜 𝚘𝚞𝚝 𝚘𝚏 {total_doc} 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚌𝚘𝚗𝚜𝚞𝚖𝚎 𝚏𝚘𝚛 𝚢𝚘𝚞𝚛 𝚝𝚊𝚜𝚔？"
        default_number = min(5, total_doc)
        selected_doc = 1
        if total_doc >= 1:
            selected_doc = col1.slider(consume_label, 0, total_doc, default_number, key='selected_number')

        if col1.button('⚡ 𝐈𝐧𝐢𝐭𝐢𝐚𝐭𝐞 𝐃𝐢𝐬𝐭𝐢𝐥𝐥𝐚𝐭𝐢𝐨𝐧 ⚡'):
            
            #4. Instantiate Summarizer
            if total_doc >= 1:
                summarizerChain = map_reduce_summarizerGen(llm)
            else:
                summarizerChain = stuff_summarizerGen(llm)

            #5. Run Summarizer
            with st.spinner('🌐 𝑨𝒄𝒕𝒊𝒗𝒂𝒕𝒆𝒅 𝑰𝒏𝒔𝒊𝒈𝒉𝒕𝒔 𝑪𝒐𝒏𝒅𝒆𝒏𝒔𝒂𝒕𝒊𝒐𝒏....'):
                start_time = time.time()
                st.write(summarizerChain.run(loadedData[:selected_doc+1]))
                execution_time = time.time() - start_time
                col2.markdown(f"`Load time = {execution_time:.2f} seconds`")
                st.success('Done!')



# Run the app function
if __name__ == '__main__':
    app()
    footer_design()