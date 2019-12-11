# -*- coding:utf-8 -*-
from peewee import *

db = SqliteDatabase('./tpc_devenv.db')

class User(Model):
    username = CharField(unique=True)
    password = CharField()
    uuid = UUIDField()
    isLoggedin = SmallIntegerField()

    class Meta:
        database = db

class OpLog(Model):
    opuser = CharField()
    opname = CharField()
    errcode = IntegerField()
    optime = DateTimeField()

    class Meta:
        database = db

class MsgLog(Model):
    srcuser = CharField()
    dstuser = CharField()
    msgbody = CharField()
    msgtime = DateTimeField()
    isread = SmallIntegerField()

    class Meta:
        database = db
