
import clr
import os
#zmqdll = os.path.join(os.path.dirname(__file__), "zeromq.dll")
assm=clr.LoadAssemblyFromFile("ZeroMQ.dll")
clr.AddReference(assm)
import ZeroMQ
# make an object to force static class initializations
ZeroMQ.ZFrame()
#from IronPython.Runtime.Types import DynamicHelpers
#_libzmq = DynamicHelpers.GetPythonTypeFromType(ZeroMQ.lib.zmq)

from ZeroMQ.lib.zmq import Version
def zmq_version_info():
    (Version.Major, Version.Minor, Version.Build)

Message = None
Stopwatch = None
device = None
proxy = None
zmq_poll = None
strerror = None
zmq_errno = None
has = None
curve_keypair = None
IPC_PATH_MAX_LEN = 0


from .context import Context

from . import constants

from .socket import Socket

from .message import Frame, Message

__all__ = [ # copy of public_api from zmq\backend\select.py
    'Context',
    'Socket',
    'Frame',
    'Message',
    'Stopwatch',
    'device',
    'proxy',
    'zmq_poll',
    'strerror',
    'zmq_errno',
    'has',
    'curve_keypair',
    'constants',
    'zmq_version_info',
    'IPC_PATH_MAX_LEN',
]


