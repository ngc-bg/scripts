
#!/usr/bin/env python
import socket
#import re
import sys
#
# Use this script to test connectivity to server address:port.
# Returns True or False... :)
#
# Open socket & connect to the destination.
# pcheck.py [-a destination address] [-p destination port].
# The default is "localhost:80"

def server_check(address, port):
    s = socket.socket()
    # print "Attempting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        # print "Connected to %s on port %s" % (address, port)
        return True
    except socket.error: #e:
        # print "Connection to %s on port %s failed: %s" % (address, port, e)
        return False

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for server", metavar="ADDRESS")
    parser.add_option("-p", "--port", dest="port", type="int", default=8080, help="PORT for server", metavar="PORT")
    (options, args) = parser.parse_args()
    # print 'options: %s, args: %s' % (options, args)
    check = server_check(options.address, options.port)
    str(check)
    print ('server_check returned %s' % check)

    a = open("log.txt", 'w')
    for i in range(0,1):
        a.write(str(check) + "\n")
        a.close()

    sys.exit(not check)