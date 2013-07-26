#!/usr/bin/env python
"""
				Creating a simple HTTP Server

"""



import SocketServer
import SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/admin' :
			self.wfile.write('This page is only for admins ...!\n')
			self.wfile.write(self.headers)
		else:
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
		


serverAddr = ('' , 8000)
httpServer = SocketServer.ThreadingTCPServer(serverAddr , HttpRequestHandler)
httpServer.serve_forever()