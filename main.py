import streamlit as st

# MBTI 궁합 데이터 (예시, 실제 궁합과는 다를 수 있습니다)
# 각 MBTI 유형에 따른 추천 배우자 MBTI 유형 리스트
mbti_compatibility = {
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "INFJ": ["ENFP", "ENTP"],
    "INTJ": ["ENFP", "ENTP"],
    "ISTP": ["ESFJ", "ENFJ"],
    "ISFP": ["ESFJ", "ENFJ"],
    "INFP": ["ENFJ", "ENTJ"],
    "INTP": ["ENFJ", "ENTJ"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ESFP": ["ISFJ", "ISTJ"],
    "ENFP": ["INFJ", "INTJ"],
    "ENTP": ["INFJ", "INTJ"],
    "ESTJ": ["INFP", "INTP"],
    "ESFJ": ["INFP", "INTP"],
    "ENFJ": ["ISTP", "ISFP"],
    "ENTJ": ["ISTP", "ISFP"],
}

st.title("💖 나의 MBTI와 어울리는 배우자 찾기 앱")
st.write("당신의 MBTI를 선택하면, 좋은 배우자가 될 수 있는 MBTI 유형을 추천해 드립니다.")

# 사용자 MBTI 선택
user_mbti = st.selectbox(
    "당신의 MBTI 유형을 선택하세요:",
    list(mbti_compatibility.keys())
)

if st.button("추천 배우자 찾기"):
    if user_mbti:
        recommended_mbtis = mbti_compatibility.get(user_mbti, ["정보 없음"])
        st.subheader(f"✨ 당신의 MBTI '{user_mbti}'와 잘 어울리는 배우자 유형은 다음과 같아요:")
        for mbti in recommended_mbtis:
            st.write(f"- **{mbti}**")
        st.markdown(
            """
            <br>
            <p style='font-size: small; color: gray;'>
            * 이 추천은 일반적인 MBTI 궁합론에 기반한 예시이며, 실제 인간관계는 다양한 요인에 의해 영향을 받습니다. 
            MBTI는 참고 자료로만 활용하시고, 개개인의 성격과 가치관을 존중하는 것이 중요합니다.
            </p>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.warning("MBTI 유형을 선택해주세요!")
