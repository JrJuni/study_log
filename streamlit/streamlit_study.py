import streamlit as st

st.set_page_config(
    page_title="Streamlit Study",
    page_icon=":tada:",
    layout="wide"
)

list_name = {"Project 1": "Project 1", "Project 2": "Project 2", "Project 3": "Project 3"}

with st.form("db"):
    name = st.text_input("Name")
    projects = st.multiselect(label="Projects", options=list(list_name.keys()), max_selections=3)
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.write(f"Hello {name}!")
        st.write(f"Projects: {projects}")
        st.write(f"Projects: {list_name[projects[0]]}")

st.title("Streamlit Study")

st.write("Heladlo World")