"""
sentry.logging.formatters
~~~~~~~~~~~~~~~~~~~~~~~~~
:copyright: (c) 2010-2016 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from __future__ import absolute_import

import traceback

from logging import Formatter

import msgpack


class MessagePackFormatter(Formatter):
    """
    Return a packed dictionary.

    Will pack the dictionary or the String representation of the message.
    """
    def format(self, record):
        pack = record.msg if isinstance(record.msg, dict) else {'msg': str(record.msg)}
        pack['levelname'] = record.levelname
        if record.exc_info:
            pack['traceback'] = traceback.format_tb(record.exc_info[-1])

        return msgpack.packb(pack)
