# coding=utf-8
#!/usr/bin/env python3

import asyncio
from proxybroker import Broker
from requests import get

from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status

async def show(proxies, proxy_list):
    while (len(proxy_list) < 20):
        proxy = await proxies.get()
        if proxy is None: break

        print_success("[" + str(len(proxy_list) + 1) + "/20]", "Proxy found:", proxy.as_json()["host"] + ":" + str(proxy.as_json()["port"]))
        
        proxy_list.append(
            proxy.as_json()["host"] + ":" + str(proxy.as_json()["port"])
        )

        pass
    pass


def find_proxies():
    proxy_list = []
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(
            types=['HTTPS'], limit=20), show(proxies, proxy_list)
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
    
    if (len(proxy_list) % 2 != 0 and len(proxy_list) > 2):
        proxy_list = proxy_list[:len(proxy_list) - (len(proxy_list) % 2)]

    return proxy_list