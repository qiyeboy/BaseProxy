#coding:utf-8

__author__ = 'qiye'
__date__ = '2018/6/21 23:34'


from setuptools import setup

setup(
    name='baseproxy',
    author='qiye',
    version='1.0.1',
    author_email='qiye_email@qq.com',
    description='Asynchronous HTTP/HTTPS proxy that intercepts and modifies messages(异步http/https代理,可拦截修改报文)',
    long_description='please visit https://github.com/qiyeboy/BaseProxy',
    license='GPLv2',
    url='https://github.com/qiyeboy/BaseProxy',
    download_url='https://github.com/qiyeboy/BaseProxy',
    packages=['baseproxy'],
    install_requires = [
        'pyOpenSSL==18.0.0',
        'chardet==3.0.4'
    ]
)

