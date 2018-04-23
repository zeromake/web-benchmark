ab:
	ab -n 200 -c 100 http://127.0.0.1:5000/echo | grep "per second"
siege:
	siege -c 200 -r 100 -b http://127.0.0.1:5000/echo > /dev/null
