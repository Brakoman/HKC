import socket
import threading

def portscan():
    host        = raw_input('\033[1;34m[?]  \033[1;37mHOST        : \033[1;30m')
    scan_dari   = int(raw_input('\033[1;34m[?]  \033[1;37mSCAN DARI   : \033[1;33m'))
    scan_sampai = int(raw_input('\033[1;34m[?]  \033[1;37mSCAN SAMPAI : \033[1;33m'))
    rem=socket.gethostbyname(host)
    print "\033[1;33m\n[+] STARTING PORT SCANNER"
    try:
        for port in range(scan_dari,scan_sampai):
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            res=sock.connect_ex((rem,port))
            if res==0:
                print '\033[1;37m[!]  \033[1;35m{}   \033[1;36mTERBUKA'.format(port)
            else:
                print '\033[1;32m[-]  \033[1;35m{}   \033[1;33mTERTUTUP'.format(port)
            sock.close()
    except socket.gaierror:
        print '\033[1;31m[!] HOST TIDAK DI TEMUKAN! atau anda offline!'
