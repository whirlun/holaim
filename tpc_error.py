# -*- coding: utf-8 -*-
from functools import wraps
from tpc_server_message import TPC_Server_Message
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='tpc_error.log',
                filemode='w')
errdict = {}

class TPCError(Exception):
    '''base exception class of all TPC errors'''
    def __init__(self, e, msg, errcode):
        logging.info(str(errcode)+":"+msg)
        self.e = e

    def errcode(self):
        return self.e()

class UsernameError(TPCError):
    def __init__(self, msg= "Undefined username", errcode=201):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 201


class PasswordError(TPCError):
    def __init__(self, msg= "Wrong password", errcode=202):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 202


class InvalidUserError(TPCError):
    def __init__(self, msg="Invalid user", errcode=203):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 203

class DstuserNotOnlineError(TPCError):
    def __init__(self, msg="the destination user is not online", errcode=204):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 204

class UserAlreadyExistError(TPCError):
    def __init__(self, msg="the user is already existed", errcode=205):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 205

class MessageLengthError(TPCError):
    def __init__(self, msg="the message is too long", errcode=301):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 301

class MessageNotPermittedError(TPCError):
    def __init__(self, msg="the user is not permitted to send messages", errcode=302):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 302

class WrongFilenameError(TPCError):
    def __init__(self, msg="the filename is wrong", errcode=304):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 304

class InvalidFileIDError(TPCError):
    def __init__(self, msg="cannot find the specific fileID", errcode=305):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 305

class NoDownloadInvitationError(TPCError):
    def __init__(self, msg="the user does not have download invitation", errcode=306):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 306

class RefusedDownloadError(TPCError):
    def __init__(self, msg="the download invitation is refused", errcode=307):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 307

class ProcessedDownloadError(TPCError):
    def __init__(self, msg="the download invitation has been processed", errcode=308):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 308

class FileTransferNotPermittedError(TPCError):
    def __init__(self, msg="the file transfer request is not permitted", errcode=309):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 309



class UploaderValidationError(TPCError):
    def __init__(self, msg="the user is not the uploader of specific uploader", errcode=311):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 311

class FilenameValidationError(TPCError):
    def __init__(self, msg="the filename does not match the record of the specific ID", errcode=312):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 312

class NoRespondError(TPCError):
    def __init__(self, msg="the receiver does not respond to the file transfer request", errcode=313):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 313

class KickoutError(TPCError):
    def __init__(self, msg="the user has been kicked out", errcode=401):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 401

class GroupCreationError(TPCError):
    def __init__(self, msg="the creation of group is failed", errcode=501):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 501

class GroupnameInvalidError(TPCError):
    def __init__(self, msg="the groupname is invalid", errcode=502):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 502

class UndefinedGroupError(TPCError):
    def __init__(self, msg="the specific group is not found", errcode=503):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 503

class UnauthorizedGroupOperationError(TPCError):
    def __init__(self, msg="the group operation is not permitted", errcode=504):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 504

class UserexistedInGroupError(TPCError):
    def __init__(self, msg="the specific user is existed in the group", errcode=505):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 505

class UserNotExistedInGroupError(TPCError):
    def __init__(self, msg="the specific user is not existed in the group", errcode=506):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 506

class GroupNumberOverflowError(TPCError):
    def __init__(self, msg="the number of groups is exceeded", errcode=507):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 507

class UserNumberOverflowError(TPCError):
    def __init__(self, msg="the number of users in the group is exceeded", errcode=508):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 508

class NotBelongToGroupError(TPCError):
    def __init__(self, msg="the user does not belong to the specific group", errcode=509):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 509

class ForbiddenError(TPCError):
    def __init__(self, msg="the user is forbidden", errcode=601):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 601

class ForbiddenCancelled(TPCError):
    def __init__(self, msg="the user is allowed to send message", errcode=602):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 602

class PackageParseError(TPCError):
    def __init__(self, msg="the data package cannot be parsed correctly", errcode=701):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 701

class InternalError(TPCError):
    def __init__(self, msg="server internal error", errcode=702):
        self.msg = msg
        TPCError.__init__(self,self,msg,errcode)

    def __call__(self):
        return 702


def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except TPCError as e:
            funcname = func.__name__
            if kwargs.has_key('uuid') is False:
                kwargs['uuid']='00000000-0000-0000-0000-000000000000'
            kwargs['errcode'] = e()
            #temp = list(args)
            #temp.append(e())
            #args = tuple(temp)
            result = getattr(TPC_Server_Message, funcname)( *args, **kwargs)
            return result
    return wrapper

def initErrdict():
    subclasses = TPCError.__subclasses__()
    for sc in subclasses:
        errdict[sc()()] = sc

def client_error_message(errcode):
    if errdict == {}:
        initErrdict()
        return errdict[int(errcode)]().msg
    else:
        return errdict[int(errcode)]().msg