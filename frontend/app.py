import streamlit as st
import requests
import streamlit.components.v1 as components

BACKEND_URL = "http://localhost:8001"

st.set_page_config(
    page_title="Policy Comparison Assistant",
    layout="wide"
)

st.title(
    "📄 Policy Comparison Assistant"
)

col1, col2 = st.columns(2)

with col1:
    legacy_file = st.file_uploader(
        "Upload Legacy Policy",
        type=["pdf", "docx", "txt"]
    )

with col2:
    modern_file = st.file_uploader(
        "Upload Modernized Policy",
        type=["pdf", "docx", "txt"]
    )

if st.button("Analyze Policies"):

    if legacy_file and modern_file:

        with st.spinner(
                "Analyzing policies..."):

            files = {
                "legacy": (
                    legacy_file.name,
                    legacy_file,
                    legacy_file.type
                ),
                "modern": (
                    modern_file.name,
                    modern_file,
                    modern_file.type
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/compare",
                files=files,
                timeout=600
            )

            result = response.json()

            tab1, tab2 = st.tabs(
                [
                    "Semantic Analysis",
                    "Text Diff"
                ]
            )

            with tab1:
                st.markdown(
                    result["analysis"]
                )

            with tab2:
                components.html(
                    result["diff_html"],
                    height=900,
                    scrolling=True
                )
