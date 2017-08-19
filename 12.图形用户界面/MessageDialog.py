# -*- coding: utf-8 -*-
#消息弹出框
import wx
def OnAlter(msg='Save Sucess!!'):
    dlg = wx.MessageDialog(None, msg,
                           'A Message Box',
                           wx.OK | wx.ICON_INFORMATION
                           # wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
    dlg.ShowModal()
    dlg.Destroy()