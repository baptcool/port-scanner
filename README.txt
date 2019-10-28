#Baptiste M
#28/10/2019



Description :
    Scanner de port écrit en Python. Qui sort les resultats sous forme Html.
    Il est possible de scanner une ou plusieurs IP(s) ou de founir un fichier qui comprend une liste d IPs.
    Il est également possible de choisir le fichier d'output.



Attention :


    programme testé sous Debian avec nmap d'installé.
    programme testé avec python 2.7 et 3.7.3
    programme testé avec tout adresses IPV4 et cidr IPV4.
    
    ###############################################
    !! PROGRAMME A(non ascii) EXECUTER AVEC ROOT !!
    ###############################################

Installation :
    
    
    pip install python-nmap    (si python 2.7)
    pip3 install python-nmap   (si python 3 ) 
    
    Pour tester le bon fonctionnement du programme :
        python tests/test.py
        
        devrait retourner  : tout fonctionne
    

Utilisation :

    usage: main.py [-h] [--host HOST] [--hosts [HOSTS [HOSTS ...]]]
                   [--fileHosts FILEHOSTS] [--outputFile OUTPUTFILE]

    optional arguments:
      -h, --help            show this help message and exit
      --host HOST           one IP ipv4 / ipv6
      --hosts [HOSTS [HOSTS ...]]
                            multiple IPs ipv4 / ipv6
      --fileHosts FILEHOSTS
                            File containing the list of IPs
      --outputFile OUTPUTFILE
                            File containing the scan result
                            
                            
                            
                                               
                            
    fileHosts format :
        Une IP par ligne
        
        par exemple :
        
        192.168.1.25
        192.168.1.0/24
        192.168.1.49
        

Commandes possibles : 


    python main.py --fileHosts ip.txt 
    python3 main.py --fileHosts ip.txt
    python main.py --host 192.168.1.2
    python main.py --host 192.186.5.0/24
    python main.py --hosts 192.168.1.1 192.168.1.45 192.138.4.0/24 192.163.9.5
    
    python3 main.py --host 192.168.1.2 --outputFile out.html


    (ou)
    ./main.py --host 192.168.1.1    (si os = linux et droit fichier +x )


Normal output :

    └──╼ $python main.py --fileHosts ip.txt 
    scan started
    --- 0 %  finished
    --- 0.0 %  finished
    --- 0.0 %  finished
    --- 0.0 %  finished
    --- 0.0 %  finished
    ----------------------------------------------------
    Host : 192.168.1.49 (Mi9SE-Hamid)
    State : up
    ----------------------------------------------------
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    --- 33.0 %  finished
    ----------------------------------------------------
    Host : 192.168.1.28 ()
    State : up
    ----------------------------------------------------
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    --- 67.0 %  finished
    ----------------------------------------------------
    Host : 192.168.1.25 (Chromecast-Ultra)
    State : up
    ----------------------------------------------------
    192.168.1.25 is up
    192.168.1.49 is up
    192.168.1.28 is up 
