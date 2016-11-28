Title: Windows 10
date: 2016-11-28 10:00
slug: windows-10

![systeminfo](https://s3-ap-southeast-1.amazonaws.com/s.kriwil.com/www/0298-systeminfo_big_annotate.png "systeminfo")

_It's been two weeks since I'm using Windows 10 for work, so I guess I could
say something about it._

I've been wanting to try to do (web) development on Windows for a while. I know
this is weird, and sounds backward. But with [Bash on Ubuntu on Windows][windows-bash],
I had high hopes that I could finally have gaming machine and could still do
development on it.

The main reason I finally did this is I need to fix my work on IE/Edge. I usually
use [BrowserStack](https://www.browserstack.com/) for testing IE (I still do), but
it's very painful to use it for a long period of time. It requires a good upload
connection, and in Indonesia, "good" and "upload connection" don't go together
in one sentence. So when I had a hard drive lying around, I decided that it's
finally the time to install Windows 10. I won't go to OS installation details,
you'll find those kind of things easily in other places.

The first thing I tried after installing Windows is that bash-thing. I was so
exited that I could finally use real shell on Windows. Well it works. Sort of.
It's slow, and other than running some shell commands, it doesn't do much. I
can't even access the server I created using `python -m SimpleHTTPServer` command.
Probably I need to do some magic thing first. But it doesn't work when I tried
it, and I was disappointed.

Once I found out I can't access that simple HTTP server, I didn't even bother
to try full python web development setup. I immediately downloaded VirtualBox
and Vagrant and setup the environment there. Maybe I should write another
post focusing on development setup on Windows.

There aren't many things I missed when working on Windows. My daily applications
usages revolve around browser, IDE, terminal, todo manager, email client, notes
taking application. From those list, I miss terminal and todo manager.

Even I mainly use Safari, I do use Chrome for development, so that's not a problem.
And with Chrome's sync, I don't even see any difference. All the bookmarks and
extensions are there. I do miss [1password's auto fill][1password-autofill], and
sometimes it hits me hard.

Powerful terminal (and shell) is probably the main reason why development on linux
or OSX is better if you're not developing for Windows platform. Yes Windows now
have PowerShell, and yes maybe it's good, but I doubt it's better.

Now, the good thing about Windows. [Steam][steam]. Games on Steam to be exact.
Yes you could install Steam on linux or OSX, but there are lots of games that only
work on Windows. And I've been enjoying games again. I don't always play games,
but it's nice to have them ready when I want to.

So, yeah, I guess Windows will mainly be a gaming system for me. I still hope the
bash will works flawlessly in the future. In fact, I just turned the Insider Preview
on so I could get faster updates, hoping there are more updates to the bash.

_I'm writing this on Windows, and will build this on bash (I'm using [pelican][Pelican]),
so if you see this paragraph, it means it's a success._

[windows-bash]: https://msdn.microsoft.com/en-us/commandline/wsl/about
[1password-autofill]: https://discussions.agilebits.com/discussion/5007/auto-fill-in-windows
[steam]: http://store.steampowered.com/
[pelican]: https://github.com/getpelican/pelican
