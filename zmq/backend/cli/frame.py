import ZeroMQ
class Frame(ZeroMQ.ZFrame):
    def __new__(cls, data, track=False):
        if track:
            raise NotImplementedError("frame tracking")
        if isinstance(data, bytes):
            data = data.ToByteArray()
        return ZeroMQ.ZFrame.__new__(cls, data)