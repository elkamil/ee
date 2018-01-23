import os
hostname = "172.217.21.174"
response = os.system("ping -c 1 " + hostname)


def is_online():
    if response == 0:
        return True
    else:
        return False
