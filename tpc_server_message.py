# -*- coding:utf-8 -*-

from tpc_helpers import TPC_Helpers

class TPC_Server_Message:
    helper = TPC_Helpers()

    @staticmethod
    def respond_login(username,password,uuid,errcode=100):
        "server responds login request"
        m = TPC_Server_Message.helper.tpc_message_parser("response",type="login", errcode=errcode,uuid=uuid,username=username)
        return m

    @staticmethod
    def  respond_logout(username,uuid,errcode=100):
        "server responds logout request"
        m = TPC_Server_Message.helper.tpc_message_parser("response", type="logout", errcode=errcode,uuid=uuid, username=username)
        return m

    @staticmethod
    def respond_register(username, password,uuid, errcode=100):
        "server responds register request"
        m = TPC_Server_Message.helper.tpc_message_parser("response", type="register", errcode=errcode, username=username)
        return m

    @staticmethod
    def respond_userlist(userlist, total, totalOnline, start, num,uuid,errcode=100):
        "server responds userlist request"
        m = TPC_Server_Message.helper.tpc_message_parser("response", type="list", errcode=errcode, uuid=uuid,total=total,totalOnline=totalOnline,
                                           start=start, num=num, userlist=userlist)
        return m

    @staticmethod
    def respond_userlist_unauthorized(uuid, errcode=203):
        "server responds userlist request when this action is not permitted"
        m = TPC_Server_Message.helper.tpc_message_parser("response", type="list",errcode=errcode, uuid=uuid)
        return m

    @staticmethod
    def respond_unichat(uuid,srcuser, dstuser, msglen, msgbody,errcode=100):
        "server responds unichat request"
        m = TPC_Server_Message.helper.tpc_message_parser("response",type="unichat", errcode=errcode,uuid=uuid)
        return m

    @staticmethod
    def respond_kickout(username,uuid,errcode=100):
        "server boardcasts kickout message"
        m = TPC_Server_Message.helper.tpc_message_parser("response", type="kickout", errcode=errcode, uuid=uuid, username=username)
        return m

    @staticmethod
    def respond_forbidchat(uuid, errcode=601):
        "server forbids client to send any message"
        m = TPC_Server_Message.helper.tpc_message_parser("response",type="forbidchat", errcode=errcode, uuid=uuid)
        return m

    @staticmethod
    def respond_resumechat(uuid, errcode=602):
        "server permits client to send message"
        m = TPC_Server_Message.helper.tpc_message_parser("response", type="resumechat", errcode=errcode, uuid=uuid)
        return m

    @staticmethod
    def respond_pollchat(uuid, msgbody, errcode=100):
        'server sends message to client'
        m = TPC_Server_Message.helper.tpc_parse_helper("response", type='pollchat', errcode = errcode, uuid = uuid, msgbody = msgbody)
        return m
