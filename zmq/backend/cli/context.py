from .constants import IO_THREADS
import ZeroMQ

class Context(ZeroMQ.ZContext):
    _closed = None

    def __init__(self, io_threads=1, shadow=None):
        self.ThreadPoolSize = io_threads
        if shadow:
            raise NotImplementedError()
        self._closed = False

    @property
    def closed(self):
        return self._closed
