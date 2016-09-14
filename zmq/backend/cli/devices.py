# coding: utf-8
"""zmq device functions"""

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

def device(device_type, frontend, backend):
    raise NotImplementedError
    return proxy(frontend, backend)

def proxy(frontend, backend, capture=None):
    if isinstance(capture, Socket):
        capture = capture._zmq_socket
    else:
        capture = None
    raise NotImplementedError


__all__ = ['device', 'proxy']
