import streamlit as st
import random

st.set_page_config(
    page_title="가위✌️바위✊보🖐️ 게임",
    page_icon="🎮",
    layout="centered"
)

# 🎨 스타일 설정
st.markdown(
    """
    <style>
    .main {
        background-color: #FCE38A;
        color: #1E1E1E;
    }
    h1 {
        color: #FF4B3E;
        text-align: center;
        font-size: 60px;
    }
    .stButton button {
        font-size: 24px;
        padding: 0.75em 2em;
        margin: 10px;
        background-color: #FFB830;
        color: white;
        border: none;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎮 제목
st.markdown("## 🕹️ 세상에서 가장 신나는 가위✌️ 바위✊ 보🖐️ 게임!")
st.markdown("### 나와 컴퓨터의 운명을 가려보자! 🎲🔥")

choices = {"가위 ✌️": "scissors", "바위 ✊": "rock", "보 🖐️": "paper"}
emoji_result = {
    "win": "🎉 승리! 축하해요! 🏆",
    "lose": "😢 패배! 다음엔 이길 수 있어요!",
    "draw": "🤝 비겼어요! 다시 도전해볼까요?"
}

user_choice = st.radio("👉 선택하세요!", list(choices.keys()), index=0)

if st.button("🎯 컴퓨터와 대결!"):
    computer_choice_key = random.choice(list(choices.keys()))
    computer_choice = choices[computer_choice_key]

    user_pick = choices[user_choice]

    # 결과 판정
    if user_pick == computer_choice:
        result = "draw"
    elif (user_pick == "rock" and computer_cho
