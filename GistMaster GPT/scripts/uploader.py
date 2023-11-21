import streamlit as st
import pandas as pd
import numpy as np
import os

# function to save the uploaded file
def save_uploaded_file(directory, file):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, file.name), "wb") as f:
        f.write(file.getbuffer())
    return True, os.path.join(directory, file.name)

# files_uploader container
def files_uploader():
    
    st.sidebar.write("\n")
    # Define the directory where files will be stored
    directory = "./uploaded_files/"
    # Initialize variables to return
    saved_file_path = None
    # Sidebar for file type selection
    file_type = st.sidebar.selectbox(
        'Select file type to upload',
        ('PDF', 'DOCX', 'HTML', 'TXT')
    )

    # Create a form for file upload
    with st.sidebar.form(key='upload_form'):
        uploaded_file = st.file_uploader(f"Upload a {file_type} file", type=[file_type.lower()])
        submit_button = st.form_submit_button(label='🚀 𝙻𝚊𝚞𝚗𝚌𝚑 𝙵𝚒𝚕𝚎 𝚄𝚙𝚕𝚘𝚊𝚍 🚀')
    
    # When the form is submitted (i.e., the upload button is clicked), save the file
    if submit_button and uploaded_file is not None:
        saved_file_path, file_path = save_uploaded_file(directory, uploaded_file)
        if saved_file_path:
            st.session_state["is_submitted"] = True
            if 'loadedData' in st.session_state:
                st.session_state.loadedData = None
            if 'customLoader' in st.session_state:
                st.session_state.customLoader = False
            #st.success(f"Saved file {uploaded_file.name} in {directory}")
        else:
            st.error("Failed to save file.")

    # If the file was saved successfully, return the file and file type
    if saved_file_path:
        return file_path, file_type, submit_button
    else:
        return None, None, None