example = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
hdr = {'User-Agent':'Mozilla/5.0'}
# PhishTank
key = "da820fcce696964f5723c8e40a26470bb8b9c0d66af733e74665953b35db0b95"
request_link = "http://data.phishtank.com/data/"+key+"/online-valid.xml"

# Feodo(IP)
req_link_1 = "https://feodotracker.abuse.ch/blocklist/?download=ipblocklist"

# ZeusTracker(domain)
req_link_2 = "https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist"

# Ransomware Domain Blocklist(Domain)
req_link_3 = "https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt"

#BlackHole(IP)
req_link_4 = "http://malc0de.com/bl/IP_Blacklist.txt"

#MalwareDomain(domain)
req_link_5 = "http://mirror2.malwaredomains.com/files/domains.txt"