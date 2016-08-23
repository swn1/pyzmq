import ZeroMQ
class Socket(ZeroMQ.ZSocket):
    def __new__(cls, *args):
        if args:
            raise NotImplementedError("too many arguments")
        return ZeroMQ.ZSocket()