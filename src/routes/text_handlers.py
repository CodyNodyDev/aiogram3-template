from aiogram import Router, types, F

from aiogram.filters import StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.keyboards.inline.constructor import KBuilder
from src.states import ConnectToAdmin
from src.utils.constants import MSG, MAIN_KB

""" All text handlers and callback for dialog-mode """

router = Router()


@router.callback_query(F.data == "go_to_write_private", StateFilter(None))
async def on_backer(call: types.CallbackQuery, state: FSMContext):
    """
    Enabling user and admin dialog mode
    """

    await state.set_state(ConnectToAdmin.started)
    await state.set_data({'userid': call.message.from_user.id})

    await call.message.edit_text(MSG['WRITE_TO_PRIVATE_MSG'])


# TODO: добавить кнопку завершения диалога к сообщениям при отправке

@router.callback_query(F.data == "finish_to_write_private", StateFilter(ConnectToAdmin))
async def on_backer(call: types.CallbackQuery, state: FSMContext):
    """
    Disabling user and admin dialog-mode
    """

    await state.clear()

    await call.message.answer('Режим диалога завершен')
    await call.message.answer(MSG['MAIN_MENU'])


@router.message(StateFilter(ConnectToAdmin))
async def dialog_handler(message: Message):
    """
    Text handler for users
    """

    #

    await message.answer(MSG['HELLO'].format(
        message.from_user.full_name,
        message.from_user.id,
        ),
        reply_markup=await KBuilder(MAIN_KB).build_keyboard()
    )


@router.message(StateFilter(ConnectToAdmin))
async def dialog_admin_handler(message: Message):
    """
    Handler for admin
        Can only respond with a reply
    """

    await message.answer('Прилшло сообщение от пользователя')