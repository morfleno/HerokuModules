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
class MorphLeaver(loader.Module):
    """Модуль для выхода из чатов"""
    strings = {"name": "MorphLeaver"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "leave_message",
                "Я покидаю этот чат. До свидания!",
                "Сообщение, отправляемое перед выходом из чата.",
                validator=loader.validators.String(),
            ),
        )

    @loader.command(
        ru_doc="Выйти из указанного чата",
    )
    async def leave(self, message: Message):
        """Выйти из указанного чата"""
        if not message.is_group:
            await utils.answer(message, "Эта команда работает только в группах.")
            return

        chat_id = message.chat.id  # Идентификатор текущего чата
        leave_message = self.config.get("leave_message")

        await utils.answer(chat_id, leave_message)
        await message.client.kick_participant(chat_id, message.sender_id)