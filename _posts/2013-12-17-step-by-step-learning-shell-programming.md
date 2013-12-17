---
layout: post
title: Step by step learning shell programming
description: ""
modified: 2013-12-17
category: articles
tags: [step by step, shell, introduce, linux]
image:
  feature: so-simple-sample-image-5.jpg
  credit: Michael Rose
  creditlink: http://mademistakes.com
comments: true
---

First of all , let's understand what is shell from a picture.

![Linux Image]({{ site.url }}/images/shell01.png)
{: .pull-centre}

1. **Shell**: A Command-Line Interpretor that connects a user to **Operating System** and allows to execute the commands or by creating text script.
2. **Process**: Any task that a user run in the system is called a process. A process is little more complex than just a task.
Unix philosophy:  Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

3. **Bourne shell** : The Bourne shell was one of the major shells used in early versions and became a de facto standard. It was written by **Stephen Bourne** at **Bell Labs**. Every Unix-like system has at least one shell compatible with the Bourne shell. The Bourne shell program name is “**sh**” and it is typically located in the file system hierarchy at **/bin/sh**.

## Basics of Shell Programming
1. To get a Linux shell, you need to start a terminal.
2. To see what shell you have, **run: echo $SHELL**.
3. In Linux, the dollar sign (**$**) stands for a shell variable.
4. The ‘**echo**‘ command just returns whatever you type in.
5. The pipeline instruction comes to rescue, when chaining several commands.
6. Linux commands have their own syntax, Linux won’t forgive you whatsoever is the mistakes. If you get a command wrong, you won’t flunk or damage anything, but it won’t work.
7. **#!/usr/bin/env bash** – It is called shell. It is written at the top of a shell script and it passes the instruction to the program **/bin/sh**.

### Process of writing and executing a script
1. Open terminal.
2. Navigate to the place where you want to create script using ‘cd‘ command.
3. Cd (enter) [This will bring the prompt at Your home Directory].
4. touch hello.sh (Here we named the script as hello, remember the ‘.sh‘ extension is compulsory).
5. vi hello.sh (nano hello.sh) [You can use your favourite editor, to edit the script].
6. chmod 744 hello.sh (making the script executable).
7. sh hello.sh or ./hello.sh (running the script)

#### Let's see your first shell script.
1. hello.sh
{% highlight css %}
#!/usr/bin/env bash
# hello.sh
set -eo pipefail
echo "Hello World!"
{% endhighlight %}

**Sample Output:**
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ ./hello.sh
Hello World!
{% endhighlight %}

2. show_process.sh
{% highlight css %}
#!/usr/bin/env bash
# show process.sh
set -eo pipefail
echo "hello $USER"
echo "I'm " $USER " and will be telling you about the current process"
echo "Running Process List"
ps -aux
{% endhighlight %}

**Sample Output:**
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ ./show_process.sh
hello ericssonxiao
I'm  ericssonxiao  and will be telling you about the current process
Running Process List
Warning: bad ps syntax, perhaps a bogus '-'? See http://procps.sf.net/faq.html
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.3   3536  1956 ?        Ss   17:33   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    17:33   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    17:33   0:00 [ksoftirqd/0]
root         6  0.0  0.0      0     0 ?        S    17:33   0:00 [migration/0]
root         7  0.0  0.0      0     0 ?        S    17:33   0:00 [watchdog/0]
root         8  0.0  0.0      0     0 ?        S<   17:33   0:00 [cpuset]
root         9  0.0  0.0      0     0 ?        S<   17:33   0:00 [khelper]
root        10  0.0  0.0      0     0 ?        S    17:33   0:00 [kdevtmpfs]
root        11  0.0  0.0      0     0 ?        S<   17:33   0:00 [netns]
root        12  0.0  0.0      0     0 ?        S    17:33   0:00 [sync_supers]
root        13  0.0  0.0      0     0 ?        S    17:33   0:00 [bdi-default]
root        14  0.0  0.0      0     0 ?        S<   17:33   0:00 [kintegrityd]
{% endhighlight %}

3. interactive.sh
{% highlight css %}
#!/usr/bin/env bash
# interactive.sh
set -eo pipefail
echo "Hey what's your first name?";
read a;
echo "wlcome Mr./Mrs. $a, would you like to tell us, your last name";
read b;
echo "Thanks Mr./Mrs. $a $b for telling us your name";
echo "****************************************************";
echo "Mr./Mrs. $b, it's time to say you good bye";
{% endhighlight %}

