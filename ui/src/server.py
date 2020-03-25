#!/usr/bin/python
import rospy
import SimpleHTTPServer, SocketServer
import webbrowser
import os

PORT = 8080

class Server:
    def __init__(self):
        # Changing directory to source files
        DIR = os.path.dirname(os.path.realpath(__file__))
        os.chdir(DIR)

        # Creating socket and handler
        SocketServer.TCPServer.allow_reuse_address = True
        self.httpd = SocketServer.TCPServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
    
        # Opens the browser
        webbrowser.open_new("http://localhost:" + str(PORT))    
    
if __name__== '__main__':
    # Init ROS node and server
    rospy.init_node("server")
    server = Server()

    # Response on KeyboardInterrupt
    rospy.on_shutdown(server.httpd.server_close)

    # Request loop
    server.httpd.serve_forever()