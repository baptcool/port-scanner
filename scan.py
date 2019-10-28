import nmap

def doScanIp4(adressesipv4,scan_result):
    nm = nmap.PortScanner()
    
    for adress in adressesipv4:  
        #écriture du résultat du scan dans le dictionnaire
        scan_result[adress]["res"] = nm.scan(hosts=adress,arguments="-sV --version-light")
        
        scan_result[adress]["finished"] = True
        
        for host in nm.all_hosts():
            
            print('----------------------------------------------------')   
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------') 
      
def doScanIp6(adressesipv6,scan_result):
    nm = nmap.PortScanner()
    
    for adress in adressesipv6:  
        #écriture du résultat du scan dans le dictionnaire
        scan_result[adress]["res"] = nm.scan(hosts=adress,arguments="-6 -sV --version-light")
        
        scan_result[adress]["finished"] = True
        
        for host in nm.all_hosts():
            
            print('----------------------------------------------------')   
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------') 
      
            
