import unittest
from unittest.mock import AsyncMock
from project.handlers.user import command_start_handler

class TestCommandStartHandler(unittest.IsolatedAsyncioTestCase):

    async def test_command_start_handler(self):
        message = AsyncMock()
        message.from_user.full_name = "Test User"
        message.answer = AsyncMock()
        await command_start_handler(message)
        message.answer.assert_awaited_with('<b>Test User</b>, добро пожаловать!\nВас приветствует <b>WorkoutBot!</b>')


if __name__ == '__main__':
    unittest.main()
