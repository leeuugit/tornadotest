#!/usr/local/bin/python3.6


import tornado.ioloop
import tornado.web

class hellomain(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Hello, world</h1>"
                   "<h2>This is test tornado web server</h2>")

def make_app():
    return tornado.web.Application([
        (r"/", hellomain),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

