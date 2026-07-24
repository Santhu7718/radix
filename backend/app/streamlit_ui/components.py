import streamlit as st


def hero(title, subtitle):

    st.markdown(
        f"""
<div class="hero">

<h1>{title}</h1>

<p>{subtitle}</p>

</div>
""",
        unsafe_allow_html=True,
    )


def section(title):

    st.markdown(
        f"""
<div class="page-title">

<h2>{title}</h2>

</div>
""",
        unsafe_allow_html=True,
    )


def metric_card(title, value, icon="📊"):

    st.markdown(
        f"""
<div class="card">

<div class="metric-title">

{icon} {title}

</div>

<div class="metric-value">

{value}

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def chip(text, color="blue"):

    classes = {
        "green": "green-chip",
        "red": "red-chip",
        "blue": "blue-chip"
    }

    st.markdown(
        f'<span class="{classes[color]}">{text}</span>',
        unsafe_allow_html=True,
    )