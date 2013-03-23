import requests
import socket
from time import time
from sys import argv

def get_fastest_resolved_host(addr, scheme = 'http://'):
    '''
    get the fastest resolved host

    '''
    elapsed_time = {}
    try:
        ip_list = socket.gethostbyname_ex(addr)[2]
        for ip in ip_list:
            host_name = socket.gethostbyaddr(ip)[0]
            before = time()
            r = requests.get(scheme + str(host_name))
            if r.status_code == 200:
                elapsed_time[ip] = [(time() - before), host_name]
        return elapsed_time
            
    except socket.errno as msg:
        print 'Socket error'
        print msg

if __name__ == '__main__':
    for arg in argv[1:]:
        print '\nfor {0} : \n{1}'.format(arg, get_fastest_resolved_host(arg))
