#!/usr/bin/python
import rospy
import SimpleHTTPServer
import SocketServer
import webbrowser

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

# Opens the browser
webbrowser.open_new("localhost:8080")

while not rospy.is_shutdown():
    httpd.serve_forever()

httpd.shutdown()




