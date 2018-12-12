import urllib.request

def get_version():   
    url = 'https://Chat-Webserver--connorbilham1.repl.co/?versionnumber'
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
