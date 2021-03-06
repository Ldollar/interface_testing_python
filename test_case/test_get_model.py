# coding=utf-8
# -*- coding:utf-8 -*-
import requests

from test_case.public import define_random_str

HTTP_CODE_SUCCESS = 200

import json

import logging
from swaggerpy.http_client import SynchronousHttpClient

from public import define_regex
from public.define_log import LogDefine


class InterfaceModel():
    def __init__(self):
        LogDefine()
        self.http_client = SynchronousHttpClient()
        # self.host
        # self.port
        # self.method
        # self.parameters
        # self.data
        self.verification = []

    def define_request_method(self, method, url, parameters=None, data=None):

        """请求模板"""
        try:
            res = self.http_client.request(method=method, url=url, params=parameters, data=data)
            http_code = res.status_code
            if http_code == HTTP_CODE_SUCCESS:
                logging.info("if code == 200 ,request success!")
                print u"返回200，请求成功", res.url
                print res.text
                return res

            else:
                logging.error("not return code 200 ,request hava some problem")
                print res.url
                print u"响应出错 code %s" % http_code
                print res.text
        except Exception,e:
            logging.info(u"请求出问题了 %s ",e)
            print e

    def parse_method_res(self, response, expected_data=None):

        """对返回数据处理分析"""
        try:
            data = json.loads(json.dumps(expected_data))
            #print data["expect_code"]
            s = define_regex.find_code(text=response.text)
            #print type(s),type(data["expect_code"])
            logging.info("type vs type %s vs %s",type(s),type(data["expect_code"]))
            if int(s) == data["expect_code"]:
                logging.info("correct response code: %s ", s)
                print u"返回正确 code: %s" % s
                if data["expect_message"]:
                    pass
            else:
                logging.error("incorrect response code: %s", s)
                # self.verification.append("incorrect response")
                print u"接口请求失败 code: %s " % s
        except Exception,e:
            logging.info(u"Response 可能没有获取到 %s" ,e)
            print u"Response 可能没有获取到 %s" %e


