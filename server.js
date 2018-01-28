var fs = require('fs');
var http = require('http');
var url = require('url');
var path = require('path');
var baseDirectory = __dirname;

var port = 1337;

var index = fs.readFileSync('index.html');

http.createServer(function (req, res) {

	if (req.url === '/' || req.url ==='/index.html') {
		res.writeHead(200, {'Content-Type': 'html'});
		res.end(index);
	}

	var requestUrl = url.parse(req.url);

	var fsPath = baseDirectory+path.normalize(requestUrl.pathname);

	var fileStream = fs.createReadStream(fsPath);
	fileStream.pipe(res)
	
	fileStream.on('open',function() {
		res.writeHead(200);
	});
	
	fileStream.on('error', function(e) {
		res.writeHead(404);
		res.end("Woah broskie, couldn't find that. \n\nError 404");
	});

}).listen(port);
console.log('Server running!');
