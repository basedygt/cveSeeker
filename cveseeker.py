import nmap
import requests

class CveSeeker:

  def __init__(self, hosts):
    self.hosts = hosts

  def scan_host(hostname):
    nm = nmap.PortScanner()
    result = nm.scan(hosts=hostname, ports=port, arguments="-sV")
    
