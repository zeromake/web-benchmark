ab:
	ab -n 20000 -c 100 http://127.0.0.1:5000/echo > benchmark.log
siege:
	siege -q -lbenchmark.log -c 200 -r 100 -b http://127.0.0.1:5000/echo
