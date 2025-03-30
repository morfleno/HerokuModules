"""
  __  __                  _
 |  \/  |                | |
 | \  / | ___  _ __ _ __ | |__
 | |\/| |/ _ \| '__| '_ \| '_ \
 | |  | | (_) | |  | |_) | | | |
 |_|  |_|\___/|_|  | .__/|_| |_|
                   | |
                   |_|
"""
# meta developer: @morphmods

from telethon.tl.types import Message
from .. import loader, utils
import logging

logger = logging.getLogger(__name__)

@loader.tds
class MorphPM(loader.Module):
    """Модуль для отправки личных сообщений"""
    strings = {"name": "MorphPM"}

    @loader.command(
        ru_doc="Команда отправки личных сообщений",
    )
    async def pm(self, message: Message):
        """Отправить личное сообщение пользователю"""
        args = message.text.split(maxsplit=2)

        if len(args) < 2:
            await utils.answer(message, "⚠️ Используйте: .pm <username> <текст> или .pm <текст>.")
            return

        if len(args) == 3:
            username = args[1].lstrip('@')
            text = args[2]
        else:
            username = message.sender.username
            text = args[1]

        if not username:
            await utils.answer(message, "⚠️ Вы должны указать username или использовать команду без него.")
            return

        try:
            user = await message.client.get_entity(username)
            await message.client.send_message(user.id, text)
            await utils.answer(message, f"✅ Сообщение успешно отправлено.")
        except Exception as e:
            await utils.answer(message, f"❌ Не удалось отправить сообщение пользователю {username}. Ошибка: {str(e)}")
