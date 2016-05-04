# coding: utf-8
"""zmq poll function"""

import clr
import ZeroMQ
from ZeroMQ import ZSocket, ZPollItem, ZPoll
clr.ImportExtensions(ZeroMQ.ZPollItems)
from System import Enum, TimeSpan

# Copyright (C) PyZMQ Developers
# Distributed under the terms of the Modified BSD License.

def _zpollitem(flag):
    if isinstance(flag, int):
        flag = Enum.Parse(ZPoll, str(flag))
    if flag == ZPoll.In:
        return ZPollItem.CreateReceiver()
    if flag == ZPoll.Out:
        return ZPollItem.CreateSender()
    if flag == ZPoll.In|ZPoll.Out:
        return ZPollItem.CreateReceiverSender()

#def _make_zmq_pollitem(socket, flags):
#    zmq_socket = socket._zmq_socket
#    zmq_pollitem = ffi.new('zmq_pollitem_t*')
#    zmq_pollitem.socket = zmq_socket
#    zmq_pollitem.fd = 0
#    zmq_pollitem.events = flags
#    zmq_pollitem.revents = 0
#    return zmq_pollitem[0]

#def _make_zmq_pollitem_fromfd(socket_fd, flags):
#    zmq_pollitem = ffi.new('zmq_pollitem_t*')
#    zmq_pollitem.socket = ffi.NULL
#    zmq_pollitem.fd = socket_fd
#    zmq_pollitem.events = flags
#    zmq_pollitem.revents = 0
#    return zmq_pollitem[0]

def zmq_poll(sockets, timeout):
    socks = []
    events = []
    allflags = 0
    for s,f in sockets:
        socks.append(s)
        events.append(_zpollitem(f))
        allflags |= int(f)

    socks.Poll(events, Enum.Parse(ZPoll, str(allflags)), TimeSpan.FromMilliseconds(timeout))
    
    #cffi_pollitem_list = []
    #low_level_to_socket_obj = {}
    #for item in sockets:
    #    if isinstance(item[0], int):
    #        low_level_to_socket_obj[item[0]] = item
    #        cffi_pollitem_list.append(_make_zmq_pollitem_fromfd(item[0], item[1]))
    #    else:
    #        low_level_to_socket_obj[item[0]._zmq_socket] = item
    #        cffi_pollitem_list.append(_make_zmq_pollitem(item[0], item[1]))
    #items = ffi.new('zmq_pollitem_t[]', cffi_pollitem_list)
    #list_length = ffi.cast('int', len(cffi_pollitem_list))
    #c_timeout = ffi.cast('long', timeout)
    #_retry_sys_call(C.zmq_poll, items, list_length, c_timeout)
    #result = []
    #for index in range(len(items)):
    #    if not items[index].socket == ffi.NULL:
    #        if items[index].revents > 0:
    #            result.append((low_level_to_socket_obj[items[index].socket][0],
    #                        items[index].revents))
    #    else:
    #        result.append((items[index].fd, items[index].revents))
    #return result

__all__ = ['zmq_poll']
