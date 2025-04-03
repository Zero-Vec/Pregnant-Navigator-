import streamlit as st
# import agent_page2
# import agent_page3
# import start_page
# import agent_page1

st.set_page_config(
    page_title="Mindpilot",
    page_icon="💞",
    layout="wide",
    initial_sidebar_state="expanded",
)

# st.session_state.fastgpt_api_key1 = st.secrets["fastgpt_api_key1"]
# st.session_state.fastgpt_api_url1 = st.secrets["fastgpt_api_url1"]
# st.session_state.fastgpt_api_key2 = st.secrets["fastgpt_api_key2"]
# st.session_state.fastgpt_api_url2 = st.secrets["fastgpt_api_url2"]
# st.session_state.fastgpt_api_key3 = st.secrets["fastgpt_api_key2"]
# st.session_state.fastgpt_api_url3 = st.secrets["fastgpt_api_url3"]

st.logo('logo_new.png', size='large', icon_image='logo.png')

start_page = st.Page("start_page.py", title="欢迎", icon="💞")
agent_page2 = st.Page('agent_page2.py', title='孕心悦', icon='🤖')
agent_page3 = st.Page("agent_page3.py", title="孕知宝", icon="👩‍💼")
agent_page1 = st.Page("agent_page1.py", title="孕心查", icon="🕵️")

pages = [start_page, agent_page1, agent_page2, agent_page3]
pg = st.navigation(pages) # 导航栏
pg.run()
