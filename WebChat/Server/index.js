var fs = require('fs');

const express = require('express');

const app = express();

app.get('/', function(request, response) {      

    contents = fs.readFileSync('log.txt', 'utf8');
    //console.log(contents);
    var messages = contents;
    
    if(request.query.getConnections == "Yes"){
      //current = fs.readFileSync('ActiveConnections.txt', 'utf8');
      var current = 0
      //response.send(current);
      console.log("Current: " + current);
      if(fs.readFileSync('u1.txt','utf8') == "1"){
        current = current + 1;
      }
      if(fs.readFileSync('u2.txt','utf8') == "1"){
        current = current + 1;
      }
      if(fs.readFileSync('u3.txt','utf8') == "1"){
        current = current + 1;
      }
      response.send(current.toString());
    }

    if(request.query.connectionStat == "Online"){
      console.log("NewConnection");
      var count = 0; 
      
      if(request.query.userID == "1"){
        fs.writeFileSync('u1.txt', "1");
      }
      if(request.query.userID == "2"){
        fs.writeFileSync('u2.txt', "1");
      }
      if(request.query.userID == "3"){
        fs.writeFileSync('u3.txt', "1");
      }

      response.send("");
    }

    //Not Efficiant Remove Number: 1
    //if(request.query.connectionStat == "Offline"){
    //  fs.unlinkSync('ActiveConnections.txt');
    //  var createStream = fs.createWriteStream("ActiveConnections.txt");
    //  createStream.end();
    //  response.send("");
    //}

    if(request.query.message == 'null'){
      console.log("Get Message Request");
      response.send(messages);
      console.log("-------------------");
    } else { 
        if(request.query.message){
          console.log("Send Message       ");
          console.log(request.query.message);
          fs.writeFileSync('log.txt', request.query.message);
          console.log("-------------------");
          response.send();
        }
    }
    //response.send("");
});


app.listen(3000, () => {
  console.log('server started');
});
