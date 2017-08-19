# -*- coding: utf-8 -*-

#例：基本的GUI程序
'''
import wx
app=wx.App()#实例化基本应用程序类，负责幕后的所有初始化操作
#win=wx.Frame(None)#创建一个窗体，None表示不需要任何父部件

#在窗体上增加按钮，并设置窗体标题及按钮标签
win=wx.Frame(None,title='Simple Editor')#创建一个窗体，None表示不需要任何父部件
btn=wx.Button(win,label='Button')

win.Show()#显示窗体
app.MainLoop()#执行初始化操作
'''

#例 简单的文本编辑器
'''
import wx
app=wx.App()
frame=wx.Frame(None,title='Editor')
loadbtn=wx.Button(frame,label='Load',pos=(255,5),size=(80,25))
savebtn=wx.Button(frame,label='Save',pos=(315,5),size=(80,25))
filename=wx.TextCtrl(frame,pos=(5,5),size=(210,25))
contents=wx.TextCtrl(frame,pos=(5,35),size=(390,4000),style=wx.TE_MULTILINE|wx.HSCROLL)
frame.Show()
app.MainLoop()
'''
# 说明：上述代码设置了窗体上每个组件的位置和尺寸，pos（x,y）位置，size(k,g)是尺寸,但是上述布局的方式太过繁琐且不能适应窗体的大小变化。
import MessageDialog
import FileDialog
#事件处理
#打开文件按钮
def load(event):
    FileDialog.OnOpen(filename)
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()
#保存按钮
def save(event):
    file=open(filename.GetValue(),'w')
    str=contents.GetValue();
    if isinstance(str,unicode):
        str = str.encode('gb2312')
    else:
        str=str.decode('utf-8')
        str = str.encode('gb2312')
    file.write(str)
    file.close()
    MessageDialog.OnAlter()


#更智能的布局（尺寸器，wx.BoxSizer）
import wx
app=wx.App()
#创建窗体设置title和大小
frame=wx.Frame(None,title='Editor',size=(410,335))
#设置背景组件
bkg=wx.Panel(frame)
#创建窗体上的控件并设置其title，并给按钮绑定事件
loadbtn=wx.Button(bkg,label='Load')
loadbtn.Bind(wx.EVT_BUTTON,load)
savebtn=wx.Button(bkg,label='Save')
savebtn.Bind(wx.EVT_BUTTON,save)
filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)
#布局管理器—wx.BoxSizer()构造函数有一个决定是水平还是垂直的参数（wx.HORIZONTAL或者wx.VERTICAL），默认是水平
hbox=wx.BoxSizer()
#proportion参数根据在窗口改变大小时所分配的空间设置比例，如下：filename组件在窗体改变大小的时候获得了全部的额外空间，如果都设置为1就会获得相等的空间。
# 在这个布局管理器里只针对的是水平的，改变垂直是不会影响的
# wx.EXPAND用于确保组件会扩展到所分配的空间中
# wx.LEFT  wx.BOTTOM  wx.RIGHT  wx.ALL 决定边框参数应用于哪个边
# border参数用于设置边缘宽度
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(savebtn,proportion=0,flag=wx.LEFT,border=5)
#设置垂直的布局管理器
vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
#设置尺寸器
bkg.SetSizer(vbox)
#显示窗体
frame.Show()
app.MainLoop()






