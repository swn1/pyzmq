# coding: utf-8
"""zmq Context class"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

# adapted from cffi\context.py for cli backend.

#import weakref

#from .constants import EINVAL, IO_THREADS, LINGER

#from zmq.error import ZMQError, InterruptedSystemCall, _check_rc

from ZeroMQ import ZContext

class Context(object):
    _zmq_ctx = None
#    _iothreads = None
#    _closed = None
    _sockets = None
    _shadow = False

    def __init__(self, io_threads=1, shadow=None):
        
        if shadow:
            self._zmq_ctx = ffi.cast("void *", shadow)
            self._shadow = True
        else:
            self._shadow = False
            if not io_threads >= 0:
                raise ZMQError(EINVAL)
        
            self._zmq_ctx = ZContext()
        if not shadow:
            self._zmq_ctx.ThreadPoolSize = io_threads
        self._sockets = set()
    
#    @property
#    def underlying(self):
#        """The address of the underlying libzmq context"""
#        return int(ffi.cast('size_t', self._zmq_ctx))
    
    @property
    def closed(self):
        return not self._zmq_ctx

    def _add_socket(self, socket):
        #ref = weakref.ref(socket)
        self._sockets.add(socket)
        return socket

    def _rm_socket(self, ref):
        if ref in self._sockets:
            self._sockets.remove(ref)

#    def set(self, option, value):
#        """set a context option
        
#        see zmq_ctx_set
#        """
#        rc = C.zmq_ctx_set(self._zmq_ctx, option, value)
#        _check_rc(rc)

#    def get(self, option):
#        """get context option
        
#        see zmq_ctx_get
#        """
#        rc = C.zmq_ctx_get(self._zmq_ctx, option)
#        _check_rc(rc)
#        return rc

#    def term(self):
#        if self.closed:
#            return
        
#        rc = C.zmq_ctx_destroy(self._zmq_ctx)
#        try:
#            _check_rc(rc)
#        except InterruptedSystemCall:
#            # ignore interrupted term
#            # see PEP 475 notes about close & EINTR for why
#            pass

#        self._zmq_ctx = None
#        self._closed = True

#    def destroy(self, linger=None):
#        if self.closed:
#            return

#        sockets = self._sockets
#        self._sockets = set()
#        for s in sockets:
#            s = s()
#            if s and not s.closed:
#                if linger:
#                    s.setsockopt(LINGER, linger)
#                s.close()
        
#        self.term()

#__all__ = ['Context']
