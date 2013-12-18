---
layout: post
title: How to install node.js in debian linux
description: ""
modified: 2013-12-17
category: articles
tags: [node.js, debian, how-to, install, introduce]
comments: true
---

Node.js is a platform built on Google javascript V8 runtime for easily building fast, scalable network applications. Node.js uses an event-driven, non-blocking I/O model, so it is really lightweight and efficient. Node.js could be used in real-time applications without more CPU computer scene.

## Where we could find the Node.js
* running this command: **wget -N http://nodejs.org/dist/node-latest.tar.gz**

* or goto official website: [http://nodejs.org/](http://nodejs.org/)
you can download the Node.js development package.

* and also you can go to github.com: [https://github.com/joyent/node](https://github.com/joyent/node)
{% highlight css %}
git clone https://github.com/joyent/node.git
{% endhighlight %}


### How to install Node.js
* When you first installed the Debian Linux System, you need to running this command:
**aptitude install build-essential python g++ make checkinstall**

if you not sure whether it could be find or not, maybe you need running this command:
**aptitude search essential**

{% highlight css %}
root@debian:~# aptitude search essential
i   build-essential                 - Informational list of build-essential pack
p   glassfish-toplink-essentials    - Open source Java EE 5 Application Server
root@debian:~# aptitude install build-essential
{% endhighlight %}

* I have already created a file folder in my root directory, which name is **bin**, and I download the node-latest.tar file in this folder,
and then running this command:**tar xzvf node-latest.tar**, then you can find node-v0.10.23 folder.

{% highlight css %}
root@debian:~/bin# ls
go1.2.linux-amd64.tar.gz  jdk-6u45-linux-x64.bin  node-latest.tar
goagent-0369625           jetty-6.1.26            node-v0.10.23

root@debian:~/bin/node-v0.10.23# ls
AUTHORS                           configure        node
backup-121320130050-pre-node.tgz  CONTRIBUTING.md  node_0.10.23-1_amd64.deb
backup-121320130052-pre-node.tgz  deps             node.gyp
benchmark                         description-pak  out
BSDmakefile                       doc              README.md
ChangeLog                         doc-pak          src
common.gypi                       lib              test
config.gypi                       LICENSE          tools
config.mk                         Makefile         vcbuild.bat
{% endhighlight %}

* Finally, running this command:
please attention: when you running **./configure** command, the system will talk about, please provide a version of node.js,
the default value is V0.10.23, please modify 0.10.23 by yourself, so you could running **checkinstall** better. 
if you can't modify, it will be running error.

{% highlight css %}
./configure
checkinstall
sudo dpkg -i node_*
{% endhighlight %}

* So let me summarize:
{% highlight css %}
aptitude install build-essential python g++ make checkinstall
mkdir ~/bin && cd $_
wget -N http://nodejs.org/dist/node-latest.tar.gz
tar xzvf node-latest.tar.gz && cd node-v*
./configure
checkinstall
dpkg -i node_0.10.23-1_amd64.deb
{% endhighlight %}

* * * * * *
<div class="sample_footer">
Copyright &copy; 2013 Want-To-Be-BigHack by ericssonxiao
</div>