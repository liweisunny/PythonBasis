# -*- coding: utf-8 -*-
import wx
import os
# 打开开文件对话框
#参数说明：filename文本框控件，用于接受路径,file_wildcard打开的文件格式
def OnOpen(filename,file_wildcard='Paint files(*.txt)|*.txt|All files(*.*)|*.*'):
    dlg = wx.FileDialog(None, "Open txt file...",
                        os.getcwd(),
                        style=wx.OPEN,
                        wildcard=file_wildcard)
    if dlg.ShowModal() == wx.ID_OK:
        filename.Value = dlg.GetPath()
    dlg.Destroy()