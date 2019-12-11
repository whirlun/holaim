# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 12 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from hola_chat import hola_chat

###########################################################################
## Class hola_friendlist
###########################################################################

class hola_friendlist(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(200, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.personal_info_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 70), wx.TAB_TRAVERSAL)
        self.personal_info_panel.SetMaxSize(wx.Size(-1, 70))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.username = wx.StaticText(self.personal_info_panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.username.Wrap(-1)
        bSizer5.Add(self.username, 0, wx.ALL, 5)

        self.personal_info_panel.SetSizer(bSizer5)
        self.personal_info_panel.Layout()
        bSizer3.Add(self.personal_info_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 430), wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.friendlist = wx.ListCtrl(self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.Size(200, 430), wx.LC_ICON)
        bSizer7.Add(self.friendlist, 0, wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer7)
        self.m_panel6.Layout()
        bSizer3.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.friendlist.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onEnterChat)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def onEnterChat(self, event):
        chat_window = hola_chat(None, event.GetItem().GetText())
        chat_window.Show()
