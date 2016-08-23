import ZeroMQ
class Frame(ZeroMQ.ZFrame):
    def __new__(cls, *args):
        if args:
            raise NotImplementedError("too many arguments")
        return ZeroMQ.ZFrame()