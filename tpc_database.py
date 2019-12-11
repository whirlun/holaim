# -*- coding:utf-8 -*-
import datetime

from tpc_model import db, User, OpLog, MsgLog
from functools import wraps
import uuid, hashlib
from peewee import PeeweeException
from collections import namedtuple
from tpc_error import *


RESERVEDUUID = '00000000-0000-0000-0000-000000000000'

def database_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except PeeweeException, e:
            return (False, str(e.__class__)[15:len(str(e.__class__))-2])
        except StopIteration:
            return (False, 'noRecord')
        except Exception, e:
            raise e
    return wrapper

@database_error_handler
def add_user(username, password):
    'call when a new user registers'
    user = User(username=username, password=hashlib.sha1(password).hexdigest(), uuid=RESERVEDUUID, isLoggedin=0)
    user.save()
    return (True, 'ok')

@database_error_handler
def remove_user(username):
    'call when a user is deleted'
    query = User.select().where(username==username)
    for q in query:
        q.delete_instance()
    return (True, 'ok')

@database_error_handler
def user_login(username, password):
    'call when a user logged in'
    query = User.select().where(User.username == username)
    q = query.__iter__().next()
    #print q.username
    if q.password == hashlib.sha1(password).hexdigest():
        q.uuid = uuid.uuid1()
        q.isLoggedin = 1
        q.save()
        return (True, ['ok', q.uuid])
    else:
        return (False, 'password')

@database_error_handler
def user_logout(uuid):
    'call when a user logged out'
    query = User.select().where(User.uuid==uuid)
    for q in query:
        q.isLoggedin = 0
        q.uuid = RESERVEDUUID
        q.save()
        return (True, ['ok', q.username])

@database_error_handler
def get_userlist(uuid):
    'call when user needs a userlist'
    check_user(uuid)
    query = User.select()
    user_struct = namedtuple('User', 'id username isLoggedin')
    user_list = []
    for q in query:
        user = user_struct(id = q.id, username = q.username,isLoggedin = q.isLoggedin)
        user_list.append(user)
    user_tuple = tuple(user_list)
    return (True, ['ok', user_tuple])

@database_error_handler
def check_user(uuid):
    'call when a function needs to check whether the request is authorized'
    query = User.select().where(User.uuid==uuid)
    if len(query) == 0:
        raise InvalidUserError

@database_error_handler
def write_msg(srcuser, dstuser, msgbody):
    'call when a msg is sent to a user'
    msg = MsgLog(srcuser = srcuser, dstuser = dstuser, msgbody = msgbody, msgtime = datetime.now(), isread = 0)
    msgbody.save()
    return (True, 'ok')

@database_error_handler
def get_msg(username):
    'call when a user needs to get his or hr messages'
    query = MsgLog.select().where(MsgLog.dstuser==username, MsgLog.isread == 0)
    if len(query) == 0:
        return tuple()
    msg_struct = namedtuple('Msg', 'srcuser msgbody')
    msglist = []
    for q in query:
        msglist.append(msg_struct(srcuser = q.srcuser, msgbody = str(q.msgbody)))
        q.isread = 1
        q.save()

    return (True, ['ok', tuple(msglist)])