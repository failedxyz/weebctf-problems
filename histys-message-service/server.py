#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer,threading,os,time
import signal
#from secrets import *
from Crypto.Cipher import AES
import os

key = 'h1st01r3_k3y_123'
iv  = '1nIt_v3ctor_3456'
#PORT = 7765

def decode(bytestring, k=16):
    """
    Remove the PKCS#7 padding from a text bytestring.
    """
    #print(bytestring)
    #print(bytestring.encode('hex'))
    val = ord(bytestring[-1])
    #print(val)
    if bytestring[-val:] != bytestring[-1]*val:
        return '( ≧Д≦) Bad padding!'
    if val > k:
        return '( ≧Д≦) Bad padding!'
        
    l = len(bytestring) - val
    return '(/^▽^)/ Message has been received!'


def encode(bytestring, k=16):
    """
    Pad an input bytestring according to PKCS#7
    
    """
    l = len(bytestring)
    val = k - (l % k)
    return str(bytestring + bytearray([val] * val))
    
def decrypts(s):
    global key, iv
    n = s.decode('hex')
    obj = AES.new(key, AES.MODE_CBC, iv)
    return obj.decrypt(n).encode('hex')

def calc(s):
    try:
        return decode(decrypts(s).decode('hex'))
    except Exception as e:
        print(e)
        return "(；￣Д￣）Error!"

class incoming(SocketServer.BaseRequestHandler):
    def handle(self):
        req = self.request

        def recvline():
            buf = ""
            while not buf.endswith("\n"):
                buf += req.recv(1)
            return buf
        signal.alarm(5)
        req.sendall("Histy's Message Service\n")
        req.sendall("(ﾟДﾟ；) Now with emotes!\n")
        
        req.sendall("Send your information AES encrypted:\n")
        data = recvline().strip()
        req.sendall(calc(data) + '\n')
        req.close()
 
class ReusableTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
  pass

SocketServer.TCPServer.allow_reuse_address = True
port = os.getenv('port',6004)
ip = os.getenv('ip','0.0.0.0')

server = ReusableTCPServer(('0.0.0.0', port), incoming)

print "Server listening on port %d" % port
print ip
server.serve_forever()
