import zmq
import ZeroMQ
import System

class Socket(ZeroMQ.ZSocket):
    def __new__(cls, context=None, socket_type=None, shadow=None):
        if not context or not socket_type:
            raise ValueError()
        rv = ZeroMQ.ZSocket.__new__(cls, context, socket_type)
        if shadow:
            raise NotImplementedError()
        return rv

    def set(self, opt, val):
        if isinstance(val, bytes):
            val = val.ToByteArray()
        self.SetOption(opt, val)

    def get(self, opt):
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

        #zmq_msg = ffi.new('zmq_msg_t*')
        #c_message = ffi.new('char[]', message)
        #rc = C.zmq_msg_init_size(zmq_msg, len(message))
        #_check_rc(rc)
        #C.memcpy(C.zmq_msg_data(zmq_msg), c_message, len(message))
        #_retry_sys_call(C.zmq_msg_send, zmq_msg, self._zmq_socket, flags)
        #rc2 = C.zmq_msg_close(zmq_msg)
        #_check_rc(rc2)

        if track:
            raise NotImplementedError()
            # return zmq.MessageTracker()

    #def recv(self, flags=0, copy=True, track=False):
    #    zmq_msg = ffi.new('zmq_msg_t*')
    #    C.zmq_msg_init(zmq_msg)
        
    #    try:
    #        _retry_sys_call(C.zmq_msg_recv, zmq_msg, self._zmq_socket, flags)
    #    except Exception:
    #        C.zmq_msg_close(zmq_msg)
    #        raise

    #    _buffer = ffi.buffer(C.zmq_msg_data(zmq_msg), C.zmq_msg_size(zmq_msg))
    #    value = _buffer[:]
    #    rc = C.zmq_msg_close(zmq_msg)
    #    _check_rc(rc)

    #    frame = Frame(value, track=track)
    #    frame.more = self.getsockopt(RCVMORE)

    #    if copy:
    #        return frame.bytes
    #    else:
    #        return frame