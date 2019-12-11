# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 12 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from tpc_client import TPC_Client_Request

###########################################################################
## Class hola_chat
###########################################################################

class hola_chat(wx.Frame):

    def __init__(self, parent, dstuser):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel7.SetMaxSize(wx.Size(-1, 50))

        bSizer9.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

        self.dstusername = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dstusername.Wrap(-1)
        self.dstusername.SetLabel(dstuser)
        bSizer9.Add(self.dstusername, 0, wx.ALL, 5)

        self.hola_chatcontent = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.HSCROLL | wx.VSCROLL)
        self.hola_chatcontent.SetScrollRate(5, 5)
        self.hola_chatcontent.SetMinSize(wx.Size(-1, 300))
        self.hola_chatcontent.SetMaxSize(wx.Size(-1, 300))

        bSizer9.Add(self.hola_chatcontent, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel9 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_panel9.SetMinSize(wx.Size(-1, 100))
        self.m_panel9.SetMaxSize(wx.Size(-1, 100))

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.msgctrl = wx.TextCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.msgctrl.SetMinSize(wx.Size(400, 100))

        bSizer10.Add(self.msgctrl, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self.m_panel9, wx.ID_ANY, u"send", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetMinSize(wx.Size(-1, 100))

        bSizer10.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_panel9.SetSizer(bSizer10)
        self.m_panel9.Layout()
        bSizer10.Fit(self.m_panel9)
        bSizer9.Add(self.m_panel9, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer9)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.send_message)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def send_message(self, event):
        from hola_gui import app
        res = TPC_Client_Request.request_unichat(app.uuid, app.username, self.dstusername.GetLabel(),
                                           len(self.msgctrl.GetValue()), self.msgctrl.GetValue())