**Sample Output:**
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ ./interactive.sh
Hey what's your first name?
eric
wlcome Mr./Mrs. eric, would you like to tell us, your last name
xiao
Thanks Mr./Mrs. eric xiao for telling us your name
****************************************************
Mr./Mrs. xiao, it's time to say you good bye
{% endhighlight %}

4. shell track options，using **set**
{% highlight css %}
set -ex 
set -eo pipefail
{% endhighlight %}
using **set -x** could produce many info, so you can use **echo** or **print** for trace.
 
5. **Script 001:**
{% highlight css %}
#!/usr/bin/env bash
# this is simple test for set command
# set -eo pipefail
set -xe
echo -n "can you write device drivers?"
read answer
answer='echo $answer | tr [a-z] [A-Z]'
if [ $answer = Y ]
then
    echo "wow,you must be very skilled"
else
    echo "Neither can i, i'm just an example shell script"
fi
{% endhighlight %}

**Sample Output:**
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ ./ex2.sh
+ echo -n 'can you write device drivers?'
can you write device drivers?+ read answer
eric
+ answer='echo $answer | tr [a-z] [A-Z]'
+ '[' echo '$answer' '|' tr '[a-z]' '[A-Z]' = Y ']'
./ex2.sh: line 8: [: too many arguments
+ echo 'Neither can i, i'\''m just an example shell script'
Neither can i, i'm just an example shell script
{% endhighlight %}

**Sample Output:**
use bash --debug command:
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ bash --debug ex2.sh
bash --debug ex2.sh
can you write device drivers?y
ex2.sh: line 8: [: too many arguments
Neither can i, i'm just an example shell script
{% endhighlight %}

**Sample Output:**
use bash --verbose command:
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ bash --verbose ex2.sh
bash --verbose ex2.sh
#!/usr/bin/env bash
# this is simple test for set command
#set -eo pipefail
#set -xe
echo -n "can you write device drivers?"
can you write device drivers?read answer
y
answer='echo $answer | tr [a-z] [A-Z]'
if [ $answer = Y ]
then
    echo "wow,you must be very skilled"
else
    echo "Neither can i, i'm just an example shell script"
fi
ex2.sh: line 8: [: too many arguments
Neither can i, i'm just an example shell script
{% endhighlight %}

6. **Script 002:**
{% highlight css %}
#!/usr/bin/env bash
# hello world
set -ex
VAR="Hello World!"
function changeVar {
local VAR="local var"
echo $VAR
}
echo $VAR
changeVar
echo $VAR
{% endhighlight %}

**Sample Output:**
{% highlight css %}
ericssonxiao@ubuntu:~/workspace/shell$ ./ex1.sh
+ VAR='Hello World!'
+ echo Hello 'World!'
Hello World!
+ changeVar
+ local 'VAR=local var'
+ echo local var
local var
+ echo Hello 'World!'
Hello World!
{% endhighlight %}

Enjoy!

**Related Web Resources**

* [Learning Shell Scripting Language: A Guide from Newbies to System Administrator](http://www.tecmint.com/learning-shell-scripting-language-a-guide-from-newbies-to-system-administrator/)
* [Understand Linux Shell and Basic Shell Scripting Language Tips – Part I](http://www.tecmint.com/understand-linux-shell-and-basic-shell-scripting-language-tips/)
* [Learning Debian GNU/Linux](http://oreilly.com/openbook/debian/book/ch13_03.html)
* [Learning Red Hat Linux, 2nd Edition Learning Red Hat Linux, 2nd Edition](http://oreilly.com/catalog/redhat2/chapter/ch13.html)
* [bash shell programming in one hour](http://benpfaff.org/writings/shell/shell.pdf)
* [Output Hollywood-hacker-scene from a shell](http://unix.stackexchange.com/questions/21347/output-hollywood-hacker-scene-from-a-shell)
* [stackexchange questions](http://unix.stackexchange.com/questions)
* [Bash shell-scripting libraries](http://dberkholz.com/2011/04/07/bash-shell-scripting-libraries/)
* [log4sh version 1.4.2](http://svn.code.sf.net/p/log4sh/svn/trunk/source/1.4/doc/log4sh.html#id2479858)
* [shell_book_blinn](http://www.cs.uleth.ca/~holzmann/C/shells/shell_book_blinn/)
* [Wicked Cool Shell Scripts: The Library](http://intuitive.com/wicked/wicked-cool-shell-script-library.shtml)
* [shell lib](http://www.vxdev.com/docs/vx55man/vxworks/ref/shellLib.html)

* * * * * *
<div class="sample_footer">
Copyright &copy; 2013 Want-To-Be-BigHack by ericssonxiao
</div>