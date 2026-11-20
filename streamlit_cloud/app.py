"""Streamlit Community Cloud portfolio adapter for persanal-assistance.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "Alex — Python Voice Assistant"
ICON = "🎙️"
DESC = "Command-driven desktop assistant using speech recognition, speech synthesis, web search and notes."
CATEGORY = "Desktop Python assistant"
NOTICE = "The original voice assistant needs a microphone, speaker and persistent local process. The Streamlit view is a portfolio page; it does not capture or process voice."
GITHUB = "https://github.com/mohsinattasial/persanal-assistance"
VERCEL = "https://mohsin-alex-assistant.vercel.app"
LOCAL_COMMAND = "python assistance.py"
FEATURES = ["Voice-triggered desktop commands","Wikipedia and web lookups","Notes and time-based reminders"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

st.subheader("Project overview")
st.write("This page is a deployable portfolio presentation of the original repository. Use the GitHub link above to inspect the code and run it in its intended local environment.")

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")
