Title: How To Download Firefox Without IE
Date: 2009-06-15 00:00:13
Slug: how-to-download-firefox-without-ie

[European won't get Internet Explorer (IE) in Windows 7](http://news.bbc.co.uk/2/hi/technology/8096701.stm). So, how could we [download](http://www.ixibo.com/2009/03/5-reasons-why-people-use-internet-explorer/) Mozilla Firefox?

Use FTP. Seriously.

1. Type <code>ftp releases.mozilla.org</code> in Run window (Start -> Run), then click OK
2. enter <code>anonymous</code> as username, and your email address as password
3. Once verified, type <code>cd pub/mozilla.org/firefox/releases/latest/win32</code>
4. By default, you want to type <code>cd en-US</code>. If you want to use other language, type <code>ls</code> and pick any language you want
5. Type <code>ls</code> to see the latest firefox release. You're looking for a filename with <code>.exe</code> in the end. Right now it's <code>Firefox Setup 3.0.11.exe</code>
6. You might want to type <code>lcd Desktop</code> to change your local directory to desktop, so the file you're going to download will be put there
6. Type <code>binary</code> to make sure you'll get binary file
6. Now, type the file, <code>get "Firefox Setup 3.0.11.exe"</code>
7. Wait until it's finished, then type <code>quit</code>
8. Install firefox, and have fun!

_credit to [boutell.com](http://www.boutell.com/newfaq/browser/installfirefoxwithoutie.html)_