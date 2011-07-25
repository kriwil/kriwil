## Install Hackintosh

Akhirnya gue punya waktu untuk mencoba [hackintosh](http://en.wikipedia.org/wiki/OSx86) yang gue download. Alasan gue untuk mencoba install hackintosh ini adalah (selain kurang kerjaan tentu saja) untuk mengetahui kemampuan komputer (_bukan PC! PC is personal computer, fgs_) non Apple.

Spesifikasi komputer gue yang digunakan adalah

* AMD X2 3600+
* 2GB DDR SDRAM
* NVidia 7300GT 256MB
* ABIT KN9 motherboard
* 80GB IDE HD
* 250GB SATA HD

ISO hackintosh yang gue gunakan bernama _LawlessPPC-Leo-10.5.4-Phenom&AMD_, iso yang katanya dibuat khusus untuk pemilik _processor_ AMD.

Proses instalasinya sendiri berjalan tanpa hambatan sama sekali. Dengan mode standar, instalasi berhasil dan gak lama gue udah bisa login di OSXnya. Masalah baru timbul setelah masuk ke OSX. Resolusi layar maksimal cuma 1024x768, dan perangkat LAN gue tidak terdeteksi. Oiya, core cpu cuma terdeteksi satu, tapi itu gak penting buat gue.

Setelah melakukan investigasi melalui [database bumi](http://google.com) (menurut film [Meet Dave](http://www.imdb.com/title/tt0765476/)), ternyata perangkat LAN dengan chipset nforce kurang lancar di hackintosh. Kalau masalah resolusi, cuma perlu install nvinject dan semua beres.

Karena malas ngutak-ngatik gimana biar LAN-nya bekerja, gue akhirnya memasang kartu LAN PCI dlink dengan chipset realtek 8139 yang terbukti lancar di hackintosh. Benar saja, setelah dipasang, LAN langsung terdeteksi tanpa masalah.

Sampai saat ini, OSX berjalan tanpa masalah. Semua berjalan sesuai fungsinya (gue cuma menggunakan buat browsing, messaging, dan mendengarkan musik). Karena satu dan lain hal, gue belum tertarik menggunakan OSX sebagai OS utama. Mungkin di tulisan lain bakal dijabarkan kenapa.

Dan, selalu belum lengkap tanpa _skrinsyut_ ...

[![hackintosh - 01](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh01-t.png)](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh01.png)[![hackintosh - 02](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh02-t.png)](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh02.png)[![hackintosh - 03](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh03-t.png)](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh03.png)[![hackintosh - 04](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh04-t.png)](http://dl.getdropbox.com/u/112837/kriwil.com/image/hackintosh04.png)

<!-- {"time": "2008-12-25 12:00:01", "title": "Install Hackintosh"} -->
