import traceback
from typing import Dict, Any

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
from utils import SendExceptionService

""" All text handlers and callback for dialog-mode """

router = Router()


@router.callback_query(F.data == "go_to_write_private", StateFilter(None))
async def start_dialog_mode_handler(
        call: types.CallbackQuery,
        state: FSMContext,
        bot: Bot,
        data: Dict[str, Any]
) -> None:
    """
    Enabling user and admin dialog mode
    Bot notifies the administrator of a user's message

    :param data:
    :param call:  Edit user's message
    :param state: Set start to communication user with admin
    :param bot:   Send message to admin
    """

    try:
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

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "finish_to_write_private", StateFilter(ConnectToAdmin))
async def end_dialog_mode_handler(
        call: types.CallbackQuery,
        state: FSMContext,
        bot: Bot,
        data: Dict[str, Any]
) -> None:
    """
    Disabling user and admin dialog-mode

    :param data:
    :param call:  Send message to user, edit inline keyboard
    :param state: Clear state
    :param bot:   Send message to admin
    """

    try:
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

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.message(StateFilter(ConnectToAdmin))
async def dialog_user_handler(
        message: Message,
        state: FSMContext,
        bot: Bot,
        data: Dict[str, Any]
) -> None:
    """
    Text handler for users
    Sending message from user to admin

    :param data:
    :param message: Get user-info from message Object
    :param state:   Save data (user id, message id, message text) into FSMContext
    :param bot:     Send user's message to Admin
    """

    try:
        await state.set_data({f'{message.from_user.id}_{message.message_id}': message.text})
        text_message = f'{message.text}\n\n от ID: {message.from_user.id}'

        await bot.send_message(ADMINS_ID[0], text_message)

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.message(AdminFilter())
async def dialog_admin_handler(
        message: Message,
        state: FSMContext,
        bot: Bot,
        data: Dict[str, Any]
) -> None:
    """
    Handler for admin
        Can only respond with a reply
    Sending message from admin to user

    :param data:
    :param message: Get user-info from message Object
    :param state:   Append messages in FMSContext from user
    :param bot:     Send message to admin
    """

    try:
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

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "save_private_dialog", AdminFilter())
async def end_dialog_mode_handler(
        call: types.CallbackQuery,
        state: FSMContext,
        data: Dict[str, Any]
) -> None:
    """
    Saving dialog story

    :param data:
    :param call:  Edit user inline keyboard
    :param state: State Object for saving-helper
    """

    try:
        await dialog_saver.save(state=state)

        await call.message.edit_reply_markup(None)

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())
