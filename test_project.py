import pytest

from discord.ext import commands
from unittest.mock import AsyncMock, patch
from project import create_bot, load_extensions,setup_events


@pytest.fixture
def bot():
    return create_bot()


def test_create_bot(bot):
    assert isinstance(bot, commands.Bot)
    assert bot.command_prefix == "!"
    assert bot.intents.message_content is True


@pytest.mark.asyncio
async def test_load_extensions(bot):
    with patch.object(bot, 'load_extension', new_callable=AsyncMock) as mock_load_extension:
        await load_extensions(bot)

        mock_load_extension.assert_any_call("cogs.stratusgpt")
        mock_load_extension.assert_any_call("cogs.weather")
        mock_load_extension.assert_any_call("cogs.prompt")
        mock_load_extension.assert_any_call("cogs.wprompt")

        assert mock_load_extension.call_count == 4


@pytest.mark.asyncio
async def test_setup_events(bot):
    setup_events(bot)

    assert hasattr(bot, "on_ready")
    assert hasattr(bot, "on_message")

    bot.process_commands = AsyncMock()
    message = AsyncMock()
    await bot.on_message(message)
    bot.process_commands.assert_called_once_with(message)
