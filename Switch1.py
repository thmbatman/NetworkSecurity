import pyautogui
import time

print("You have 10 seconds to place the cursor where you want typing to begin...")
time.sleep(10)

lines_to_type = [
    "enable",
    "conf t",
    "interface range f0/2-4, f0/6-9, f0/11-22, g0/2",
    "shutdown",
    "switchport mode access",
    "switchport nonegotiate",
    "interface range f0/1, f0/5, f0/10",
    "switchport mode access",
    "switchport port-security",
    "switchport port-security maximum 2",
    "switchport port-security mac-address sticky",
    "switchport port-security violation restrict",
    "switchport nonegotiate",
    "interface range f0/1, f0/5, f0/10, g0/1",
    "spanning-tree bpduguard enable",
    "spanning-tree portfast",
    "end",
    "copy running-config startup-config",
    ""
]

for line in lines_to_type:
    pyautogui.write(line, interval=0.05)
    pyautogui.press('enter')
    time.sleep(1)
