import ZeroMQ
class Context(ZeroMQ.ZContext):
    def __new__(cls, *args):
        if args:
            raise NotImplementedError("too many arguments")
        return ZeroMQ.ZContext()