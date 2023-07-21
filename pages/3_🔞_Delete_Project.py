import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Delete Project", page_icon="🔞")

st.markdown("# 🔞 Delete Project")

st.write(
    """Follow the steps below to remove a project from the APEX Project Database"""
)