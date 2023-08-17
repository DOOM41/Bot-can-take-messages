import httpx
from conf import URL

async def set_bot_code(bot_code, chat_id):
    async with httpx.AsyncClient() as client:
        url = URL+"set-bot-code/"  # Замените на ваш реальный URL эндпоинта
        json_data = {
            "bot_code": bot_code,
            "chat_id": str(chat_id)
        }
        
        response = await client.post(url, json=json_data)

        if response.status_code == 200:
            return True
        return False

