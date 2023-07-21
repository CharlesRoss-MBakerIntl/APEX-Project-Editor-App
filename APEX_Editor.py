import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# APEX Project Editing Application 📝")


st.markdown(
    """
    Application developed to add, updates, or delete projects associated with the Alaska State Department of Transportation
    APEX Contstuction Management Program.

    **👈 Select an action from the sidebar** to begin your editing session
    """
)