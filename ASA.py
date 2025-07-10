import pyautogui
import time

print("You have 10 seconds to place the cursor where you want typing to begin...")
time.sleep(10)

lines_to_type = [
    "enable",
    "Thecar1Admin",
    "conf term",
    "domain-name thecar1.com",
    "hostname HQ-ASA5506",
    "",
    "interface g1/1",
    "nameif OUTSIDE",
    "security-level 1",
    "ip address 209.165.200.253 255.255.255.240",
    "no shutdown",
    "",
    "interface g1/2",
    "nameif INSIDE",
    "security-level 100",
    "ip address 192.168.10.1 255.255.255.0",
    "no shutdown",
    "",
    "interface g1/3",
    "nameif DMZ",
    "security-level 70",
    "ip address 192.168.20.1 255.255.255.0",
    "no shutdown",
    "exit",
    "dhcpd address 192.168.10.25-192.168.10.35 INSIDE",
    "dhcpd dns 192.168.10.10 interface INSIDE",
    "dhcpd option 3 ip 192.168.10.1",
    "dhcpd enable INSIDE",
    "route OUTSIDE 0.0.0.0 0.0.0.0 209.165.200.254",
    "ntp authenticate",
    "ntp authentication-key 1 md5 corpkey",
    "ntp server 192.168.10.10",
    "ntp trusted-key 1",
    "username Car1Admin password adminpass01",
    "aaa authentication ssh console LOCAL",
    "crypto key generate rsa modulus 1024",
    "yes",
    "ssh 192.168.10.250 255.255.255.255 INSIDE",
    "ssh timeout 20",
    "object network INSIDE-nat",
    "subnet 192.168.10.0 255.255.255.0",
    "nat (inside,outside) dynamic interface",
    "exit",
    "configure terminal" ,
    "object network DMZ-web-server",
    "host 192.168.20.2",
    "nat (dmz,outside) static 209.165.200.241",
    "exit",
    "configure terminal",
    "object network DMZ-dns-server",
    "host 192.168.20.5",
    "nat (dmz,outside) static 209.165.200.242",
    "exit",
    "configure terminal",
    "access-list NAT-IP-ALL extended permit ip any any",

    "access-group NAT-IP-ALL in interface OUTSIDE",
    "access-group NAT-IP-ALL in interface DMZ",

    "access-list OUTSIDE-TO-DMZ extended permit tcp any host 209.165.200.241 eq 80",
    "access-list OUTSIDE-TO-DMZ extended permit tcp any host 209.165.200.242 eq 53",
    "access-list OUTSIDE-TO-DMZ extended permit udp any host 209.165.200.242 eq 53",
    "access-list OUTSIDE-TO-DMZ extended permit tcp host 198.133.219.35 host 209.165.200.241 eq ftp",
    "end",
    "copy running-config startup-config",
    ""
        
    ]

for line in lines_to_type:
    pyautogui.write(line, interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)
