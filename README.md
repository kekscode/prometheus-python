# Testing python client for prometheus

This repo is a little demo meant to show how to expose basic prometheus-compatible monitoring metrics from a python application using [this client library][promclient].

## Dependencies

* Python 3
  * requests module
  * prometheus_client module
  * psutil module
* [Prometheus][promserver]

## PromQL examples

Some queries for metrics/graphs:

* [All things by job label "pypromtests"][1]
* [Percentage of bad HTTP requests][2]

[1]: http://localhost:9090/graph?g0.range_input=5m&g0.expr=%7Bjob%3D%22pypromtests%22%7D&g0.tab=0
[2]: http://localhost:9090/graph?g0.range_input=1m&g0.expr=http_requests_bad+%2F+(http_requests_good+%2B+http_requests_bad)&g0.tab=1
[3]: http://localhost:9090/graph?g0.range_input=1m&g0.expr=(memory_usage+%2F+1024+%2F+1024)&g0.tab=1
[promserver]: https://prometheus.io/download/#prometheus
[promclient]: https://github.com/prometheus/client_python
