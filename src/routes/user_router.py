import traceback
from typing import Any, Dict

from aiogram import Router, types, F
from aiogram.filters import StateFilter
from keyboards.inline.constructor import KBuilder
from utils.constants import (
    MSG, PORTFOLIO_KB,
    PROJECT_KB, MAIN_KB
)
from utils import SendExceptionService

""" Router messages from users """

router = Router()


@router.callback_query(F.data == "go_to_portfolio", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]):
    """
    Pressed the first button

    :param data:
    :param call: Edit user text and inline keyboard
    """

    try:
        await call.message.edit_text(
            MSG['PORTFOLIO_MENU']
        )
        await call.message.edit_reply_markup(
            inline_message_id=str(call.message.message_id),
            reply_markup=await KBuilder(PORTFOLIO_KB).build_keyboard()
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "go_to_write_next_proj", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]):
    """
    Flip the cards forward

    :param data:
    :param call: Edit user text and inline keyboard
    """

    try:
        # TODO: спрятать текст сообщения в константы

        await call.message.edit_text(
            'Сюда идёт динамическая подгрузка проектов ▶️ ДАЛЕЕ'
        )
        await call.message.edit_reply_markup(
            inline_message_id=str(call.message.message_id),
            reply_markup=await KBuilder(PORTFOLIO_KB).build_keyboard()
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "go_to_prev_proj", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]):
    """
    Flip the cards backward

    :param data:
    :param call: Edit user text and inline keyboard
    """

    try:
        await call.message.edit_text(
            'НАЗАД ◀️ Сюда идёт динамическая подгрузка проектов'
        )
        await call.message.edit_reply_markup(
            inline_message_id=str(call.message.message_id),
            reply_markup=await KBuilder(PORTFOLIO_KB).build_keyboard()
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "go_to_inside_proj", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]):
    """
    Open a card

    :param data:
    :param call: Edit user text and inline keyboard
    """

    try:
        # TODO: спрятать текст сообщения в константы
        # TODO: сделать динамичесуб подгрузку проектов

        await call.message.edit_text(
            'Здесь открывается проект. Идёт его описание.'
        )
        await call.message.edit_reply_markup(
            inline_message_id=str(call.message.message_id),
            reply_markup=await KBuilder(PROJECT_KB).build_keyboard()
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "go_to_main_menu", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]):
    """
    Back button to return to the main menu

    :param call: Edit user text and inline keyboard
    """

    try:
        await call.message.edit_text(MSG['MAIN_MENU'])
        await call.message.edit_reply_markup(
            inline_message_id=str(call.message.message_id),
            reply_markup=await KBuilder(MAIN_KB).build_keyboard()
        )

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "go_to_education", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]):
    """
    Go to education menu

    :param data:
    :param call: Edit user text
    """

    try:
        await call.message.edit_text(MSG['EDUCATION_MENU'])

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())


@router.callback_query(F.data == "go_to_write_feedback", StateFilter(None))
async def on_backer(call: types.CallbackQuery, data: Dict[str, Any]) -> None:
    """
    Got to ~ write feedback ~ menu

    :param data:
    :param call: Edit user text
    """

    try:
        await call.message.edit_text(MSG['LEAVE_FEEDBACK'])

    except Exception as e:
        exception_service: SendExceptionService = data.get("exception_service")
        await exception_service.send_ex(value=e.__str__(), traceback=traceback.format_exc())
