import ZeroMQ

def strerror(errno):
    return ZeroMQ.ZError.FromErrno(errno).Text

def zmq_errno():
    return ZeroMQ.ZError.GetLastErr().Number

__all__ = ['strerror', 'zmq_errno']
