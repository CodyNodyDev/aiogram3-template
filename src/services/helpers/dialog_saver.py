import random

from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.utils.config import DIALOGS_URL


async def save(state: FSMContext):
    dialog_messages_dict = await state.get_data()
    output_message = ''
    dialog_messages_map = map(str, dialog_messages_dict.keys())
    id_for_filename = [i for i in dialog_messages_map][0]

    for key in dialog_messages_dict:
        output_message += f'{key}\n{dialog_messages_dict[key]}\n\n'
    text_file = open(f"{DIALOGS_URL}dialog_{id_for_filename}.txt", "w")
    text_file.write(output_message)
    text_file.close()

    await state.clear()


async def create_template_for_data(message: Message):
    user_user_id = int(message.reply_to_message.text.split('ID:')[1])
    user_datetime = str(message.reply_to_message.date).split()[0] + str(message.reply_to_message.date)[-1]
    user_text = message.reply_to_message.text.split()[0]
    user_msg_id = message.reply_to_message.message_id

    bot_id = message.from_user.id
    bot_datetime = message.date
    bot_text = message.text
    bot_msg_id = message.message_id

    rand_index = random.randint(100, 999)

    user_key = f'{user_user_id}_{user_msg_id}_{rand_index}'
    user_data = f'[{user_datetime}]-USER: {user_text}'

    admin_key = f'{bot_id}_{bot_msg_id}_{rand_index}'
    admin_data = f'[{bot_datetime}]-ADMIN: {bot_text}'

    return [user_key, user_data, admin_key, admin_data, user_user_id]
