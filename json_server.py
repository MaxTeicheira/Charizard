import tornado.ioloop
import tornado.web

import transmissionrpc as tr





class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")
        
    def post(self):
        print self.request.arguments
        client = tr.Client()
            try:
            torrent = client.add_torrent()
        except:
            torrent = client.get_torrents([])


application = tornado.web.Application([
    (r"/" ,MainHandler),
    ])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
