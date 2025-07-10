import pyautogui
import time

print("You have 10 seconds to place the cursor where you want typing to begin...")
time.sleep(10)

lines_to_type = [
    # "CORPADMIN",
    # "NetSec-Admin1",
    "enable",
    "RTR-AdminP@55",
    "conf ter",
    
    "access-list 120 permit ip 209.165.200.240 0.0.0.15 198.133.219.32 0.0.0.31",
    
    "crypto isakmp policy 10",
    "encryption aes 256",
    "hash sha",
    "authentication pre-share",
    "group 2",
    "lifetime 1800",
    "exit",

    "crypto isakmp key Vpnpass101 address 198.133.219.2",

    "crypto ipsec transform-set VPN-SET esp-aes esp-sha-hmac",

    "crypto map VPN-MAP 10 ipsec-isakmp",
    "match address 120",
    "set transform-set VPN-SET",
    "set peer 198.133.219.2",
    "set pfs group2",
    "set security-association lifetime seconds 1800",
    "exit",

    "int s0/0/0",
    "crypto map VPN-MAP",
    "end",
    "copy running-config startup-config"
]

for line in lines_to_type:
    pyautogui.write(line, interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)
