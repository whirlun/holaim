# -*- coding:utf-8 -*-
import re

class TPC_Helpers:
    def tpc_message_parser(self, *params, **format):
        '''this function takes a tunple includes stirngs that needs to replace
        and a dictionary to describe the format of the message'''
        strlist = []
        msgbody = None
        userlist = None
        if params:
            for p in params:
                strlist.append(p + "\r\n")
        for notation in format:
            if notation is "userlist":
                userlist = format['userlist']
                continue
            elif notation is "msgbody":
                msgbody = format['msgbody']
                continue
            strlist.append(notation + ":" + str(format[notation]) + "\r\n")

        strlist.append("\r\n")
        if msgbody:
            strlist.append(msgbody)
            strlist.append("\r\n")
        if userlist:
            for u in userlist:
                strlist.append(u + "\r\n")
        m = ''.join(strlist)
        return m

    @staticmethod
    def tpc_parse_helper(parsed_msg):
        result_msg={}
        if parsed_msg[0] == ['request']:
            parsed_msg.remove(['request'])
            for i in parsed_msg:
                if len(i) is 2:
                    result_msg[i[0]] = i[1]
                elif len(i) is 1:
                    if result_msg['type'] == 'unichat':
                        result_msg['msgbody'] = parsed_msg[-1][0]
                    elif result_msg['type'] == 'list':
                        result_msg['list'] = parsed_msg[i:len(parsed_msg)-1]
        elif parsed_msg[0] == ['response']:
            parsed_msg.remove(['response'])
            for i in parsed_msg:
                if len(i) is 2:
                    result_msg[i[0]] = i[1]
                elif len(i) is 1:
                    if result_msg['type'] == 'pollchat':
                        result_msg['pollchat'] = i[0]
                    elif result_msg['type'] == 'list':
                        if not result_msg.has_key('list'):
                            result_msg['list'] = []
                        result_msg['list'].append(i[0])
        return result_msg