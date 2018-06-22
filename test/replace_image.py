#coding:utf-8
__author__ = 'qiye'
__date__ = '2018/6/22 22:55'

from baseproxy.proxy import RspIntercept, AsyncMitmProxy



class ImageInterceptor( RspIntercept):

    def deal_response(self, response):
        if response.get_header("Content-Type") and 'image' in response.get_header("Content-Type"):
            with open("../img/qiye2.jpg",'rb') as f:
                response.set_body_data(f.read())
        return response


if __name__ == "__main__":
    baseproxy = AsyncMitmProxy(https=True)
    baseproxy.register(ImageInterceptor)
    baseproxy.serve_forever()