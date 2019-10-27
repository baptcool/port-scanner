import nmap

def doScanIp4(adressesipv4,scan_result):
    nm = nmap.PortScanner()
    #print("cici")
    
    
    #print("voici ladresse", adressesipv4)
    for adress in adressesipv4:  
        
        scan_result[adress]["res"] = nm.scan(hosts=adress,arguments="-sV --version-light")
        
        scan_result[adress]["finished"] = True
        #print(nm.scaninfo())
        #print(nm._scan_result)
        for host in nm.all_hosts():
            
            print('----------------------------------------------------')   
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------') 
      
def doScanIp6(adressesipv6,scan_result):
    nm = nmap.PortScanner()
    #print("cici")
    for adress in adressesipv6:  
        
        scan_result[adress]["res"] = nm.scan(hosts=adress,arguments="-6 -sV --version-light")
        
        scan_result[adress]["finished"] = True
        #print(nm.scaninfo())
        #print(nm._scan_result)
        for host in nm.all_hosts():
            
            print('----------------------------------------------------')   
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------') 
      
            
