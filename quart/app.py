from quart import Quart

app = Quart(__name__)

@app.route('/echo')
async def hello():
    return 'echo'

if __name__ == '__main__':
    app.run(port=5000)