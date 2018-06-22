#coding:utf-8
from baseproxy.proxy import CAAuth

__author__ = 'qiye'
__date__ = '2018/6/20 11:30'

ca = CAAuth(ca_file = "ca.pem", cert_file = 'ca.crt')
cnp = ca["www.baidu.com"]
print(cnp)