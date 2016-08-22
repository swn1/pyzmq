import ZeroMQ
class Context(ZeroMQ.ZContext):
    def __new__(cls, *args):
        return ZeroMQ.ZContext()