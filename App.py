import streamlit as st
import YoutubeVideo as yt
import os

st.set_page_config(page_title="YouTube Downloader", layout="wide")
st.title("YouTube Video Downloader")

# UI component
link = st.text_input("Please provide the video link")
q = st.sidebar.radio("Select the quality ", ["144p", "240p","360p", "480p", "720p", "1080p",
                                              "1440p", "2160p"])

# Exixting Video removal
if not os.path.exists("./out"):
    os.mkdir("out")
else:
    try:
        os.remove("./out/video.mp4")
    except:
        pass

# Download system
if st.button("Download"):
    if link == "":
        st.warning("Please Provide link")
    else:
        if yt.VideoChecker(link, q):
            yt.Download(link, q)
            st.success("Your Video is found, download using the video menu")
            st.video("./out/video.mp4")
        else:
            st.error("Video Unavailable, Please try with different quality")
