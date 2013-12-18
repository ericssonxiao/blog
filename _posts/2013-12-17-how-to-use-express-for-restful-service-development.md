---
layout: post
title: How to use express for restful service development
description: ""
modified: 2013-12-17
category: articles
tags: [node.js, express, restful, service, introduce, how-to]
comments: true
---

## Firstly, let me write "Hello World" web server
This simple web server written in Node responds with "Hello World" for every request.
{% highlight css %}
var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World\n');
}).listen(1337, '127.0.0.1');
console.log('Server running at http://127.0.0.1:1337/');
{% endhighlight %}
To run the server, put the code into a file example.js and execute it with the node program from the command line:

% node example.js
Server running at http://127.0.0.1:1337/
Here is an example of a simple TCP server which listens on port 1337 and echoes whatever you send it:
{% highlight css %}
var net = require('net');

var server = net.createServer(function (socket) {
  socket.write('Echo server\r\n');
  socket.pipe(socket);
});

server.listen(1337, '127.0.0.1');
{% endhighlight %}

### How to install express
{% highlight css %}
root@debian:~# npm install -g express
...
/usr/local/bin/express -> /usr/local/lib/node_modules/express/bin/express
express@3.4.7 /usr/local/lib/node_modules/express
├── methods@0.1.0
├── merge-descriptors@0.0.1
├── cookie-signature@1.0.1
├── range-parser@0.0.4
├── buffer-crc32@0.2.1
├── fresh@0.2.0
├── debug@0.7.4
├── cookie@0.1.0
├── mkdirp@0.3.5
├── commander@1.3.2 (keypress@0.1.0)
├── send@0.1.4 (mime@1.2.11)
1.1 ─ connect@2.12.0 (uid2@0.0.3, pause@0.0.1, qs@0.6.6, bytes@0.2.1, raw-body@
.2, batch@0.5.0, negotiator@0.3.0, multiparty@2.2.0)
{% endhighlight %}

* * * * * *
<div class="sample_footer">
Copyright &copy; 2013 Want-To-Be-BigHack by ericssonxiao
</div>