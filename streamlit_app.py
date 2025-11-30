import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
    page_title='Andy Mei | Portfolio',
    page_icon='🎯',
    layout='wide'
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
    .sub-header {font-size: 24px; text-align:center; color: #666;}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title('🌎 Navigation')
page = st.sidebar.radio(
    'Go to',
    ['🦾 Home', '🐼 About', '📚 Projects', '🚗 Skills', '✈ Resume', '📞 Contact']
)

# ---------------- HOME PAGE ----------------
if page == '🦾 Home':
    st.markdown('<p class="main-header">Andy Mei</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Aspiring Businessman | Medgar Evers College</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('GPA', '3.3', '🖱')
    with col2:
        st.metric('Projects', '5', '🛠')
    with col3:
        st.metric('Skills', '10+', '🏀')

    st.write('---')

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader('Welcome to my digital space! 👋')
        st.write("""
        I am a student at Medgar Evers College, hoping to one day run a business with the goal 
        of making it in life. I am currently learning coding (HTML, CSS, JavaScript, and Python)
        to build new and innovative solutions.

        ⌨ **Current Focus:** Building interactive web applications with Streamlit  
        📚 **Currently Learning:** Internet & Emerging Technologies (CIS 211)  
        🌱 **Fun Fact:** I'm an NBA superfan!
        """)

    with col2:
        st.image(
            'https://raw.githubusercontent.com/AMeiwah/CIS-211-project-1/refs/heads/main/golden.jfif',
            use_column_width=True
        )

# ---------------- ABOUT PAGE ----------------
elif page == '🐼 About':
    st.title('About Me')
    st.subheader('My Journey 🗺️')

    with st.expander('2025 - Present: Medgar Evers College'):
        st.write("""
        - Major: Business Administration  
        - Relevant Coursework: Internet & Emerging Technologies, Small Business Management, Organizational Behavior  
        - Activities: Gamer, Basketball  
        """)

    with st.expander('2017 - 2021: NYC Museum School'):
        st.write("""
        - Graduated with honors  
        - AP US History  
        - Played on the Basketball Team  
        """)

    st.subheader('Interests & Hobbies 🏀')
    interests = ['Web Development', 'AI/Machine Learning', 'Photography', 'Basketball', 'Travel', 'Baseball']

    cols = st.columns(3)
    for i, interest in enumerate(interests):
        with cols[i % 3]:
            st.info(f'🔷 {interest}')

# ---------------- PROJECTS PAGE ----------------
elif page == '📚 Projects':
    st.title('My Projects')

    # Project 1
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('download.jpeg')
        with col2:
            st.subheader('🛒 Final Essay From ELA 150')
            st.write('Python web scraper that monitors Amazon prices and sends alerts')
            st.caption('**Technologies:** Python, BeautifulSoup, Streamlit')

    # Project 2
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://www.publicdomainpictures.net/pictures/90000/nahled/calculator-black-clipart.jpg')
        with col2:
            st.subheader('📊 Student Grade Calculator')
            st.write('Interactive web app for calculating and visualizing grades')
            st.caption('**Technologies:** Python, Pandas, Plotly')

# ---------------- SKILLS PAGE ----------------
elif page == '🚗 Skills':
    st.title('Technical Skills')

    st.subheader('Life Skills')
    skills_data = {
        'Basketball': 85,
        'Gaming': 80,
        'Coding': 69,
        'Cooking': 65
    }

    for skill, level in skills_data.items():
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(skill)
        with col2:
            st.progress(level / 100)

    st.subheader('Tools & Technologies')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.success('Excel')
        st.info('Word')
        st.warning('Access')

    with col2:
        st.success('PowerPoint')
        st.info('Google Docs')
        st.warning('ChatGPT / AI Tools')

    with col3:
        st.success('Presentations')
        st.info('Writing')
        st.warning('Social Media')

    # ---------------- RESUME PAGE ----------------
elif page == '✈ Resume':
    st.title('My Resume')

    try:
        with open('my_resume.pdf', 'rb') as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label='🔻 Download Full Resume (PDF)',
            data=PDFbyte,
            file_name='Andy_Mei_Resume.pdf',
            mime='application/pdf'
        )

    except FileNotFoundError:
        st.error("❌ Resume file not found. Make sure 'my_resume.pdf' is in the same folder.")

elif page == '📞 Contact':
    st.title("Let's Connect!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Send me a message')

        st.write('''
        📧 **Email:** andymei152@gmail.com  

        📷 **Instagram:** [@andymei24](https://www.instagram.com/) 


        ''')



      


          
  
  
