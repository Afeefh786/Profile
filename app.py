import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
cnn_project_image = Image.open("images/CNN_PROJECT.png")
Heart_Disease_Prediction_using_Machine_Learning = Image.open("images/Heart_Disease_Prediction_using_Machine_Learning.png")

# ---- HEADER SECTION ----
with st.container():
    st.title("Hi, I am Mohammed Afeef Hussain :wave:")
    st.title("A Cyber Security Analyst From Bangalore")
    st.write(
        "I am passionate about finding ways to use Python and Networking used in Cyber Security to be more efficient and effective in business settings."
    )
# --- Skills---
with st.container():
    st.title("Skills")
    st.subheader("Programming Languages")
    st.write(
        "C, C++, Python, Java."
    )
    st.subheader("Technologies")
    st.write("Power BI, JQuery, PERL, NumPy, SIEM, AWS, CSS, Linux, Git, GitHub, MS Excel, Website Design.")
    st.subheader("Others Skills")
    st.write("Pivot Tables, Code Design, Malware Analysis, Application Security, Touch Typing.")
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.title("Jr.Cyber Security Analyst.")
        st.write(
            """
            
            Network Intelligence India Pvt Ltd.

            08.2022 – 12.2023

            Bangalore, India

            -Providing Cyber Security Operations Center support on a 24x7x365 basis by shift work with rotation.
    
            -Continuous monitoring of alert queues on the SIEM console

            -Identify False Positive, and True Positive.

            -Handling Alert on SIEM Dashboard by creating tickets.
            """
        )
       
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(cnn_project_image)
    with text_column:
        st.subheader("Using CNN detection of diseased leaf and recommendation system")
        st.write(
            """
            • This was my Final year Project of Engineering Using Convolutional Network we tried to detect a diseased leaf in the plant

            • We Collected World Data from about 10,000 leaves, and the Project's accuracy was about 90%.
            """
        )
        


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Heart_Disease_Prediction_using_Machine_Learning)
    with text_column:
        st.subheader("Heart Attack Prediction Analysis")
        st.write(
            """
            • Using Algorithms, Machine learning describes systems that make predictions using a model trained on real-world data.
            """
        )
        

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mohammedafeefh@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
