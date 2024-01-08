from aiogram import Router, types, F
from aiogram.filters import StateFilter
from keyboards.inline.constructor import KBuilder
from utils.constants import (
    MSG, PORTFOLIO_KB,
    PROJECT_KB, MAIN_KB
)

""" Router messages from users """

router = Router()


@router.callback_query(F.data == "go_to_portfolio", StateFilter(None))
async def on_backer(call: types.CallbackQuery):
    """
    Pressed the first button
    """

    await call.message.edit_text(
        MSG['PORTFOLIO_MENU']
    )
    await call.message.edit_reply_markup(
        inline_message_id=str(call.message.message_id),
        reply_markup=await KBuilder(PORTFOLIO_KB).build_keyboard()
    )


@router.callback_query(F.data == "go_to_write_next_proj", StateFilter(None))
async def on_backer(call: types.CallbackQuery):
    """
    Flip the cards forward
    """

    # TODO: спрятать текст сообщения в константы

    await call.message.edit_text(
        'Сюда идёт динамическая подгрузка проектов ▶️ ДАЛЕЕ'
    )
    await call.message.edit_reply_markup(
        inline_message_id=str(call.message.message_id),
        reply_markup=await KBuilder(PORTFOLIO_KB).build_keyboard()
    )


@router.callback_query(F.data == "go_to_prev_proj", StateFilter(None))
async def on_backer(call: types.CallbackQuery):
    """
    Flip the cards backward
    """

    await call.message.edit_text(
        'НАЗАД ◀️ Сюда идёт динамическая подгрузка проектов'
    )
    await call.message.edit_reply_markup(
        inline_message_id=str(call.message.message_id),
        reply_markup=await KBuilder(PORTFOLIO_KB).build_keyboard()
    )


@router.callback_query(F.data == "go_to_inside_proj", StateFilter(None))
async def on_backer(call: types.CallbackQuery):
    """
    Open a card
    """

    # TODO: спрятать текст сообщения в константы
    # TODO: сделать динамичесуб подгрузку проектов

    await call.message.edit_text(
        'Здесь открывается проект. Идёт его описание.'
    )
    await call.message.edit_reply_markup(
        inline_message_id=str(call.message.message_id),
        reply_markup=await KBuilder(PROJECT_KB).build_keyboard()
    )


@router.callback_query(F.data == "go_to_main_menu", StateFilter(None))
async def on_backer(call: types.CallbackQuery):
    """
    Back button to return to the main menu
    """

    await call.message.edit_text(MSG['MAIN_MENU'])
    await call.message.edit_reply_markup(
        inline_message_id=str(call.message.message_id),
        reply_markup=await KBuilder(MAIN_KB).build_keyboard()
    )


@router.callback_query(F.data == "go_to_education", StateFilter(None))
async def on_backer(call: types.CallbackQuery):

    # TODO: задокументировать

    await call.message.edit_text(MSG['EDUCATION_MENU'])


@router.callback_query(F.data == "go_to_write_feedback", StateFilter(None))
async def on_backer(call: types.CallbackQuery):

    # TODO: задокументировать

    await call.message.edit_text(MSG['LEAVE_FEEDBACK'])
