from tpc_error import *
from tpc_server_message import TPC_Server_Message
from tpc_analyser import parser
from tpc_client import TPC_Client_Request
from tpc_helpers import TPC_Helpers

@error_handler
def respond_logout(username, uuid):
    raise UnauthorizedGroupOperationError
    #return TPC_Server_Message.respond_logout(username, uuid)

r = TPC_Client_Request()
m  = r.request_unichat("23423121043611e896e29801a78c25e9","bbrabbit", "bbrabbit1", len("hello"), "hello")
print m
n = TPC_Helpers.tpc_parse_helper(m)
print n