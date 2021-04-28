#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: 2021 Stefan Gehn <stefan+cmk@srcbox.net>
#
# SPDX-License-Identifier: GPL-2.0-only

from cmk.gui.valuespec import Dictionary, TextAscii
from cmk.gui.plugins.wato import notification_parameter_registry, NotificationParameter


@notification_parameter_registry.register
class NotificationParameterTelegram(NotificationParameter):
    @property
    def ident(self):
        return "telegram"

    @property
    def spec(self):
        return Dictionary(
            title=_("Create notification with the following parameters"),
            required_keys=["bot_token", "chat_id"],
            elements=[
                (
                    "bot_token",
                    TextAscii(
                        title=_("Bot Token"),
                        help=_("Telegram Bot Token for sending notifications"),
                        size=46,
                        allow_empty=False,
                    ),
                ),
                (
                    "chat_id",
                    TextAscii(
                        title=_("Chat ID"),
                        help=_("Telegram Chat ID to send notifications to"),
                        size=24,
                        allow_empty=False,
                    ),
                ),
                (
                    "url_prefix",
                    TextAscii(
                        title=_("URL prefix for links to Checkmk"),
                        help=_(
                            "If you specify an URL prefix here, then notifications are "
                            "armed with hyperlinks to your Check_MK GUI, so the "
                            "recipient of the message can directly visit the host or "
                            "service in question in Check_MK. Specify an absolute URL "
                            "including the <tt>.../check_mk/</tt>"
                        ),
                        regex="^(http|https)://.*/check_mk/$",
                        regex_error=_(
                            "The URL must begin with <tt>http</tt> or "
                            "<tt>https</tt> and end with <tt>/check_mk/</tt>."
                        ),
                        size=64,
                        allow_empty=True,
                    )
                ),
            ],
        )
