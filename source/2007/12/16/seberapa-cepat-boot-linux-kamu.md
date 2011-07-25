## Seberapa Cepat boot Linux Kamu?

Iseng kurang kerjaan. Dari [milis id-ubuntu](http://groups.google.com/group/id-ubuntu). Awalnya [ada yang menghitung waktu boot ubuntu-nya dengan menggunakan stopwatch](http://groups.google.com/group/id-ubuntu/msg/7c5f1cce7f1a308f). Kemudian [MDAMT](http://aksi.mdamt.net/) [memberikan sebuah link](http://groups.google.com/group/id-ubuntu/msg/1aef1beec5903fac) ke [Bootchart](http://bootchart.org/).

Diambil dari situsnya,

bq. Bootchart is a tool for performance analysis and visualization of the GNU/Linux boot process.

Dari situ kita bisa melihat seberapa cepat linux kita melakukan boot. Waktu yang dihitung cuma sampai sebelum xserver dijalankan, jadi waktu untuk menjalankan xserver tidak dihitung.

Di ubuntu (dan mungkin debian-based distro lainnya) cukup lakukan

<code>sudo apt-get install bootchart</code>

Kemudian restart komputernya. Nanti di folder 

<code>/var/log/bootchart/</code>

ada sebuah file png yang memvisualisasikan proses boot yang terjadi.

Tentunyaaa, kurang lengkap kalau saya tidak memberikan hasil boot saya sendiri, jadi silahkan diliat (klik gambar untuk hasil lebih lengkap).

Laptop (Intel Pentium M 1.6Ghz 1GB RAM):
[![laptop gutsy](http://kriwil.com/images/thumbnail-laptop-gutsy-20071216-1.png))](http://kriwil.com/images/laptop-gutsy-20071216-1.png)

Desktop (AMD X2 3600+ 2GB RAM):
[![desktop gutsy](http://kriwil.com/images/thumbnail-desktop-gutsy-20071216-1.png)](http://kriwil.com/images/desktop-gutsy-20071216-1.png)

*update*:
Sekarang datanya sudah ada di [wiki ubuntu-id](http://wiki.ubuntu-id.org). Silahkan menuju [http://wiki.ubuntu-id.org/SeaGamesUbuntu](http://wiki.ubuntu-id.org/SeaGamesUbuntu) untuk melihat langsung.

<!-- {"time": "2007-12-16 09:30:52", "title": "Seberapa Cepat boot Linux Kamu?"} -->
