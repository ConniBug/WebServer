import urllib.request

def Connect():   
    url = 'https://Chat-Webserver--connorbilham1.repl.co/?connectionStat=Online&userID=1'
    try:
        req = urllib.request.Request(url)
        return(req)
    except urllib.error.HTTPError as e:
        print(e)

def Disconnect():   
    url = 'https://Chat-Webserver--connorbilham1.repl.co/?connectionStat=Offline'
    try:
        req = urllib.request.Request(url)
        return(req)
    except urllib.error.HTTPError as e:
        print(e)

def get_message():   
    url = 'https://Chat-Webserver--connorbilham1.repl.co/?message=null'
    try:
        req = urllib.request.Request(url)
        return(req)
    except urllib.error.HTTPError as e:
        print(e)

with urllib.request.urlopen(Connect()) as response:
    the_page = response.read()

    
with urllib.request.urlopen(get_message()) as response:
    the_page = response.read()
    print(the_page)

#with urllib.request.urlopen(Disconnect()) as response:
#    the_page = response.read()
