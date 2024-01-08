from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.keyboard_config import (
    DEFAULT_DATA,
    NAME, CALLBACK,
    COLUMN, SHOP_CARDS,
    JUST_BACK, CUSTOM
)

""" 
Customize Keyboard Builder 
Inherited from Aiogram Keyboard builder
"""


class KBuilder(InlineKeyboardBuilder):
    def __init__(self, kb_data: dict) -> None:
        """
        To create a keyboard, you need an object that contains 3 fields:

        :param kb_data:
                    buttons_count:  The number of buttons
                    key_board_view: The view
                    buttons_data:   List of the data {button name and their callbacks}
        """

        super().__init__()

        buttons_count = kb_data['btns_count']
        keyboard_view = kb_data['keyboard_view']
        buttons_data = kb_data['buttons_data']

        self._buttons_count = buttons_count if buttons_count > 0 else 1
        self._keyboard_view = keyboard_view
        self._buttons_data = buttons_data

    async def build_keyboard(self) -> InlineKeyboardMarkup:
        """
        :return: a ready-to-use keyboard
        """

        await self.__set_view()
        return self.as_markup()

    async def __reset_data(self) -> None:
        """
        If a non-existent keyboard type is passed,
        the data is reset to the default keyboard
        """

        self._buttons_count = 1
        self._keyboard_view = COLUMN
        self._buttons_data = [DEFAULT_DATA]

    async def __add_buttons(self) -> None:
        for i in range(self._buttons_count):
            self.button(
                text=self._buttons_data[i][NAME],
                callback_data=self._buttons_data[i][CALLBACK]
            )

    async def __set_view(self) -> bool:
        """
        Type of keyboard's view: 'column', 'shop_cards', 'custom'

        To create a custom keyboard you need to add methods to
        the class. Use the documentation to help you create it:

        https://docs.aiogram.dev/en/dev-3.x/utils/keyboard.html
        """

        if self._keyboard_view == COLUMN or self._keyboard_view == JUST_BACK:
            await self.__add_buttons()
            self.adjust(1)
            return True

        elif self._keyboard_view == SHOP_CARDS:
            await self.__add_buttons()
            self.adjust(3, 1)
            return True

        elif self._keyboard_view == CUSTOM:
            pass

        await self.__reset_data()
        await self.__add_buttons()

        return False


