#!/usr/bin/python3
from ctypes import *
class DriverCallbacks(Structure):
    _fields_ = [
        ("drvcomm_Open",     c_void_p),
        ("drvcomm_Close",    c_void_p),
        ("drvcomm_Transfer", c_void_p)
    ]

class InitDataEntry(Structure):
    _fields_ = [
        ("iface",   64 * c_byte),
        ("handle",  c_void_p)
    ]

class InitDataContainer(Structure):
    _fields_ = [
        ("size",    c_uint),
        ("id",      c_uint),
        ("data",    POINTER(InitDataEntry))
    ]


lib = cdll.LoadLibrary("./sum.so")

driverFuncList = DriverCallbacks()
driverFuncList.drvcomm_Open = cast(lib.ftdi_open, c_void_p)
driverFuncList.drvcomm_Close = cast(lib.ftdi_close, c_void_p)
driverFuncList.drvcomm_Transfer = cast(lib.ftdi_transfer, c_void_p)


libc = cdll.LoadLibrary("libc.so.6")

initData = InitDataEntry()
libc.strcpy(byref(initData.iface), c_char_p("DriverCallbacks".encode('utf-8')))
initData.handle = cast(pointer(driverFuncList), c_void_p)

initDataCont = InitDataContainer()
initDataCont.size = c_uint(3)
initDataCont.id = c_uint(9)
initDataCont.data = pointer(initData)



ret = lib.dev_Create(byref(initDataCont))
