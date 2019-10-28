import os
import argparse
import logging
from logger import Logger
import re
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def get_user_parameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="one IP  ipv4 / ipv6 ", type=str)
    parser.add_argument("--hosts",nargs='*', help="multiple IPs ipv4 / ipv6", type=str)
    parser.add_argument("--fileHosts", help="File containing the list of IPs", type=str)

    args = parser.parse_args()
    adressesipv4 = []
    adressesipv6 = []
    cidrs = []
    if args.host != None:
        insertionAdresse(args.host,adressesipv4,adressesipv6 )
        #ici cidrs
    elif args.hosts != None:
        for adresse in args.hosts:
            insertionAdresse(adresse,adressesipv4,adressesipv6)
            #ici cidrs
    elif args.fileHosts != None:
        try:
            file = open(args.fileHosts)
            content = file.readlines()
            file.close()

            for line in content:
                insertionAdresse(line.rstrip("\n\r"),adressesipv4,adressesipv6)
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur d\'ouverture.')
    else:
        print("--help to see usage")
        exit()
    return adressesipv4, adressesipv6




def insertionAdresse(adress,adressesipv4,adressesipv6):
    if re.match(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", adress) != None:
        adressesipv4.append(adress);
    if re.match(r"(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))", adress) != None:
        adressesipv6.append(adress);


