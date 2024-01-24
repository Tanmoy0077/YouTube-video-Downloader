import streamlit as st
import YoutubeVideo as yt

st.set_page_config(page_title="YouTube Downloader", layout="wide")
st.title("YouTube Video Downloader")
link = st.text_input("Enter the video link")
q = st.sidebar.radio("Select the quality ", ["240p","360p", "480p", "720p", "1080p", "2160p"])

# if st.button("Check"):
#     if link == "":
#         st.write("Please Provide link")
#     else:
#         try:
#             if yt.VideoChecker(link, q):
#                 st.write("Video Available")
#             else:
#                 st.write("Video Unavailable")
#         except:
#             st.write("Invalid Link")

if st.button("Download"):
    if link == "":
        st.warning("Please Provide link")
    else:
        try:
            if yt.VideoChecker(link, q):
                st.button("Get File",data=yt.Download(link, q))
            else:
                st.warning("Video Unavailable")
        except:
            st.error("Invalid Link")

with st.form("Test form"):
    link = st.text_input("This is inside form")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if link == "":
            st.warning("Please Provide link")
        else:
            try:
                if yt.VideoChecker(link, q):
                    yt.Download(link, q)
                    st.success("Download Successfull")
                else:
                    st.warning("Video Unavailable")
            except:
                st.error("Invalid Link")
    
