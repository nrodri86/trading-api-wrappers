from ..base import Server

# API Server
PROTOCOL = 'https'
HOST = 'www.bitstamp.net/api'
VERSION = 'v2'


# SURBTC API server
class BitstampServer(Server):

    def __init__(self):
        Server.__init__(self, PROTOCOL, HOST, VERSION)