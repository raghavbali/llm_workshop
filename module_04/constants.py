#####################
## Set Constants
#####################
HF_TOKEN = '<YOUR KEY>'
OPENAI_TOKEN = '<YOUR KEY>'
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# Constants for embedding model
EMB_MODEL_ID = 'pinecone/mpnet-retriever-discourse'
EMB_API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{EMB_MODEL_ID}"

# Constants for QA model
QA_MODEL_ID = 'deepset/roberta-base-squad2'

# List of Different Endpoints
HF_QA_ENDPOINT = 'HF-QA'
HF_LM_ENDPOINT = 'HF-LM'
OPENAI_ENDPOINT = 'OPENAI-LM'
LOCAL_OLLAMA_ENDPOINT = 'OLLAMA'
AVAILABLE_LMs = {
    'models':
    [
        'deepset/roberta-base-squad2',
        'Intel/dynamic_tinybert',
        #'google/gemma-2-2b-it', # this is timing out mostly
        'Local-LLAMA-3.1:8b',
        'OpenAI-GPT4o-mini'
    ],
    'endpoints':
    [
        HF_QA_ENDPOINT,
        HF_QA_ENDPOINT,
        #HF_LM_ENDPOINT, #this is timing out mostly
        LOCAL_OLLAMA_ENDPOINT,
        OPENAI_ENDPOINT,
    ]
}