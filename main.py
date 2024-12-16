from telethon import TelegramClient, events
import asyncio
import os
from dotenv import load_dotenv

class TelegramLogin:
    def __init__(self):
        load_dotenv()
        
        # Telegram API 정보
        self.api_id = os.getenv('API_ID')  # Telegram API ID
        self.api_hash = os.getenv('API_HASH')  # Telegram API Hash
        
        self.client = None
        
    async def get_dialogs(self, username):
        async with TelegramClient(username, self.api_id, self.api_hash) as client:
            self.client = client
            try:
                print("대화방 목록:")
                print("-" * 30)
                # 대화방 목록 가져오기
                async for dialog in client.iter_dialogs():
                    print(f"{dialog.name} ({dialog.id})")
            except Exception as e:
                print(f'오류: 대화방 목록을 가져오는 중 오류 발생: {str(e)}')
    
    def login(self):
        # API 정보 확인
        if not self.api_id or not self.api_hash:
            print('오류: API ID 또는 API Hash가 설정되지 않았습니다.')
            return
            
        username = input("텔레그램 사용자명을 입력하세요 (@포함): ")
        if not username.startswith('@'):
            print('경고: 사용자명은 @로 시작해야 합니다.')
            return
            
            
        # 비동기 작업 실행
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.get_dialogs(username))

def main():
    app = TelegramLogin()
    app.login()

if __name__ == '__main__':
    main() 