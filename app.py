import os
from telethon import TelegramClient, events

# دریافت اطلاعات API از محیط
api_id = int(os.environ.get('TELEGRAM_API_ID'))
api_hash = os.environ.get('TELEGRAM_API_HASH')
phone_number = os.environ.get('PHONE_NUMBER')
target_user = os.environ.get('TARGET_USER')

# ایجاد کلاینت تلگرام
client = TelegramClient('session', api_id, api_hash)

# اتصال و شروع کلاینت
async def main():
    await client.start(phone=phone_number)
    
    # بررسی عضویت در کانال مورد نظر
    channel = await client.get_entity('channel_username')  # جایگزین با یوزرنیم کانال

    # تنظیم رویداد برای دریافت پیام‌های کانال
    @client.on(events.NewMessage(chats=channel))
    async def handler(event):
        message = event.message.message
        await client.send_message(target_user, message)

    print("Bot is running...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
