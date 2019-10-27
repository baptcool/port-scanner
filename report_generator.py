

def ecritureFichier(htmlText):
    try:        
        FileReport = open("Report.html","w")
        FileReport.write(" ".join(htmlText))
        FileReport.close()
    except IOError:
        print("error while writing scan repport")

def generateReport(result):
    head = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\"><html xmlns=\"http://www.w3.org/1999/xhtml\"xml:lang=\"en\" lang=\"en\"><head><meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />  <title>Scan Report</title> </head><body>"
    bottom = "	<br>	<br>	<hr>	<br>	<br></body></html>"
    templateMachine = "<p>	<h3>Nmap scan report for NameMachine (IpMachine)</h3>	<p>Host is MachineState</p>	<p>PORT      STATE SERVICE VERSION</p>	<ul>	#ici	</ul></p>"
    templatePortText = "<li>PortNumber     PortState  PortService PortServiceVersion</li>"
    

    #print(result)
    
    htmlText = list()
    htmlText.append(head)
    
    
    try:
        for host in result:

            #print(self.scan_result[host]["res"]["scan"][host]["hostnames"][0]["name"])                
            for sousHost in  result[host]["res"]["scan"]:
                #print(sousHost + " is " + result[host]["res"]["scan"][sousHost]["status"]["state"])
                temptemplateMachine = templateMachine.replace("NameMachine", result[host]["res"]["scan"][sousHost]["hostnames"][0]["name"]+" "+result[host]["res"]["scan"][sousHost]["hostnames"][0]["type"] )
                temptemplateMachine = temptemplateMachine.replace("IpMachine", sousHost)
                temptemplateMachine = temptemplateMachine.replace("MachineState",result[host]["res"]["scan"][sousHost]["status"]["state"])
                
                for port in result[host]["res"]["scan"][sousHost]["tcp"]:                    
                    temptemplatePortText = templatePortText.replace("PortNumber",str(port))
                    temptemplatePortText=temptemplatePortText.replace("PortState",result[host]["res"]["scan"][sousHost]["tcp"][port]["state"])
                    temptemplatePortText=temptemplatePortText.replace("PortService",result[host]["res"]["scan"][sousHost]["tcp"][port]["name"] + " " +result[host]["res"]["scan"][sousHost]["tcp"][port]["product"])
                    temptemplatePortText=temptemplatePortText.replace("PortServiceVersion",result[host]["res"]["scan"][sousHost]["tcp"][port]["version"]+" "+result[host]["res"]["scan"][sousHost]["tcp"][port]["extrainfo"])
                    temptemplateMachine = temptemplateMachine.replace("#ici	", temptemplatePortText + "#ici	")
              #    [host]["tcp"]:
            #if self.scan_result[host]["res"]["scan"][host]["tcp"][port]["state"] == "open":
             #   compteur+=1
            #print("number open ports : " + str(compteur))
    except Exception as ex:
        print("error while reading scan results")      
        print(ex)


    htmlText.append(bottom)
    ecritureFichier(htmlText)
    


