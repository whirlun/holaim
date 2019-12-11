# -*- coding:utf-8 -*-
import array

from tpc_database import *
from tpc_error import *
from tpc_server_message import TPC_Server_Message
from tpc_analyser import parser
from tpc_helpers import TPC_Helpers

blank = "blank"

def request_handler(msg):
    handlers = {"login":respond_login, "logout":respond_logout, "register": respond_register,
                "list": respond_userlist, "unichat": respond_unichat}
    parsed = parser.parse(msg)
    print parsed
    cli_msg = TPC_Helpers.tpc_parse_helper(parsed)
    func = handlers[cli_msg['type']]
    varnames = func.__doc__.split(',')
    arglist = []
    print cli_msg
    for var in varnames:
        arglist.append(cli_msg[var])
    arglist = tuple(arglist)
    m = func(*arglist)
    return m


@error_handler
def respond_login(username, password):
    'username,password'
    r = user_login(username, password)
    (status, msg) = r
    if not status:
        if msg == "noRecord":
            raise UsernameError
        elif msg == "password":
            raise PasswordError
    else:
        [_,uuid] = msg
        return TPC_Server_Message.respond_login(username,blank,uuid)


@error_handler
def respond_logout(uuid):
    'uuid'
    r = user_logout(uuid)
    (status, msg) = r
    if not status:
        raise InvalidUserError
    else:
        [_, username] = msg
        return TPC_Server_Message.respond_logout(username, uuid)

@error_handler
def respond_register(username, password):
    'username,password'
    r = add_user(username,password)
    (status, msg) = r
    if not status:
        if msg == "IntegrityError":
            raise UserAlreadyExistError
        else:
            raise InternalError
    else:
        return TPC_Server_Message.respond_register(username, blank,RESERVEDUUID)

@error_handler
def respond_userlist(uuid):
    'uuid'
    r = get_userlist(uuid)
    (status, msg) = r
    if not status:
        raise InternalError
    else:
        _, user_tuple = msg
        userlist = []
        userid = array.array('I')
        loggedincounter = 0
        for u in user_tuple:
            userlist.append(u.username)
            userid.append(u.id)
            if u.isLoggedin == 1:
                loggedincounter += 1
        return TPC_Server_Message.respond_userlist(userlist, len(user_tuple), loggedincounter, userid[0], len(user_tuple), uuid)


@error_handler
def respond_chatpoll(uuid, username):
    'uuid,username'
    r = get_msg(username)
    (status, msg) = r
    if not status:
        raise InternalError
    else:
        [_, msglist] = msg
        return TPC_Server_Message.respond_pollchat(uuid, msglist)


@error_handler
def respond_unichat(uuid, srcuser, dstuser, msglen, msgbody):
    'uuid,srcuser,dstuser,msglen,msgbody'
    if msglen == len(msgbody):
        r = write_msg(srcuser, dstuser, msgbody)
        (status, msg) = r
        if not status:
            raise InternalError
        else:
            return TPC_Server_Message.respond_unichat(uuid, srcuser,dstuser, msglen, msgbody)
    else:
        raise MessageLengthError