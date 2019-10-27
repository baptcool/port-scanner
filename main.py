from get_parameters import get_user_parameters
import os
import argparse
import logging
from  scan_manager import Scan_Manager
from logger import Logger



if __name__ == "__main__":

    adressesipv4, adressesipv6 = get_user_parameters()
    multiTreadActive = 1
    nombrethread = 100
    Scan_Manager(multiTreadActive,nombrethread,adressesipv4,adressesipv6)

    
