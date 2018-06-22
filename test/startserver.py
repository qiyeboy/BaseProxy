#coding:utf-8
__author__ = 'qiye'
__date__ = '2018/6/22 18:38'
from baseproxy.proxy import AsyncMitmProxy

baseproxy = AsyncMitmProxy(server_addr=('',8899),https=True)

baseproxy.serve_forever()