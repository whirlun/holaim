# -*- coding:utf-8 -*-

from tcp_base_client import process_normal_message
from tpc_client_message import TPC_Client_Message
from tpc_analyser import parser
from tpc_helpers import TPC_Helpers

class TPC_Client_Request:
    def request_login(self, username, password):
        m = TPC_Client_Message.request_login(username, password)
        raw_res = process_normal_message(m)
        res = parser.parse(raw_res)
        res = TPC_Helpers.tpc_parse_helper(res)
        return res

    def request_logout(self, uuid):
        m = TPC_Client_Message.request_logout(uuid)
        raw_res = process_normal_message(m)
        res = parser.parse(raw_res)
        return res

    def request_userlist(self, uuid):
        m = TPC_Client_Message.request_userlist(uuid)
        raw_res = process_normal_message(m)
        res = parser.parse(raw_res)
        return res

    def request_unichat(self, uuid, srcuser, dstuser, msglen, msgbody):
        m = TPC_Client_Message.request_unichat(srcuser, dstuser, msglen, msgbody, uuid)
        print m
        raw_res = process_normal_message(m)
        res = parser.parse(raw_res)
        return res

    def request_register(self, username, password):
        m = TPC_Client_Message.request_register(username, password)
        raw_res = process_normal_message(m)
        res = parser.parse(raw_res)
        return res


#c = TPC_Client_Request()
#m = c.request_login("bbrabbit2", "12ws34rf")
#m = c.request_logout("b7b96ba6-f87f-11e7-b1d3-6a0002256a80")
#print m