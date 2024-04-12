import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
import os
from dotenv import load_dotenv
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
GROUP_LINK = os.getenv("GROUP_LINK")

async def send_weekly_message():
    # Initialize the client with a session file. It will be created on the first run.
    client = TelegramClient('my_telegram_session', API_ID, API_HASH)

    await client.start(phone=PHONE_NUMBER)
    print("Client Created")
    # Ensure you're authorized
    if await client.is_user_authorized() == False:
        await client.send_code_request(PHONE_NUMBER)
        try:
            await client.sign_in(PHONE_NUMBER, input('Enter the code: '))
        except Exception:
            await client.sign_in(password=input('Password: '))

    await client.send_message(GROUP_LINK, 'The weekly message.')
    await client.disconnect()

def schedule_messages():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_weekly_message())

if __name__ == '__main__':
    schedule_messages()