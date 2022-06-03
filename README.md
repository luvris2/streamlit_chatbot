# 심리상담 챗봇

심리상담 정신건강 상담 챗봇. AI chatbot for psychology consultation.

![chatbot_ex](https://user-images.githubusercontent.com/105832446/171950293-b2b7bdca-8833-444d-99af-5616ef389290.png)

## Pretrained Model

SentenceBERT [jhgan/ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask)

## Dataset

[웰니스 대화 스크립트 데이터셋](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006)
https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006

## Dependency

- streamlit
- streamlit-chat
- pandas
- sentence-transformers
- scikit-learn

## 파이썬 파일
app.py : 메인 파일
simple_chatbot.ipynb : 모델 로드와 데이터 가공, 전처리 과정이 담겨 있는 파일
test.py : 간단한 테스트 파일, streamlit_chat 라이브러리 호출 확인용
 
## 추가 데이터 파일
AI_chatbot.pkl : 모델링 정보를 저장, 캐쉬를 사용하지 않고 사용 할 때 사용하기 위함 (선택)
wellness_dataset ~ .csv : AI Hub에서 제공하는 웰니스 대화 데이터셋, 원본 파일과 가공된 파일