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
from tpc_error import client_error_message
from tpc_helpers import TPC_Helpers



###########################################################################
## Class hola_login
###########################################################################

class hola_login(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"hola", pos=wx.DefaultPosition, size=wx.Size(350, 200),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.username_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer9 = wx.GridSizer(0, 2, 0, 0)

        self.username_label = wx.StaticText(self.username_panel, wx.ID_ANY, u"username", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.username_label.Wrap(-1)
        gSizer9.Add(self.username_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.username_input = wx.TextCtrl(self.username_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(150, -1), 0)
        gSizer9.Add(self.username_input, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.username_panel.SetSizer(gSizer9)
        self.username_panel.Layout()
        gSizer9.Fit(self.username_panel)
        bSizer2.Add(self.username_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.password_label = wx.StaticText(self.m_panel4, wx.ID_ANY, u"password", wx.DefaultPosition, wx.DefaultSize,
                                            0)
        self.password_label.Wrap(-1)
        gSizer3.Add(self.password_label, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.password_input = wx.TextCtrl(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.Size(150, -1), wx.TE_PASSWORD)
        gSizer3.Add(self.password_input, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_panel4.SetSizer(gSizer3)
        self.m_panel4.Layout()
        gSizer3.Fit(self.m_panel4)
        bSizer2.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.login_btn = wx.Button(self.m_panel6, wx.ID_ANY, u"login", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.login_btn, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.error_cue = wx.StaticText(self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.error_cue.Wrap(-1)
        bSizer5.Add(self.error_cue, 0, wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer5)
        self.m_panel6.Layout()
        bSizer5.Fit(self.m_panel6)
        bSizer2.Add(self.m_panel6, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.setBgColor)
        self.login_btn.Bind(wx.EVT_BUTTON, self.request_login)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def request_login(self, event):
        username = self.username_input.GetValue()
        password = self.password_input.GetValue()
        r = TPC_Client_Request()
        res = r.request_login(username, password)
        if int(res['errcode']) is 100:
            from hola_gui import app
            app.uuid = res['uuid']
            app.username = res['username']
            res = r.request_userlist(res['uuid'])
            frres = TPC_Helpers.tpc_parse_helper(res)
            for fr in frres['list']:
                app.fl_frame.friendlist.InsertItem(app.fl_frame.friendlist.GetItemCount(), str(fr))
            app.fl_frame.Show(True)
            app.login_frame.Hide()

        else:
            self.error_cue.SetLabel(client_error_message(res['errcode']))

    def setBgColor(self, event):
        event.Skip()

