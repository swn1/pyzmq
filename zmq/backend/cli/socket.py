import zmq
import ZeroMQ
import System

class Socket(ZeroMQ.ZSocket):
    _closed = None
    def __new__(cls, context=None, socket_type=None, shadow=None):
        if not context or not socket_type:
            raise ValueError()
        rv = ZeroMQ.ZSocket.__new__(cls, context, socket_type)
        if shadow:
            raise NotImplementedError()
        return rv

    @property
    def closed(self):
        return self._closed

    def close(self):
        self.Close()
        self._closed = True

    def set(self, opt, val):
        if isinstance(val, bytes):
            val = val.ToByteArray()
        self.SetOption(opt, val)

    def get(self, opt):
        if opt == ZeroMQ.ZSocketOption.RCVMORE:
            return self.ReceiveMore
        return self.GetOption(opt)

    @property
    def linger(self):
        return self.Linger.TotalMilliseconds

    @linger.setter
    def linger(self, value):
        self.Linger = System.TimeSpan.FromMilliseconds(value)

    # clrzmq4 exposes the underlying C byte array as a C# string or Byte[], string is easier to deal with.
    @property
    def identity(self):
        return bytes(self.IdentityString)
    @identity.setter
    def identity(self, value):
        self.IdentityString = str(value)

    def connect(self, address):
        self.Connect(address)

    def send(self, message, flags=0, copy=False, track=False):
        #if isinstance(message, unicode):
        #    raise TypeError("Message must be in bytes, not an unicode Object")

        if not isinstance(message, zmq.Frame):
            message = zmq.Frame(message)

        self.Send(message, System.Enum.Parse(ZeroMQ.ZSocketFlags, str(flags)))

        if track:
            raise NotImplementedError()
            # return zmq.MessageTracker()

    def recv(self, flags=0, copy=True, track=False):
        if track:
            raise NotImplementedError("recv track option")

        frame, err = self.ReceiveFrame(System.Enum.Parse(ZeroMQ.ZSocketFlags, str(flags)))

        if copy:
            return bytes(frame.Read())
        else:
            return zmq.Frame(frame)