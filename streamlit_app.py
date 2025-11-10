
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
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)

# Sidebar
st.sidebar.title('🌎 Navigation')
page = st.sidebar.radio('Go to',
                        ['🦾 Home','🐼 About', '📚 Projects', '🚗 Skills', '✈ Resume', '📞 Contact' ])

# Home page
if page == '🦾 Home':
  st.markdown('<p class="main-header">Andy Mei</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">Aspiring Businessman | Medger Evers College</p>', unsafe_allow_html=True)

  # Three Columns for stats

col1, col2, col3 = st.columns(3)

with col1:
  st.metric('GPA', '3.3', '🖱')
with col2:
  st.metric('Projects', '5', '🛠')
with col3:
  st.metric('Skills', '10+', '🏀')

st.write('---')

#Introduction with columns
col1, col2 = st.columns([2,1])
with col1:
  st.subheader('Welcome to my digtial space!👋')
  st.write('''
  I am a student of Medger Evers College, hoping to one day learn how to run a business with the goel of making it in life. Currently learning how to code with HTML, CSS, JavaScript, and Python to build innovative solutions.

  ⌨ **Current Focus:** Building interative web applications with Streamlit

  📚 **Currently learning:** Internet and Emergin Technologies (CIS 211)

  🌱 **Fun Fact:** I am a NBA superfan!
  ''')

with col2:
  # Placeholder for image
  st.image('https://raw.githubusercontent.com/AMeiwah/CIS-211-project-1/refs/heads/main/golden.jfif', use_column_width=True)

# elif page == '🤠 About':
    st.title('About Me')

    # Timeline of my Professional Journey
    st.subheader('My Journey 🗺️')

    with st.expander('2025 - Present: Medgar Evers College'):
        st.write('''
            - Major: Computer Information Systems
            - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
            - Activities: Track Team, Volleyball Team, Hackathon participant
        ''')

st.subheader('Interests & Hobbies 🏀')
  interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')
elif page == '💼 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')
          
  
  
