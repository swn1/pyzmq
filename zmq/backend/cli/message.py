"""Dummy Frame object"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

import zmq
from zmq.utils.strtypes import unicode
from ZeroMQ import ZFrame

import platform
if platform.python_implementation() == 'IronPython':
    view = lambda x: bytes(memoryview(x)).ToByteArray()
else:
    try:
        view = memoryview
    except NameError:
        view = buffer

_content = lambda x: x.tobytes() if type(x) == memoryview else x

class Frame(ZFrame):
    #_data = None
    tracker = None
    closed = False
    more = False
    #buffer = None


    def __init__(self, data, track=False):
        #try:
        #    view(data)
        #except TypeError:
        #    raise

        super(Frame, self).__init__(view(data))
        #self._data = data

        #if isinstance(data, unicode):
        #    raise TypeError("Unicode objects not allowed. Only: str/bytes, " +
        #                    "buffer interfaces.")

        self.more = False
        self.tracker = None
        self.closed = False
        if track:
            self.tracker = zmq.MessageTracker()

        #self.buffer = view(self.bytes)

    @property
    def bytes(self):
        data = _content(self._data)
        return data

    def __len__(self):
        return len(self.bytes)

    def __eq__(self, other):
        return self.bytes == _content(other)

    def __str__(self):
        if str is unicode:
            return self.bytes.decode()
        else:
            return self.bytes

    @property
    def done(self):
        return True

Message = Frame

__all__ = ['Frame', 'Message']
