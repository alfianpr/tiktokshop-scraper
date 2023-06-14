import subprocess as proc
import re
    
byte_output = proc.check_output(["adb", "shell", "ip", "addr", "show", "wlan0", "|", "grep", "inet"])
str_output = str(byte_output, "utf-8")
regex = re.findall(r'(?<=inet ).*?(?=/)', str_output)