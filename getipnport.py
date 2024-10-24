import socket

def get_ip_address():
  """Gets the IP address of the local machine."""
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    port = s.getsockname()[1]

    print("Your IP address is : ", ip)
    print("Ephemeral Port no : ", port)
    s.close()
    return ip
  except Exception as e:
    print(f"Error getting IP address: {e}")
    return None

if __name__ == "__main__":
  ip_address = get_ip_address()

# OUTPUT:
# Your IP address is :  172.16.116.15
# Ephemeral Port no :  58051
