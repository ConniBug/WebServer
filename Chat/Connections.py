import urllib.request

def Disconnect():   
    url = 'https://Chat-Webserver--connorbilham1.repl.co/?connectionStat=Offline'
    try:
        req = urllib.request.Request(url)
        return(req)
    except urllib.error.HTTPError as e:
        print(e)

def get_connections():   
    url = 'https://Chat-Webserver--connorbilham1.repl.co/?getConnections=Yes'
    try:
        req = urllib.request.Request(url)
        return(req)
    except urllib.error.HTTPError as e:
        print(e)

with urllib.request.urlopen(get_connections()) as response:
    the_page = response.read()
    print(the_page)

with urllib.request.urlopen(Disconnect()) as response:
    the_page = response.read()
