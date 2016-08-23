import ZeroMQ
class Message(ZeroMQ.ZMessage):
    def __new__(cls, *args):
        if args:
            raise NotImplementedError("too many arguments")
        return ZeroMQ.ZMessage()