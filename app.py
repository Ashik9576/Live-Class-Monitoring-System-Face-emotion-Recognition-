import streamlit as st
from PIL import Image
from model_predict import *
from streamlit_webrtc import webrtc_streamer

st.title("✨ Welcome ✨")
st.sidebar.title("🎇Choose an options🎇")
choice_options=st.sidebar.selectbox("",('Home','Start webcam','About'))

if choice_options=="Home":
    st.title('👨Face Emotion Recognition using Live Web Camera👩')
    image = Image.open('data/face.jpeg')
    st.image(image)
    st.sidebar.subheader("""💎 Face Emotion Recognition is a system used to detect the emotions from face.""")
    st.sidebar.subheader("""💎 Nowadays it is widely used applications.Eg: In zoom meeting we can able to detect the student emotion.""")
    st.sidebar.subheader("""💎 It is very helpful for teachers where they can able to teach based on their students emotion and make class more interactive.""")
if choice_options=="Start webcam":
    st.header("Webcam Live Feed")
    st.write("Click on start to use webcam and detect your face emotion")
    webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
if choice_options=="About":
    st.title('Project Members')
    col1, col2= st.columns(2)
    with col1:
        image_1= Image.open('data/ape.png')
        st.subheader("Ashik Kumar")
        st.image(image_1)
        st.write("Email:ashikkumar491@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/ashik-kumar-94a06a207)""")
    with col2:
        image_2 = Image.open('data/jai.png')
        st.subheader("Jai Harish S")
        st.image(image_2)
        st.write("Email:jaiharishs361@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/jai-harish-s-64b1b01ab)""")

    col1, col2= st.columns(2)
    with col1:
        image_3 = Image.open('data/pranil.png')
        st.subheader("Pranil Satish Thorat")
        st.image(image_3)
        st.write("Email:pranilthorat@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/pranil-thorat-834361216)""")
    with col2:
        image_4 = Image.open('data/saransh.png')
        st.subheader("Saransh Srivastava")
        st.image(image_4)
        st.write("Email:saranshoffice@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/saranshsrivastava13)""")
    col1, col2= st.columns(2)
    with col1:
        image_5 = Image.open('data/akasl.png')
        st.subheader("Bhaskar subanji")
        st.image(image_5)
        st.write("Email:bysubanji@gmail.com")
        st.markdown("""[LinkedIn profile](https://www.linkedin.com/in/bysubanji)""")
    with col2:
        pass


