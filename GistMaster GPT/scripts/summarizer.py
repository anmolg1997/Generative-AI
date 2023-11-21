import os
import openai
import langchain
import streamlit as st

# Langchain
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

from langchain.document_loaders import (
    UnstructuredCSVLoader,
    UnstructuredHTMLLoader,
    UnstructuredImageLoader,
    UnstructuredWordDocumentLoader,
    PythonLoader,
    PyPDFLoader,
    JSONLoader,
    Docx2txtLoader,
    ToMarkdownLoader,
    UnstructuredFileLoader
)
from langchain.document_loaders.csv_loader import CSVLoader

from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter
)

# Custom functions

def customLoaderGen(file_path, file_type):
    # st.write(file_type.lower())
    try:
        if file_type.lower()=='csv':
            customLoader = CSVLoader(file_path=file_path)
        if file_type.lower()=='txt':
            customLoader = TextLoader(file_path=file_path)
        if file_type.lower()=='docx':
            customLoader = Docx2txtLoader(file_path=file_path)
        if file_type.lower()=='pdf':
            customLoader = PyPDFLoader(file_path=file_path)
        if file_type.lower()=='html':
            customLoader = UnstructuredHTMLLoader(file_path=file_path)
        if file_type.lower() in ('md', 'markdown'):
            customLoader = ToMarkdownLoader(file_path=file_path)
    except:
        st.write('using file loader')
        customLoader = UnstructuredFileLoader(file_path=file_path)
    return customLoader

def customSplitter(chunk_size=2000, chunk_overlap=100):
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=100,
    )
    return recursive_splitter
    
def map_reduce_summarizerGen(_llm, _verbose=False):
    map_template = """Based on given context, extract theme, write a concise yet compelling summary of the following and deduce inference, without missing anything important:
    
    
    "{text}"
    
    
    CONCISE SUMMARY:"""
    
    combine_template = """The following is a set of summaries of different part of a big document:
    
    "{text}"
    
    Take these and distill it into a final YET consolidated, impactful and coherent OUTPUT. Ensure to not to miss anything important.

    Give the FINAL OUTPUT in below structured and bulleted format:
    1. THEME:
    2. SUMMARY:
    3. INFERENCE:"""
    
    map_prompt = PromptTemplate.from_template(map_template)
    combine_prompt = PromptTemplate.from_template(combine_template)
    
    summarizerChain = load_summarize_chain(
        llm=_llm,
        chain_type='map_reduce',
        map_prompt=map_prompt,
        combine_prompt=combine_prompt,
        verbose=_verbose
    )
    return summarizerChain

def stuff_summarizerGen(_llm, _verbose=False):

    stuff_template = """Based on the given document, distill it into a final YET consolidated, impactful and coherent OUTPUT. Ensure to not to miss anything important.:
    
    "{text}"
    
    Give the FINAL OUTPUT in below structured and bulleted format:
    
    1. THEME:
    
    2. SUMMARY:
    
    3. INFERENCE:"""
    
    stuff_prompt = PromptTemplate.from_template(stuff_template)
    
    summarizerChain = load_summarize_chain(
        llm=_llm,
        chain_type='stuff',
        prompt = stuff_prompt
    )
    return summarizerChain
    