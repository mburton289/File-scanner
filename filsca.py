import os
import wx


class Welcome(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'File Scanner', size=(400, 240))
        panel = wx.Panel(self)
        self.dlg = wx.TextCtrl(panel, -1, pos=(100, 20), size=(100, 20))
        self.dlf = wx.TextCtrl(panel, -1, pos=(100, 120), size=(100, 20))
        wx.StaticText(panel, -1, "Path:", pos=(100, 0), size=(40, 20))
        wx.StaticText(panel, -1, "size(bytes):", pos=(100, 100), size=(80, 20))
        self.scanButt = wx.Button(panel, -1, "scan path", (0, 0), (100, 100))
        self.scanButt.Bind(wx.EVT_BUTTON, self.enter, self.scanButt)
        self.numButt = wx.Button(panel, -1, "Size", (0, 100), (100, 100))
        self.numButt.Bind(wx.EVT_BUTTON, self.numval, self.numButt)

    def numval(self, event):
        porl = self.dlf.GetValue()
        self.xv = int(porl)

    def enter(self, event):

        popl = self.dlg.GetValue()
        walkit = os.walk(popl)

        for dirp, dirn, filename in walkit:
            for i in filename:
                filePath = os.path.join(dirp, i)
                progSize = os.path.getsize(filePath)
                try:
                    if progSize > self.xv:
                        print(filePath, progSize*1e-9)
                except:
                    if progSize > 1000000000:
                        print(filePath, progSize*1e-9)

if __name__ == '__main__':
    app = wx.App(False)
    frame = Welcome(parent=None, id=-1)
    frame.Show()
    app.MainLoop()