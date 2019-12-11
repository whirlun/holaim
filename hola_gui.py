import wx

import hola_login
import hola_friendlist
import hola_chat


class holaGUI(wx.App):

    def OnInit(self):
        self.login_frame = hola_login.hola_login(parent=None)
        self.fl_frame = hola_friendlist.hola_friendlist(None)
        self.login_frame.Show(True)
        return True


app = holaGUI()
