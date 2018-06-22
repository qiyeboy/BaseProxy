#coding:utf-8
from baseproxy.proxy import ReqIntercept, RspIntercept, AsyncMitmProxy

__author__ = 'qiye'
__date__ = '2018/6/21 23:35'

class DebugInterceptor(ReqIntercept, RspIntercept):

    def deal_request(self, request):

        return request

    def deal_response(self, response):

        if response.get_header("Content-Type") and 'image'in response.get_header("Content-Type"):
            response = None

        return response

if __name__=="__main__":

    baseproxy = AsyncMitmProxy(https=False)
    baseproxy.register(DebugInterceptor)
    baseproxy.serve_forever()