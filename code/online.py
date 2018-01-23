import socket
# REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    timeout = 1.0
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    # s = socket.create_connection(host)
    s = socket.create_connection((host, 80), 2)
    s.settimeout(timeout)
    return True
  except:
     pass
  return False


# is_connected('google.com')
