import logging
import os
import time

import subprocess
import queue
import threading
from logger import Logger
from report_generator import generateReport
import scan
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

class Scan_Manager():

    def __init__(self, thread_enable,nb_thread, adressesipv4, adressesipv6 ):

        self.arrayThr =  queue.Queue()
    
        if thread_enable == 1:
            if nb_thread >=1:
                self.nbThr = nb_thread
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
        
        arraytemp = [] 
        
        #ipIndex=0
        #while ipIndex<nbIp:
            
         #   if ipIndex < len(adressesipv4):
         #       self.scan_result[adressesipv4[ipIndex]] = dict()
         #       self.scan_result[adressesipv4[ipIndex]]["type"] = "ipv4"
         #       self.scan_result[adressesipv4[ipIndex]]["finished"] = False 
         #       arraytemp.append(adressesipv4[ipIndex])
         #   else:
         #       self.scan_result[adressesipv6[ipIndex]] = dict()
         #       self.scan_result[adressesipv4[ipIndex]]["type"] = "ipv6"
         #       self.scan_result[adressesipv6[ipIndex]]["finished"] = False 
         #       arraytemp.append(adressesipv6[ipIndex])
                
                
         #   if (ipIndex+1) % ipParThr == 0  or ( len(adressesipv4) != 0 and ipIndex+1 == len(adressesipv4)  ) :
         #       self.arrayThr.put(arraytemp)
         #       arraytemp = []
         #   ipIndex+=1
            
             
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
        
        self.startThread()
        generateReport(self.scan_result)



    def threadtask(self ):
        
        while True != self.arrayThr.empty():
            temp = self.arrayThr.get()
            # temp est un tuple
            # temp[0] array de ips
            # temp[1] type de ips ipv4/6
            
            print("taille tuple",temp)
            if temp[1] == "ipv6":
                scan.doScanIp6(temp[0], self.scan_result)
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
                
                array.append(threading.Thread(target = self.threadtask, args=[]))
            for e in array:
                e.start()
                print("thread lancé")
            print("scan started")
            PourcentageFinished = 0
            while PourcentageFinished != 100:
               # print(self.scan_result)
                print("--- "  + str(PourcentageFinished) + " %  finished")
                time.sleep(1)
                PourcentageFinished = 0
                for k, v in self.scan_result.items():
                    if v["finished"] == True:
                        PourcentageFinished += 1
                PourcentageFinished =round(PourcentageFinished/len(self.scan_result.items()) *100)
                
                
            try:
                for host in self.scan_result:
                    
                    #print(self.scan_result[host]["res"]["scan"][host]["hostnames"][0]["name"])                
                    for sousHost in  self.scan_result[host]["res"]["scan"]:
                        print(sousHost + " is " + self.scan_result[host]["res"]["scan"][host]["status"]["state"])
                    
                          #    [host]["tcp"]:
                        #if self.scan_result[host]["res"]["scan"][host]["tcp"][port]["state"] == "open":
                         #   compteur+=1
                    #print("number open ports : " + str(compteur))
            except:
                print("error while reading scan results")  
            

    
       
        

