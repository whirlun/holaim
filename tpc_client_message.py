# -*- coding:utf-8 -*-

from tpc_helpers import TPC_Helpers
from tpc_analyser import parser
from tpc_lexer import lexer

class TPC_Client_Message:
    helper = TPC_Helpers()

    @staticmethod
    def request_login(username,password):
        "client sends login request"
        m = TPC_Client_Message.helper.tpc_message_parser("request",type="login",username=username,password=password)
        return m
    @staticmethod
    def request_logout(uuid):
        "client sends logout request"
        m = TPC_Client_Message.helper.tpc_message_parser("request", type="logout", uuid=uuid)
        return m
    @staticmethod
    def request_userlist(uuid):
        "client requests to get userlist"
        m = TPC_Client_Message.helper.tpc_message_parser("request", type="list", uuid=uuid)
        return m
    @staticmethod
    def request_unichat(srcuser,dstuser,msglen,msgbody, uuid):
        "client requests to talk to an exact user"
        m = TPC_Client_Message.helper.tpc_message_parser( "request", type="unichat", uuid=uuid, srcuser=srcuser,dstuser=dstuser,msglen=msglen, msgbody=msgbody)
        return m

    @staticmethod
    def request_register(username, password):
        "client requests to create new account"
        m  =TPC_Client_Message.helper.tpc_message_parser("request", type="register", username=username, password=password)
        return m
#m = TPC_Client_Message.request_unichat("00000000-00000-0000000-0000000000000", "bbrabbit", "admin","20", "12345678901234567890")
#print m
#lexer.input(m)

#while True:
#    tok = lexer.token()
#    if not tok: break      # No more input
#    print tok
#res = parser.parse(m)

#print res
