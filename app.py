import streamlit as st

st.header("Data Science :red[Internship_2K23#]")
st.snow()

st.header("Hello!   I'am :green[Pradyumna] & Welcome to my :blue[Streamlit_web_App]")

st.subheader("Dashbords on :orange[Iris Data]")

CODE = '''print("created on using VS_code")'''

st.code(CODE, language="python")

btn_click = st.button("Click Me!")
st.write(btn_click)

if btn_click == True: 
    st.subheader("you Clicked me :sunglasses:")
    st.balloons()

