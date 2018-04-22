import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("echo")

def make_app():
    return tornado.web.Application([
        (r"/echo", MainHandler),
    ], debug=False)

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()