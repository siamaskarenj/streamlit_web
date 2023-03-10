from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="my frist webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

lottie_coding=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

#---------header section
with st.container():
    st.subheader("Hi,I am Marshal :wave:")
    st.title(" A Researcher From Belgium ")
    st.write("I am super passionate about daylight energy  and building stimulation ")
    st.write("[Learn More > ](https://www.researchgate.net)")


#_____what  i do

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
with left_column:
    st.header("what I do")
    st.write("##")
    st.write("""Marshal is working as FNRS Postdoctoral research fellow at Universit√© Catholique de Louvain, Belgium. He formerly served as Chair for MTech program in Building Energy Performance at CEPT University, Ahmedabad, India. He has also worked as consultant/advisor for Energy Lab at IIHS Bangalore, India, as part of Solar Decathlon India initiative.
He holds an integrated MSc-PhD degree in Energy Science and Engineering from IIT Bombay, and has research interest in building lighting/daylight, visual comfort and overall building performance evaluation through measurement and simulation.
""")
    st.write("[linkedin profile > ](https://be.linkedin.com)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Research")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)


        with text_column:
            st.subheader("integrate lottie animation inside your streamlit app")
            st.write("""learn how to use lottie files in streamlit!Animations make our web app more engaging and fun, and lottie files are the easiest way todo in this tutorial thank you""")
            st.markdown("[watch vedio...]")


with st.container():
    st.write("---")
    st.header("Get In Touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/shilpadummymybebu@gmil.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name ="message" placeholder="your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
