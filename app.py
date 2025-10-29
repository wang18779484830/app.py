import srreamlit as st
st.title("Streamlit 테스트 앱")
st.write("Hello World")
name = st.text_input("이름을 입력하세요:")
if st.button("인사하기"):
    st.success(f"안녕하세요,(name)님!")
    
