### Gunicorn experiments

# Tools used
- Prometheus - ran locally
  `cmd => ./prometheus --web.enable-remote-write-receive`
  `enable-remote-write-receive` lets you add data to prometheus by using k6 integration

- k6 - installed through go toolchain, the default binary was overwritten by xk6 to add the prometheus extention 
  `cmd => K6_PROMETHEUS_REMOTE_URL=http://localhost:9090/api/v1/write k6 run load-tests/script.js -o output-prometheus-remote`

# Experiments details
- Experiment #1 - Load testing GET requests with 2 worker
  `cmd => ./run.sh --workers=1 experiment1:app`
