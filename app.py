# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 AI 대시보드 예시")

# 예제 데이터
df = pd.DataFrame({
    "날짜": pd.date_range("2025-01-01", periods=7),
    "예측 값": [100, 120, 130, 90, 80, 150, 170]
})

# 라인 차트
st.line_chart(df.set_index("날짜"))

# 표 보기
if st.checkbox("데이터 보기"):
    st.write(df)

# 요약 통계 기능 추가
st.subheader("📌 예측 값 요약 통계")
summary = df["예측 값"].describe()
st.write(summary)
