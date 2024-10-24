import uuid

def get_mac_address():
  """Gets the MAC address of the local machine."""
  try:
    mac_address = uuid.getnode()
    return ':'.join(('%012X' % mac_address)[i:i+2] for i in range(0, 12, 2))
  except Exception as e:
    print(f"Error getting MAC address: {e}")
    return None

if __name__ == "__main__":
  mac_address = get_mac_address()
  if mac_address:
    print("MAC address:", mac_address)
  else:
    print("Failed to get MAC address.")

#OUTPUT:    
#PS E:\sockets> py getmac.py
#MAC address: D8:BB:C1:2B:E2:FC
