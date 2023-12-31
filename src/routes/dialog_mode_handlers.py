from aiogram import Router, types, F, Bot

from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.keyboards.inline.constructor import KBuilder
from src.filters.AdminFilter import AdminFilter
from src.states import ConnectToAdmin
from src.utils.constants import MSG, MAIN_KB, END_DIALOG_MODE_KB
from src.utils.config import ADMINS_ID


""" All text handlers and callback for dialog-mode """

router = Router()


@router.callback_query(F.data == "go_to_write_private", StateFilter(None))
async def start_dialog_mode_handler(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    """
    Enabling user and admin dialog mode

    Bot notifies the administrator of a user's message
    """

    await state.set_state(ConnectToAdmin.started)
    await state.set_data({'userid': call.message.from_user.id})

    await call.message.edit_text(MSG['WRITE_TO_PRIVATE_MSG'])
    await call.message.edit_reply_markup(
                                    reply_markup=await KBuilder(END_DIALOG_MODE_KB).build_keyboard()
    )

    user_id = call.from_user.id
    user_name = call.from_user.username

    await bot.send_message(
                        chat_id=ADMINS_ID[0],
                        text=f'User {user_id}\n@{user_name}\n\nhas started dialog-mode'
    )


# TODO: спрятать текст сообщения вышел -> 39 строка и 64
# TODO: Доставать админов из диспетчера

@router.callback_query(F.data == "finish_to_write_private", StateFilter(ConnectToAdmin))
async def end_dialog_mode_handler(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    """
    Disabling user and admin dialog-mode
    """

    await state.clear()

    await call.message.answer('Режим диалога завершен')
    await call.message.edit_reply_markup(
                            inline_message_id=str(call.message.message_id),
                            reply_markup=None
    )
    await call.message.answer(
                            MSG['MAIN_MENU'],
                            reply_markup=await KBuilder(MAIN_KB).build_keyboard()
    )
    await bot.send_message(
                        chat_id=ADMINS_ID[0],
                        text=f'User ID:{call.message.from_user.id}\n\nhas closed dialog-mode'
    )


@router.message(StateFilter(ConnectToAdmin))
async def dialog_user_handler(message: Message, bot: Bot):
    """
    Text handler for users
        Sending message from user to admin
    """

    text_message = f'{message.text}\n\n от ID: {message.from_user.id}'

    await bot.send_message(ADMINS_ID[0], text_message)


@router.message(AdminFilter())
async def dialog_admin_handler(message: Message,  bot: Bot):
    """
    Handler for admin
        Can only respond with a reply

    Sending message from admin to user
    """

    send_to_user_id = int(message.reply_to_message.text.split('ID:')[1])
    print(f'send to {send_to_user_id}')

    # TODO: спрятать текст сообщения в константы
    # TODO: Изменить инструкцию пользователя к старту диалога

    message_for_user = f'Ответ:\n{message.text}\n\nЕсли вы ещё не завершили диалог, не нажимайте на кнопку, просто продолжите переписку'
    await bot.send_message(
                        chat_id=send_to_user_id,
                        text=message_for_user,
                        reply_markup=await KBuilder(END_DIALOG_MODE_KB).build_keyboard()
    )
