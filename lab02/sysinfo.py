from platform import *
from socket import *
import uuid
# from getmac import get_mac_address
import psutil


# platform
print("OS: " + system())
print("Processor: " + processor())
print("Machine type: " + machine())
print("Platform: " + platform())
print("Version: " + version())
print("Uname: " + str(uname()))

# socket
hostname = gethostname()
print("Host name: " + hostname)

# ip = gethostbyname(hostname)
# print("IP Address: " + ip)

macadd = uuid.getnode()
print("MAC Address: " + str(macadd))

cpu = psutil.cpu_percent()
print("CPU Usage: " + str(cpu) + "%")

ram = psutil.virtual_memory()[2]
print("RAM Usage: " + str(ram) + "%")

print("Swap memory information: " + str(psutil.swap_memory()))

print("Total physical memory: " + str(psutil.virtual_memory()) + "bytes")

