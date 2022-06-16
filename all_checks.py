import os
import shutil
import sys
import socket


def check_network():
    try:
        socket.gethostbyname('www.google.com')
        return False
    except:
        return True

def Reboot():
    return os.path.exists('/run/reboot-required')

def check_disk_full(disk,min_gb,min_percent):
    du  = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabyte_free = du.free / 2**30
    
    if percent_free < min_percent or gigabyte_free < min_gb:
        return True
    return False
    
def disk_root_full():
    return check_disk_full('/',2,10)
    


def main():
    checks=[
        (Reboot,'Pending Reboot'),
        (disk_root_full,'Root Partition full'),
        (check_network,'No working Network')
    ]
    EveryThing_ok=True
    for check, msg in checks:
        if  check():
            print(msg)
            EveryThing_ok=False
        if not EveryThing_ok:
            sys.exit(1)
                
    print('Every Thing is Ok!')
    sys.exit(0)
    

main()