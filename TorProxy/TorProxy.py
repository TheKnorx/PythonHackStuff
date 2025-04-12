import os
import argparse
from subprocess import Popen, PIPE
from socks import socksocket, SOCKS5


"""parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-t", type=str, help="starts Tor and returns socket Object", required=False)
group.add_argument("-r", type=str, help="restarts Tor and returns socket object", required=False)
group.add_argument("-c", type=str, help="closes Tor", required=False)
args = parser.parse_args()"""


def get_proxy_socket():
    s = socksocket()
    s.set_proxy(SOCKS5, "127.0.0.1", 9050)
    return s


def kill_tor():
    pid = open("pid.txt", "r").read()
    os.kill(int(pid), 9)
    os.remove("pid.txt")


def start_tor():
    process = Popen("tor-win32-0.4.5.10/Tor/tor.exe", stdout=PIPE, stderr=PIPE)
    _, errors = process.communicate()
    return errors if errors else open("pid.txt", "w").write(str(process.pid))


"""if __name__ == '__main__':
    if args.t:
        start_tor() and get_proxy_socket()
    elif args.r:
        kill_tor() and start_tor() and get_proxy_socket()
    else:
        kill_tor()"""
