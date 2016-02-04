//First Javascript Code
//Reading Contents of a file



var http=require('http');
var express=require('express');
var app = express();
app.use(function(req, res, next){
  res.header("Access-Control-Allow-Origin", "*");		
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();	



});
app.use('/',express.static(__dirname+'/'));

app.get('/', function(request, response)
{
	response.sendFile(__dirname + '/HelloPlant.html');
});

var port=8000;

http.createServer(app).listen(port);
