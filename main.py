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
st.write("아래에서 가위, 바위, 보 중 하나를 선택하고 ‘대결!’ 버튼을 눌러주세요!")

# 선택지 딕셔너리
choices = {
    "가위 ✌️": "scissors",
    "바위 ✊": "rock",
    "보 🖐️": "paper"
}

# 사용자 선택
user_choice_text = st.radio("내 선택:", list(choices.keys()), index=0)

if st.button("🔥 대결!"):
    # 컴퓨터 랜덤 선택
    computer_choice_text = random.choice(list(choices.keys()))
    user_choice = choices[user_choice_text]
    computer_choice = choices[computer_choice_text]

    # 결과 판단
    if user_choice == computer_choice:
        result = "🤝 비겼어요!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "🎉 당신이 이겼어요! 🏆"

