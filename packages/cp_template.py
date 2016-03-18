import win32com
import win32com.client
import pythoncom
import threading
import time

class CpClass:
    cnt = 0

    @classmethod
    def Bind(self, usr_obj):
        handler = type('CpClass_%s'% CpClass.cnt, (CpClass,), {})
        handler.idx = CpClass.cnt
        handler.com_obj = win32com.client.Dispatch(usr_obj.com_str)
        handler.usr_obj = usr_obj
        win32com.client.WithEvents(handler.com_obj, handler)
        CpClass.cnt = CpClass.cnt + 1
        return handler

    @classmethod
    def Request(self):
        self.usr_obj.request(self.com_obj)

    def OnReceived(self):
        self.usr_obj.response(self.com_obj)

