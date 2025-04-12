from socks import socksocket, SOCKS5


host = "zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion"


def get_proxy_socket():
    s = socksocket()
    s.set_proxy(SOCKS5, "127.0.0.1", 9050)
    return s


socket = get_proxy_socket()
socket.connect((host, 80))
socket.sendall(f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode())
html = ""
while True:
    _html = socket.recv(1024).decode()
    if html:
        html += _html
    elif len(_html) < 1024:
        html += _html
        break
    else:
        break
print("HTML:\n" + html)
