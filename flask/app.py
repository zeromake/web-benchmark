#!/bin/env python
from flask import Flask

app = Flask(__name__)

@app.route("/echo")
def echo():
	return "echo"

if "__main__" == __name__:
	app.run(host="0.0.0.0", port=5000, debug=False)

