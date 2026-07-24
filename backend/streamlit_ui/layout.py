import streamlit as st

def page(title):

    st.markdown(f"""
    <div class="page-title">

    <h1>{title}</h1>

    </div>
    """, unsafe_allow_html=True)