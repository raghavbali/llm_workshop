#####################
## imports
#####################
import pandas as pd
import json
import requests
from retry import retry
import streamlit as st
import chromadb.utils.embedding_functions as embedding_functions
from huggingface_hub import InferenceClient
from openai import OpenAI
import ollama
from constants import (
    HF_TOKEN,
    OPENAI_TOKEN,
    HEADERS,
    EMB_MODEL_ID,
    EMB_API_URL,
    QA_MODEL_ID,
    HF_QA_ENDPOINT,
    HF_LM_ENDPOINT,
    OPENAI_ENDPOINT,
    LOCAL_OLLAMA_ENDPOINT,
    AVAILABLE_LMs)


import chromadb


lm_df = pd.DataFrame.from_dict(AVAILABLE_LMs)

#####################
## Utility Functions
#####################

def get_lines(uploaded_file):
  """
    Utility to read raw text file in binary
  """
  raw_data = []
  for line in uploaded_file:
        raw_data.append(line.decode("utf-8") )
  return raw_data

def create_db():
  """
    Utility to instantiate vector db client and collection
  """
  chroma_client = chromadb.Client()
  # huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
  #     api_key=HF_TOKEN,
  #     model_name=EMB_MODEL_ID
  # )
  db = chroma_client.get_or_create_collection(name="nlp_llm_workshop",)
                                      #embedding_function=huggingface_ef)
  return chroma_client,db

def load_data(db, documents):
  """
    Utility to add/index data into vector db
  """
  try:
      db.add(
          documents=documents,
          ids=[str(i) for i in range(len(documents))]
  )
  except Exception as ex:
      return "Apologies but I could not ingest document", 0.0, ex

def get_relevant_documents(query, db):
  """
    Utility to retrieve relevant documents from vector DB
  """
  try:
      relevant_doc = db.query(query_texts=[query], n_results=1)['documents'][0][0]
      return relevant_doc
  except Exception as ex:
      return "Apologies but I could not process your query", 0.0, ex

def get_hf_qa_answer(payload,lm_model):
    data = json.dumps(payload)
    try:
      QA_API_URL = f"https://api-inference.huggingface.co/models/{lm_model}" 
      response = requests.request("POST", QA_API_URL, headers=HEADERS, data=data)
      decoded_response = json.loads(response.content.decode("utf-8"))
      return decoded_response['answer'], decoded_response['score'], ""
    except Exception as ex:
      return "Apologies but I could not find any relevant answer", 0.0, ex

# this is mostly timing out
def get_hf_llm_answer(payload,lm_model):
    try:
        client = InferenceClient(
        "google/gemma-2-2b-it",
        token=HF_TOKEN,)

        content = f"Given the context, answer the question. \ncontext:{payload['context']}\nquestion:{payload['question']}"
        response= client.chat_completion(
    	messages=[{"role": "user", "content": content}],
    	max_tokens=500,
    	stream=False,
        )
    
        return json.loads(message.choices[0].delta.content), 0.0 
    except Exception as ex:
      return "Apologies but I could not find any relevant answer", 0.0, ex

def get_local_llama_answer(payload,lm_model):
    try:
        content = f"Given the context, perform the following tasks:1.Respond with a summarized answer to the question factually in few words only if the provided context contains the answer\n2.Check if your answer is really in the provided context, otherwise respond with 'Sorry I could not find the answer'.\n 3.Generate a relevance score between 0 and 1.\n4. Format the output as a json with answer and score as keys.\n5.Do not add makrdown syntax only respond with json.\nBe careful and Think step by step.\ncontext:{payload['context']}\nquestion:{payload['question']}"
        response = ollama.chat(model='llama3.1:8b', messages=[
            {
                'role': 'user',
                'content': content,
            },
        ]
                              )
        json_output = json.loads(response['message']['content'])
        return json_output['answer'], json_output['score'], ""
    except Exception as ex:
      st.markdown(ex)
      return "Apologies but I could not find any relevant answer", 0.0, ex
        
def get_opeai_answer(payload,lm_model):
    try:
        client = OpenAI(
            api_key=OPENAI_TOKEN,
        )
        content = f"Given the context, perform the following tasks:1.Respond with a summarized answer to the question factually in few words only if the provided context contains the answer\n 2.Generate a relevance score.\n3. Format the output as a json with answer and score as keys. Do not add makrdown syntax.\nThink step by step.\ncontext:{payload['context']}\nquestion:{payload['question']}"
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model="gpt-4o-mini",
        )
        json_output = json.loads(chat_completion.choices[0].message.content)
        return json_output['answer'], json_output['score'], ""
    except Exception as ex:
      return "Apologies but I could not find any relevant answer", 0.0, ex


def get_answer(question,context,lm_model):
    """
      Utility to leverage QA model for answering question using given context
      and the mentioned model
    """
    payload = {
        "question": question,
        "context":context
    }
    try:
      endpoint_type = lm_df[lm_df['models']==lm_model]['endpoints'].values[0]  
      if endpoint_type == HF_QA_ENDPOINT:
          return get_hf_qa_answer(payload,lm_model)
      elif endpoint_type == HF_LM_ENDPOINT:  
          return get_hf_llm_answer(payload,lm_model)
      elif endpoint_type == OPENAI_ENDPOINT: 
          return get_opeai_answer(payload,lm_model)
      elif endpoint_type == LOCAL_OLLAMA_ENDPOINT:
          return get_local_llama_answer(payload,lm_model)
      else:
          "This is not implemented yet", 0.0, ex
    except Exception as ex:
      return "Apologies but I could not find any relevant answer", 0.0, ex


def sidebar():
    """
      Utility to add content to sidebar
    """
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload a txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        st.markdown("---")
        st.markdown("## Which LM would you like to use?")
        option = st.selectbox(
            "Select a Model",
             lm_df['models'],
            label_visibility='hidden'
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖PersonalGPT is a demo to showcase retrieval augmented question answering system"
        )
        st.markdown(":heart: Made by [raghav bali](https://raghavbali.github.io)")
        st.markdown("---")

        return option