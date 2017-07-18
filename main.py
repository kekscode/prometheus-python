#!/usr/bin/env python3

import time
import psutil
import requests
import random
from prometheus_client import start_http_server, Gauge, Counter


def disk_usage(g):
    return g.set(psutil.disk_usage('/')[3])


def cpu_usage(g):
    return g.set(psutil.cpu_percent())


def resident_memory_size(g):
    p = psutil.Process().memory_info()[0]
    p = p / 1024 / 1024
    return g.set(p)


def fetch_page(url, bad, good):
    if random.randint(1, 10) == 1:  # ~10% HTTP 404
        url = url + "/kaputt"
    r = requests.get(url)
    if r.status_code == 200:
        print(r.status_code)
        good.inc()
    else:
        print(r.status_code)
        bad.inc()


def eat_memory(mem=1024):
    return (bytearray(mem))


if __name__ == '__main__':
    g_disk = Gauge('disk_free', 'Used disk space in percent')
    g_cpu = Gauge('cpu_usage', 'CPU usage in percent')
    g_memory = Gauge('memory_usage', 'Memory usage (MB)')

    c_http_request_good = Counter('http_requests_good',
                                  'GOOD http request counter')
    c_http_request_bad = Counter('http_requests_bad',
                                 'BAD http request counter')

    start_http_server(8000)
    sink = bytearray()

    while True:
        cpu_usage(g_cpu)
        disk_usage(g_disk)
        resident_memory_size(g_memory)

        fetch_page('http://ccc-ffm.de', c_http_request_bad,
                   c_http_request_good)

        sink += eat_memory(mem=10**6)

        time.sleep(1)
