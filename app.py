import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json
import joblib
try:
    from typing import Literal # 파이썬 3.8
except ImportError:
    from typing_extensions import Literal # 파이썬 3.7 이하

@st.cache(allow_output_mutation=True)
def cached_model():
    model = joblib.load('data/AI_chatbot.pkl')
    #model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('data/wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('심리상담 챗봇')
st.markdown('심리상담 챗봇입니다.')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# 텍스트를 입력하여 봇과 대화 할 수 있는 폼 생성
# clear_on_submit 옵션을 통해서 submit 하면 폼의 내용이 지워짐
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('당신 : ', '')
    submitted = st.form_submit_button('전송')

# 메시지를 입력 후 전송을 누를 경우
if submitted and user_input:
    embedding = model.encode(user_input)
    # 입력한 메시지의 유사도를 확인하여 가장 가까운 답변을 제시
    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[ df['distance'].idxmax() ]

    # ???
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer['챗봇'])
# ??? 유저와 챗봇 대화 내용 추가 (대화 내용 보여주기)
for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i], key=str(i) + '_bot')