
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

zmq_version_info = ZeroMQ.lib.zmq.version
from ZeroMQ.backend import *

Message = Frame
Stopwatch = None
device = None
proxy = None
strerror = None
zmq_errno = None
has = None
curve_keypair = None
IPC_PATH_MAX_LEN = 0

from . import constants

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


