from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from config.app import dp
from models import User


class OrderStates(StatesGroup):
    test_state1 = State()
    test_state2 = State()


@dp.message_handler(commands=['start'], content_types=types.ContentTypes.TEXT, state="*")
async def all_other_messages(message: types.Message):
    if not User.find(message.from_user.id):
        user = User()
        user.id = message.from_user.id
        user.first_name = message.from_user.first_name
        user.last_name = message.from_user.last_name
        user.username = message.from_user.username
        user.save()
    await message.answer('Welcome!')


@dp.message_handler(commands=['admin'], content_types=types.ContentTypes.TEXT, state='*')
async def get_admin_info(message: types.Message):
    user = User.find(message.from_user.id)
    if user.is_admin:
        await message.reply('You are admin!')
    else:
        await message.reply('Permission deny!')


@dp.message_handler(commands=['test_states'], content_types=types.ContentTypes.TEXT, state='*')
async def test_states(message: types.Message):
    await message.answer('Start testing states!\nSend any text to continue.')
    await OrderStates.test_state1.set()


@dp.message_handler(content_types=types.ContentTypes.ANY, state=OrderStates.test_state1)
async def all_other_messages(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        await message.reply("You enter in 'test_state1'")
        await OrderStates.next()
    else:
        await message.reply("WHAT IS IT?! I don't understand anything but a text.")


@dp.message_handler(content_types=types.ContentTypes.ANY, state=OrderStates.test_state2)
async def all_other_messages(message: types.Message, state: FSMContext):
    if message.content_type == 'text':
        await message.reply("You enter in 'test_states2' and finish state group.")
        await state.finish()
    else:
        await message.reply("WHAT IS IT?! I don't understand anything but a text.")


@dp.message_handler(content_types=types.ContentTypes.ANY, state='*')
async def all_other_messages(message: types.Message):
    if message.content_type == "text":
        await message.reply("I don't know what it means...")
    else:
        await message.reply("WHAT IS IT?! I don't understand anything but a text.")
