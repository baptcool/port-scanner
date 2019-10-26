import nmap

def doScanIp4(adressesipv4,scan_result):
    nm = nmap.PortScanner()
    for adress in adressesipv4:   
        scan_result[adress]["res"] = nm.scan(hosts=adress)
        #print(nm.scaninfo())
        #print(nm._scan_result)
        for host in nm.all_hosts():
            scan_result[adress]["finished"] = True
            print('----------------------------------------------------')   
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            print('----------------------------------------------------')   
            