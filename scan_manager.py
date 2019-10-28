
import os
import time

import subprocess
import queue
import threading

from report_generator import generateReport
import scan

class Scan_Manager():

    def __init__(self, thread_enable,nbThr, adressesipv4, adressesipv6 ):

        self.arrayThr =  queue.Queue() #la queue des tasches a(non ascii) faire
    
        if thread_enable == 1:
            if nbThr >=1:
                self.nbThr = nbThr
            else:
                self.nbThr = 1
        else:
            self.nbThr = 1
        self.nbThrInUse = 0
        self.lock = threading.Lock()
        
        nbIp = len(adressesipv4) +len(adressesipv6)      
        
        self.scan_result = dict()
        
        if nbIp < self.nbThr:
            self.nbThr = nbIp
        ipParThr = nbIp//self.nbThr
        #chaque thread a le meme nombre de scan(ip) a(non ascii) faire
        arraytemp = []         
        
            
        # *******
        # on met dans la Queue arrayThr des taches qui sont des listes d IPs
        # on ne melange pas les ipv4 et ipv6 par tache
        for index,ip in enumerate(adressesipv4):
            self.scan_result[ip] = dict()
            self.scan_result[ip]["finished"] = False 
            self.scan_result[ip]["type"] = "ipv4"
            arraytemp.append(ip)
            if (index+1) % ipParThr == 0 or index+1 ==  len(adressesipv4) :
                self.arrayThr.put((arraytemp,"ipv4"))
                arraytemp = []
        arraytemp = []
        for index,ip in enumerate(adressesipv6):
            self.scan_result[ip] = dict()
            self.scan_result[ip]["finished"] = False 
            self.scan_result[ip]["type"] = "ipv6"
            arraytemp.append((ip,"ipv6"))
            if (index+1) % ipParThr == 0  or index+1 ==  len(adressesipv6) :
                self.arrayThr.put((arraytemp,"ipv6"))
                arraytemp = []
        # *******
        
        
        
        self.startThread()
        generateReport(self.scan_result)



    def threadtask(self ):
        #Chaque thread execute cette fonction
        
        
        #Tant qu il y a des taches a(non ascii) faire dans la Queue
        while True != self.arrayThr.empty():
            temp = self.arrayThr.get()
            # temp est un tuple
            # temp[0] array de ips
            # temp[1] type de ips = ipv4/6
            
            #print("taille tuple",temp)
            if temp[1] == "ipv6":
                scan.doScanIp6(temp[0], self.scan_result) #lancement du scan
            elif temp[1] == "ipv4":
                scan.doScanIp4(temp[0], self.scan_result)          
            
        
            
        self.lock.acquire()
        try:
            self.nbThrInUse -= 1
        finally:
            self.lock.release()
            
    def startThread(self):
        array = []
        
        if (self.nbThr - self.nbThrInUse >= 0 ):
            for i in range(self.nbThr - self.nbThrInUse):
                
                self.lock.acquire()
                try:
                    self.nbThrInUse += 1
                finally:
                    self.lock.release()
                
                
                #on prepare les threads
                array.append(threading.Thread(target = self.threadtask, args=[]))
            for e in array:
                #puis on demarre les threads
                e.start()
               
            print("scan started")
            PourcentageFinished = 0
            while PourcentageFinished != 100:
               #on affiche la progression
                print("--- "  + str(PourcentageFinished) + " %  finished")
                time.sleep(1)
                PourcentageFinished = 0
                for k, v in self.scan_result.items():
                    if v["finished"] == True:
                        PourcentageFinished += 1
                PourcentageFinished =round(PourcentageFinished/len(self.scan_result.items()) *100)
                
                
                
            #enfin, lorsque le scan est termine, on affiche un cours resume
            try:
                for host in self.scan_result:
                                  
                    for sousHost in  self.scan_result[host]["res"]["scan"]:
                        print(sousHost + " is " + self.scan_result[host]["res"]["scan"][host]["status"]["state"])
                    
            except:
                print("error while reading scan results")  
            

    
       
        

