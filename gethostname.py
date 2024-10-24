
import socket

def get_hostname():
  """Gets the hostname of the local machine."""
  try:
    hostname = socket.gethostname()
    return hostname
  except Exception as e:
    print(f"Error getting hostname: {e}")
    return None

if __name__ == "__main__":
  hostname = get_hostname()
  if hostname:
    print("Hostname:", hostname)
  else:
    print("Failed to get hostname.")

# PS E:\sockets> py gethostname.py
# Hostname: SYSTEMA15
