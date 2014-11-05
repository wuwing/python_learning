#-*-coding:utf-8-*-
#!/usr/bin/python
import socket
import sys
if len(sys.argv) < 3:
	print 'Usage: %s [hostname] [port name]' % sys.argv[0]
	sys.exit(1)

hostname = sys.argv[1]
port = int(sys.argv[2])

#Set up a standard Internet socket. The setsockopt call lets this
#server use the given port even if it was recently used by another sever(fot instance,an earlier incarnation of SimpleSocketServer).

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

sock.bind((hostname,port))
sock.listen(1)
print "Wait for a request"

request,clientAddress = sock.accept()
print "Received request from",clientAddress
request.send(bytes('-=SimpleSocketServer 3000=-\n'))
request.send(bytes('Go away!\n'))
request.shutdown(2)
print "Have handled request,stopping server"
sock.close()
"""套接字编程
运行演示:
python SimpleSocketServer.py localhost 2000 #启动服务器

telnet localhost 2000 #连接服务器
"""
