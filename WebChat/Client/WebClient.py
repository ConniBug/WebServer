import urllib.request
  
message = "null"
#def send_message(message):
#req = urllib.request.Request(url)
    #return(req)


#send_message(input("Message: "))

User = str(open("User.txt","r+").read()+"-|")

message = input("Message: ")
url = 'https://Chat-Webserver--connorbilham1.repl.co/?message=' + User + message

print("Sending 1/3")
try:
    req = urllib.request.Request(url)
except all as e:
    print("Error")
    print(e)
    print("Report bug with what you were doing when message was sent and the error")    
    
print("Sending 2/3")
try:
    urllib.request.urlopen(req)
except all as e:
    print("Error")
    print(e)
    print("Report bug with what you were doing when message was sent and the error")    

print("Sending 3/3")
print("")
