from aiogram import Router, types, F, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from filters.AdminFilter import AdminFilter
from keyboards.inline.constructor import KBuilder
from services.helpers import dialog_saver
from states import ConnectToAdmin
from utils.config import ADMINS_ID
from utils.constants import MSG, MAIN_KB, END_DIALOG_MODE_KB, END_DIALOG_MODE_ADMINKB

""" All text handlers and callback for dialog-mode """

router = Router()


@router.callback_query(F.data == "go_to_write_private", StateFilter(None))
async def start_dialog_mode_handler(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    """
    Enabling user and admin dialog mode

    Bot notifies the administrator of a user's message
    """

    await state.set_state(ConnectToAdmin.started)
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


@router.callback_query(F.data == "finish_to_write_private", StateFilter(ConnectToAdmin))
async def end_dialog_mode_handler(call: types.CallbackQuery, state: FSMContext, bot: Bot):
    """
    Disabling user and admin dialog-mode
    """

    await state.clear()

    await call.message.answer(MSG['END_DIALOG_MODE'])
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
                        text=f'User ID:{call.message.from_user.id}\n\nhas closed dialog-mode',
                        reply_markup=await KBuilder(END_DIALOG_MODE_ADMINKB).build_keyboard()
    )


@router.message(StateFilter(ConnectToAdmin))
async def dialog_user_handler(message: Message, state: FSMContext, bot: Bot):
    """
    Text handler for users
        Sending message from user to admin
    """

    await state.set_data({f'{message.from_user.id}_{message.message_id}': message.text})
    text_message = f'{message.text}\n\n от ID: {message.from_user.id}'

    await bot.send_message(ADMINS_ID[0], text_message)


@router.message(AdminFilter())
async def dialog_admin_handler(message: Message, state: FSMContext, bot: Bot):
    """
    Handler for admin
        Can only respond with a reply

    Sending message from admin to user
    """

    user_key, user_data, admin_key, admin_data, \
        user_user_id = dialog_saver.create_template_for_data(message)

    await state.update_data({user_key: user_data})
    await state.update_data({admin_key: admin_data})

    message_for_user = MSG['USER_TIP_FOR_DIALOG'].format(message.text)
    await bot.send_message(
                        chat_id=user_user_id,
                        text=message_for_user,
                        reply_markup=await KBuilder(END_DIALOG_MODE_KB).build_keyboard()
    )


@router.callback_query(F.data == "save_private_dialog", AdminFilter())
async def end_dialog_mode_handler(call: types.CallbackQuery, state: FSMContext):
    """
    Saving dialog story
    """

    await dialog_saver.save(state=state)

    await call.message.edit_reply_markup(None)

