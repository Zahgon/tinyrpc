#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import urllib.parse as urlparse
from typing import Any, Tuple

from . import ServerTransport


class CGIServerTransport(ServerTransport):
    """CGI transport.

    The CGIServerTransport adds CGI as a supported server protocol.
    It can be used with the regular HTTP client.

    Reading stdin is blocking but, given that we've been called, something is
    waiting.  The transport accepts only POST requests.

    A POST request provides the entire JSON-RPC request in the body of the HTTP
    request.
    """
    def receive_message(self) -> Tuple[Any, bytes]:
        """Receive a message from the transport.

        Blocks until a message has been received. May return a context
        opaque to clients that should be passed to :py:func:`send_reply`
        to identify the client later on.

        :return: A tuple consisting of ``(context, message)``.
        """
        pass

    def send_reply(self, context: Any, reply: bytes) -> None:
        """Sends a reply to a client.

        The client is usually identified by passing ``context`` as returned
        from the original :py:func:`receive_message` call.

        Messages must be bytes, it is up to the sender to convert the message
        beforehand. A non-bytes value raises a :py:exc:`TypeError`.

        :param any context: A context returned by :py:func:`receive_message`.
        :param bytes reply: A binary to send back as the reply.
        """
        pass
