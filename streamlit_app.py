import streamlit as st
import pandas as pd 
from datetime import datetime

# Page Config
st.set_page_config(
  page_title ='Andy Mei | Portfolio',
  page_icon='🎯',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font_size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('🌎 Navigation')
page = st.sidebar.radio('Go to',
                        {'🦾 Home','🐼 About', '📚 Projects', '🚗 Skills', '✈ Resume', '📞 Contact' })

# Home page
if page == '🦾 Home':
  st.markdown('<p class"main-header">Andy Mei</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring Businessman | Medger Evers College</p>', unsafe_allow_html=True)
  
