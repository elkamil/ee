import os
hostname = "172.217.21.174"


def is_online():
    response = os.system("timeout 0.5 ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False
