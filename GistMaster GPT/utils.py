import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Custom Utilities

def footer_design():
    
    st.sidebar.markdown("""
    <style>
    .footer {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 30px; /* Adjust the height as needed */
        background-color: #D8D9DA;
        color: #053B50;
        border-top: 0px solid #fff; /* Add a top border for separation */
        
        
    }
    .footer p {
        margin: 0; /* Remove default margin */
        text-shadow: 0 1px 1px rgba(0, 0, 0, 0.2); /* Add text shadow */
        font-weight: 400; /* Make the text bold */
        background: linear-gradient(to bottom, #D8D9DA, #BEC0C2); /* Add gradient background */
        border-radius: 5px; /* Add rounded corners */
        padding: 5px 15px; /* Add padding to the text */
        transform: perspective(400px) rotateX(10deg); /* Rotate the text to counteract the projection */
        border-top: 1px solid #fff;
        box-shadow: 0 10px 10px rgba(0, 0, 255, 0.4); /* Add a shadow to the top */

    }
    </style>
    <div class="footer">
        <p> 🌟 Navigating Insights : Engineered by <a href="https://whober.uberinternal.com/999000268380">Anmol Jaiswal</a> &copy; 2023 🌟</p>
    </div>
    """, unsafe_allow_html=True)

def shadow_title(bg, tc, title, opacity, fs, lh, tab, with_divider=True):
    '''
    0 : background_color
    '''
    htmlstr1="""<h2 style='background-color:{0};
                   color:{1};
                   font-size:{4}px;
                   border-radius:5px;
                   line-height:{5}px;
                   letter-spacing: 1.5px;
                   opacity:{3};
                   font-family:Greycliff;
                   text-align:center;
                   box-shadow:
                    0 5px 12px 0 rgba(0, 0, 0, 0.5),
                    0 5px 12px 0 rgba(0, 0, 0, 0.5),
                    0 -5px 12px 0 rgba(255, 255, 255, 0.5),
                    0 -5px 12px 0 rgba(255, 255, 255, 0.5);
                   '>
                   {2}</style>
                   <br></h2>"""
    tab.markdown(htmlstr1.format( bg, tc, title, opacity, fs, lh),unsafe_allow_html=True)
    if with_divider:
        tab.divider()
    
def cln_str(txt):
    return txt.replace('_', ' ').title()
