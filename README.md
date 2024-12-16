# 텔레그램 채팅방 리스트 조회 프로그램

텔레그램 API를 사용하여 사용자의 채팅방 목록을 조회하는 콘솔 프로그램입니다.

## 설치 방법

1. Python 가상환경 생성 및 활성화 
```
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

2. 필요한 패키지 설치
```
pip install -r requirements.txt
```


3. 환경 변수 설정
- `.env.sample` 파일을 복사하여 `.env` 파일 생성
- Telegram API ID와 API Hash 입력
  - API 정보는 https://my.telegram.org 에서 얻을 수 있습니다

## 실행 방법
```
python main.py
```

## 필요 패키지 목록
- telethon
- python-dotenv
