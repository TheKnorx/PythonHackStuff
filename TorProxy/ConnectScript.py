import requests

from TorProxy import get_proxy_socket, start_tor
import subprocess


# subprocess.Popen("tor-win32-0.4.5.10/Tor/tor.exe")
address = "zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion"
socket = get_proxy_socket()
socket.connect((address, 80))
socket.sendall(f"GET / HTTP/1.1\r\nHost:{address}\r\n\r\n".encode())
print(socket.recv(9999).decode())


"""proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}
url = "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page#Whistleblowing"
r = requests.get(url, proxies=proxies)
print(r.text)"""
