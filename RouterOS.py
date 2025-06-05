import routeros_api

# MikroTik router credentials
router_ip = "192.168.99.101"  # Change to your router's IP address
username = "admin"
password = ""

# ISP settings
isp_dns_servers = ["8.8.8.8", "8.8.4.4"]  # Example DNS servers
gateway_ip = "192.168.1.1"  # ISP Gateway IP
static_ip_address = "192.168.1.100"  # Static IP to set
netmask = "255.255.255.0"  # Netmask for the static IP
interface = "ether1"  # Interface to assign IP to

# Connect to the router
connection = routeros_api.RouterOsApiPool(router_ip, username=username, password=password, plaintext_login=True)
api = connection.get_api()

# Set DNS servers
api.get_resource('/ip/dns').set(servers=",".join(isp_dns_servers))

# Set default route to the ISP gateway
api.get_resource('/ip/route').add(dst_address="0.0.0.0/0", gateway=gateway_ip)

# Assign static IP address to the interface
api.get_resource('/ip/address').add(address=f"{static_ip_address}/{netmask}", interface=interface)

# Commit changes and close connection
connection.disconnect()

print("ISP settings and static IP address configured successfully!")