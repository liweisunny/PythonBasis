# -*- coding: utf-8 -*-
import wx
import MessageDialog
class Calculator(wx.Frame):
    #初始化窗体
    def __init__(self):
        self.equation = ""  # 记录表达式
        #初始化窗体属性
        wx.Frame.__init__(self,None,title=U'计算器',size=(270,400))
        #设置背景组件
        panel=wx.Panel(self)
        #垂直布局器
        vboxsizer=wx.BoxSizer(wx.VERTICAL)
        #
        gridsizer=wx.GridSizer(rows=5, cols=4, hgap=5, vgap=5)
        #文本框
        self.text_expression=wx.TextCtrl(panel,style=wx.TE_MULTILINE)
        #设置按钮
        strbtn='CE,C,Del,/,7,8,9,*,4,5,6,-,1,2,3,+,+_,0,.,='.split(',')
        #创建水平布局器
        for str in strbtn:
           btnItem=wx.Button(panel,label=str,size=(60,50))

           self.createHandler(btnItem, str)
           gridsizer.Add(btnItem, 0, 0)
        vboxsizer.Add(self.text_expression,proportion=0,flag=wx.EXPAND)
        vboxsizer.Add(gridsizer,proportion=0,flag=wx.EXPAND)
        panel.SetSizer(vboxsizer)
    # 事件处理
    def createHandler(self, btn, lable):
        if lable == 'CE' or lable == 'C':
            self.Bind(wx.EVT_BUTTON, self.onClear, btn)
        elif lable == 'Del':
            self.Bind(wx.EVT_BUTTON, self.onDel, btn)
        elif lable == '=':
            self.Bind(wx.EVT_BUTTON, self.onResult, btn)
        elif lable=='+_':
            self.Bind(wx.EVT_BUTTON,self.onAbs,btn)
        else:
            self.Bind(wx.EVT_BUTTON, self.onAppend, btn)

    def onClear(self, event):
        self.text_expression.Clear()
        self.equation=''

    def onDel(self, event):
        str = self.text_expression.GetValue()[:-1]
        self.text_expression.Value = str

    def onResult(self, event):
        try:
            result = eval(self.equation)
            self.text_expression.Value = str(result)
            self.equation= str(result)
        except:
            MessageDialog.OnAlter('expression error!!')
    def onAbs(self,event):
        try:
            self.text_expression.Value=str(0-int(self.text_expression.Value))
            self.equation =  self.text_expression.Value
        except:
            MessageDialog.OnAlter('not num!!')
    def onAppend(self, event):
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.text_expression.SetValue(self.equation)
if __name__=='__main__':
    app=wx.App()
    frame=Calculator()
    frame.Show()
    app.MainLoop()

