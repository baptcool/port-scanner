from get_parameters import get_user_parameters
import os
import argparse

from  scan_manager import Scan_Manager




if __name__ == "__main__":

    adressesipv4, adressesipv6 = get_user_parameters() # récupération des tableaux des ips v4 et v6
    multiTreadActive = 1 # activation ou non du multi threading 
    nombrethread = 100 # 100 threads max. 1 thread par scan.
    Scan_Manager(multiTreadActive,nombrethread,adressesipv4,adressesipv6) 

    
