from sanic import Sanic
from sanic.response import text
import logging
import multiprocessing

logging.basicConfig(level=logging.ERROR)

app = Sanic(__name__)

@app.route("/echo")
async def test(request):
    return text('echo')

if __name__ == "__main__":
    workers = multiprocessing.cpu_count() * 2 + 1
    app.run(host="0.0.0.0", port=5000, debug=False, workers=workers, access_log=False)
