import tornado.ioloop
import tornado.web
import multiprocessing


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("echo")

def make_app():
    return tornado.web.Application([
        (r"/echo", MainHandler),
    ], debug=False)

if __name__ == "__main__":
    workers = multiprocessing.cpu_count() * 2
    server = tornado.httpserver.HTTPServer(make_app())
    server.bind(5000)
    server.start(workers)  # forks one process per cpu
    tornado.ioloop.IOLoop.current().start()