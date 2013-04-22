import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
        
    def post(self):
        print self.request.arguments["data"]

application = tornado.web.Application([
    (r"/" ,MainHandler),
    ])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
