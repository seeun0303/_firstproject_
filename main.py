import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="가위✌️바위✊보🖐️ 게임",
    page_icon="🎮",
    layout="centered"
)

# 배경색 및 스타일링
st.markdown(
    """
    <style>
    body {
        background-color: #FFF8DC;
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1 {
        color: #E63946;
        text-align: center;
        font-size: 50px;
        margin-bottom: 0;
    }
    .stRadio > div > label {
        font-size: 24px;
        padding: 8px 20px;
    }
    .stButton button {
        background-color: #457B9D;
        color: white;
        font-size: 24px;
        padding: 10px 30px;
        border-radius: 12px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 타이틀과 설명
st.title("🎮 컴퓨터와 가위✌️바위✊보🖐️ 게임!")
st.write("아래에서 선택하고 ‘컴퓨터와 대결!’ 버튼을 눌러 보세요.")

# 선택지와 매핑
choices = {"가위 ✌️": "scissors", "바위 ✊": "rock", "보 🖐️": "paper"}

# 사용자 입력
user_choice_text = st.radio("당신의 선택:", list(choices.keys()), index=0)

if st.button("👊 컴퓨터와 대결!"):
    # 컴퓨터 랜덤 선택
    computer_choice_text = random.choice(list(choices.keys()))
    user_choice = choices[user_choice_text]
    computer_choice = choices[computer_choice_text]

    # 결과 판정
    if user_choice == computer_choice:
        result_text = "🤝 비겼어요! 다시 도전해보세요!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_text = "🎉 당신이 이겼어요! 축하합니다! 🏆"
    else:
        result_text = "😢 컴퓨터가 이겼어요! 다음엔 꼭 이겨봐요!"

    # 결과 출력
    st.markdown(f"### 🙋 당신의 선택: **{user_choice_text}**")
    st.markdown(f"### 🖥️ 컴퓨터의 선택: **{computer_choice_text}**")
    st.markdown(f"## {result_text}")

    # 승리 시 풍선 효과, 패배 시 눈 효
