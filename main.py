import streamlit as st
import utils, os

st.title('Rätsel für Scotland Yard')

ort = st.selectbox('Ort', sorted([p.replace(".md", "") for p in os.listdir('pages')]))

st.markdown(utils.read_markdown_file(f"pages/{ort}.md"), unsafe_allow_html=True)