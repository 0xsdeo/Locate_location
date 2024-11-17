# -*- coding: UTF-8 -*-
# @Project ：Locate_location
# @File    ：main.py
# Author   ：0xsdeo
# Date     ：2024/11/14 23:14
import os
from mitmproxy.http import HTTPFlow


def download_js(host, content, js, temp_js):
    with open(f"{host}/{js}", "b+w") as f1:
        f1.write(content)
        with open(f"{host}/{temp_js}", "b+w") as f2:
            f2.write(content)
            f1.flush()
            f2.flush()


def response(flow: HTTPFlow):
    if ".js" == flow.request.url[-3:]:
        index = flow.request.url.rfind("/")
        js = flow.request.url[index + 1:]
        index = js.rfind(".")
        temp_js = js[:index] + '.temp.js'

        content = flow.response.content
        if "location.replace" in content.decode() or "location.href" in content.decode() or "location.assign" in content.decode():
            print(flow.request.url)
            if os.path.isdir(f"{os.getcwd()}/{flow.request.host}"):
                download_js(flow.request.host, content, js, temp_js)
            else:
                os.mkdir(f"{os.getcwd()}/{flow.request.host}")
                download_js(flow.request.host, content, js, temp_js)
