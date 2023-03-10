from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ðá´á´ÉªÉ´",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ðá´á´Ê",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ðÊá´á´á´ÊÉªsá´",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ðÊá´á´á´á´á´sá´",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="ðÊá´É´",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ðÊÊÉªá´s",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ðÉªÉ´É¢",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="ðÊá´Ê",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="ðÊá´ÊÊÉªsá´",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ðÉªá´á´á´á´Êá´á´s",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="ðá´á´Êá´",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="ðá´á´á´",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="â Êá´Êá´© â",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
