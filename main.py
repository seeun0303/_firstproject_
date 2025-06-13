import streamlit as st
import random
# 페이지 설정
st.set_page_config(
    page_title="가위✌️바위✊보🖐️ 게임",
    page_icon="🎮",
    layout="centered"
)

# 스타일 CSS
st.markdown(
    """
    <style>
    body {
        background-color: #FEF9EF;
        color: #222222;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 {
        color: #D72631;
        text-align: center;
        font-size: 48px;
        margin-bottom: 5px;
    }
    .stRadio > div > label {
        font-size: 22px;
        padding: 8px 25px;
    }
    .stButton button {
        background-color: #2E86AB;
        color: white;
        font-size: 24px;
        padding: 12px 35px;
        border-radius: 15px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목과 설명
st.title("🎮 컴퓨터와 가위✌️바위✊보🖐️ 게임!")
st.write(

