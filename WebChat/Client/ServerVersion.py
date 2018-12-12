import urllib.request
  
#def send_message(message):
#req = urllib.request.Request(url)
    #return(req)

url = 'https://Chat-Webserver--connorbilham1.repl.co/?versionnumbe

try:
    req = urllib.request.Request(url)
except all as e:
    print("Error")
    print(e)
    print("Report bug with what you were doing when message was sent and the error")    
    
try:
    urllib.request.urlopen(req)
except all as e:
    print("Error")
    print(e)
    print("Report bug with what you were doing when message was sent and the error")    

