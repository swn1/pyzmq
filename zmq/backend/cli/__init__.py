
import clr
clr.AddReference("ZeroMQ") # installed in build folder via NuGet.
import ZeroMQ
# make an object to force static class initializations
ZeroMQ.ZFrame()
#from IronPython.Runtime.Types import DynamicHelpers
#_libzmq = DynamicHelpers.GetPythonTypeFromType(ZeroMQ.lib.zmq)

zmq_version_info = ZeroMQ.lib.zmq.version
IPC_PATH_MAX_LEN = 0

from . import constants
from .context import Context
from .socket import Socket
from .frame import Frame
from .message import Message
from .stopwatch import Stopwatch
from .devices import device, proxy
from .poll import zmq_poll
from .error import strerror, zmq_errno

has = ZeroMQ.ZContext.Has

def curve_keypair():
    pk = None
    sk = None
    return ZeroMQ.Z85.CurveKeypair()

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


