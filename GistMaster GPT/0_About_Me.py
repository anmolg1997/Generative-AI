import streamlit as st
from utils import * 
import random
import time

def run():
    st.set_page_config(
        page_title="sGPT",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    shadow_title('#000000', '#fff0f0', "📚 GistMaster GPT 📚", 0.85, 35, 50, st)

    st.markdown(
    """
    ## 📘 `About GistMaster GPT`

    Welcome to the GistMaster GPT, your tool for condensing extensive information into bite-sized insights! 🚀

    Our application is designed to enhance your reading experience by providing succinct summaries of your documents. 
    Dive into your texts with efficiency and gain the ability to grasp key concepts quickly. 📈🔍

    ### ⚡ `Our Goal`

    The Document Summarizer aims to streamline your information consumption. With our tool, you can:

    - **Time Efficiency:** Quickly understand the essence of your documents. ⏱️
    - **Ease of Use:** Upload your file and receive a summary in moments. 📤
    - **Content Comprehension:** Improve your understanding with concise summaries. 📚

    ## 🎙 `Features`

    - **User-Friendly Design:** Our app is intuitive and simple to navigate, ensuring a smooth user experience. 🖱️👨‍💻
    - **Versatile File Handling:** Whether it's a PDF, DOCX, or TXT, our summarizer is equipped to handle multiple file formats. 📄
    - **Quality Summaries:** Leveraging advanced algorithms to provide the essence of your text. 🧠

    ### 🤔 `How to Get Started`
    
    | **Tabs** 🕹️ | **Description** 🔍 |
    | ---- | ----------- |
    | 1. **Upload File** | Choose and upload the document you wish to summarize. |
    | 2. **Create Summary** | View the generated summary of your uploaded document. |

    ### 🎧 `Contact Us`

    Have questions, feedback, or need assistance? Feel free to reach out:

    - 📧 Anmol Jaiswal: [ajaisw26@ext.uber.com](mailto:ajaisw26@ext.uber.com)

    **📖 Transform the way you read and understand documents with Document Summarizer! 📖**
    """
)

    # 2. Footer
    footer_design()


if __name__ == "__main__":
    run()