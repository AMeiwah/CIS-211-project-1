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

# About Page
if page == '🐼 About':
  st.title('About Me')

  # Timeline of my Professional Journey
  st.subheader('My Journey 🗺️')

with st.expander('2025 - Present: Medgar Evers College'):
  st.write('''
    - Major: Computer Information Systems
    - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, AI
    - Activities: Track Team, Volleyball Team, Hackathon participant
''')

with st.expander('2017 - 2021: NYC Museum School'):
  st.write('''
    - Graduated with honors
    - AP US History
    - Played on the Basketball team
''')
  st.subheader('Interests & Hobbies 🏀')
interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

# Display the interests in columns
cols = st.columns(3)
for i, interest in enumerate(interests):
  with cols[i % 3]:
    st.info(f'🔷 {interest}')
elif page == '📚 Projects':
  st.title('My Projects')
  st.write('Here are some projects I have worked on:')

# Project 1
with st.container():
  col1, col2 = st.columns([1, 2])
  
with col1:
    st.image('https://iprx-cms-content.ams1.vultrobjects.com/Blog_How_To_Crawl_4_capcha_ded9206d5f.png')

with col2:
    st.subheader('🛒 E-Commerce Price Tracker')
    st.write('Python web scraper that monitors Amazon prices and sends alerts')
    st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')


  # Project 2 
with st.container():
  col1, col2 = st.columns([1,2])
with col1:
  st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg')
with col2:
  st.subheader('📊 Student Grade Calulator')
  st.write('Interactive web app for calculating and visualizing grades')
  st.caption('**Technologies:** Python, Pandas, Plotly')

elif page == '✈ Skills':
  st.title('Technical Skills')

# Skills with progress bar
st.subheader ('Life skills')

skills_data = {
  'Basketball': 85,
  'Gaming': 80,
  'Coding': 69,
  'Cooking': 65
}
for skill, level in skills_data.items():
  col1, col2 = st.columns([1,3])
with col1:
  st.write(skill)
with col2:
  st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
with col1:
  st.success('Excel')
  st.info('Word')
  st.warning('Access')

with col2:
  st.success('PowerPoint')
  st.info('Google Docs')
  st.warning('ChatGPT/AI Tools')
    
with col3:
  st.success('Presentations')
  st.info('Writing')
  st.warning('Social Media')
    
      


          
  
  
