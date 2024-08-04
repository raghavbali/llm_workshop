## import required components

import pandas as pd
from utils import (
    get_lines,
    load_data,
    get_relevant_documents,
    get_answer,
    create_db,
    sidebar,
)
import streamlit as st
chroma_client, db = create_db()

## Setup Page Header and Sidebar
st.set_page_config(page_title="PersonalGPT", page_icon="📖", layout="wide")
lm_model = sidebar()
st.header(f"📖PersonalGPT")
st.markdown(f">:zap: Responses Powered by **{lm_model}**")

if 'is_doc_uploaded' not in st.session_state:
    st.session_state['is_doc_uploaded'] = False


## Add Uploader Component
uploaded_file = st.file_uploader(
    "Upload a txt file",
    type=["txt"],
    help="Text files with each sentence acting as a document",
)

if not st.session_state['is_doc_uploaded']:
    ## Check if upload is complete
    if not uploaded_file:
        st.stop()
    
    ## Read uploaded file
    try:
        file_data = get_lines(uploaded_file)
        ## Verbose Status update
        st.markdown(f"> Uploaded file has {len(file_data)} lines of text")
        st.session_state['is_doc_uploaded'] = True
    except Exception as e:
        st.markdown(f"Could not upload/read file={e}")
        st.session_state['is_doc_uploaded'] = False
    
    ## Index Uploaded text file
    with st.spinner("Indexing document... This may take a while⏳"):
        db_status_msg = load_data(db, documents=file_data)
    
    ## status update
    st.markdown(f"> Database indexed {db.count()} documents")
    if db.count() == 0:
        st.markdown(db_status_msg)
        st.session_state['is_doc_uploaded'] = False

## Get User Input
with st.form(key="qa_form"):
    query = st.text_area("Enter Your Query:",placeholder="Examples: \nwhat is tf-idf?\nwhich module covers RLHF\nhow many moons does Jupiter have?")
    submit = st.form_submit_button("Submit")

## Provide additional Options for citing source
with st.expander("Advanced Options"):
    show_source = st.checkbox("Show Source")

## Generate Output upon button click
if submit:
  # Get relevant documents from DB
  context = get_relevant_documents(query, db)

  # get answer from LLM
  answer,score,error = get_answer(query,context,lm_model)

  # Showcase response on screen
  st.markdown(f"**Answer:** _{answer}_")
  st.markdown(f"> **Relevance Score**:{score}")
  st.markdown("---")

  # Add more details if advanced option is chosen
  if show_source:
    st.markdown("**Source(s):**")
    st.markdown(f"- <i>{context[:100]}...</i>", unsafe_allow_html=True)
