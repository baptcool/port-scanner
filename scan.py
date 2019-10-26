import nmap

def doScanIp4(adressesipv4,scan_result):
    nm = nmap.PortScanner()
    print("cici")
    for adress in adressesipv4:  
        print("cici222")
        scan_result[adress]["res"] = nm.scan(hosts=adress,arguments="")
        print("cici")
        scan_result[adress]["finished"] = True
        #print(nm.scaninfo())
        #print(nm._scan_result)
        for host in nm.all_hosts():
            
            print('----------------------------------------------------')   
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------') 
      
            
