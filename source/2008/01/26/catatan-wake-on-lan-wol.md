## Catatan: Wake On LAN (WOL)

Buat catatan aja, soalnya suka lupa kalau abis install ulang komputer. Dan juga buat bagi-bagi ilmu kalau yang belum tau.

bq. Wake on LAN (WOL, sometimes WoL) is an Ethernet computer networking standard that allows a shut-down computer to be booted remotely. (dari [wikipedia](http://en.wikipedia.org/wiki/Wake-on-LAN))

Jadi, fungsinya itu biar kita bisa menyalakan komputer secara _remote_. Hal ini berguna buat orang-orang seperti gue yang meletakkan data di komputer terpisah di dalam satu jaringan, dan ingin mengakses sewaktu-waktu, tetapi tidak ingin membiarkan komputernya nyala terus.

Syarat pertama dari menggunakan fitur Wake On LAN ini adalah dukungan dari ethernet card (dan motherboard? gak tau juga sih) komputer yang akan "dibangunkan". Cara taunya liat di BIOS, dan cari tulisan yang mirip-mirip Wake on LAN. Aktifkan jika belum aktif.

Kemudian, kita harus tau nama perangkat jaringan (_network device_) yang akan digunakan. Di terminal, ketikkan

`ifconfig`

Hasil di komputer saya seperti ini:

    eth0      Link encap:Ethernet  HWaddr 00:50:8D:9D:D1:84  
    inet addr:10.0.0.6  Bcast:255.255.255.255  Mask:255.255.255.0
    inet6 addr: fe80::250:8dff:fe9d:d184/64 Scope:Link
    UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
    RX packets:166 errors:0 dropped:0 overruns:0 frame:0
    TX packets:118 errors:0 dropped:0 overruns:0 carrier:0
    collisions:0 txqueuelen:1000 
    RX bytes:20233 (19.7 KB)  TX bytes:84689 (82.7 KB)
    Interrupt:16 

    lo        Link encap:Local Loopback  
    inet addr:127.0.0.1  Mask:255.0.0.0
    inet6 addr: ::1/128 Scope:Host
    UP LOOPBACK RUNNING  MTU:16436  Metric:1
    RX packets:0 errors:0 dropped:0 overruns:0 frame:0
    TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
    collisions:0 txqueuelen:0 
    RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)

Perangkat yang akan saya gunakan adalah `eth0`. Catat (dan maksud catat di sini adalah copy - paste ke text editor, gak usah ambil kertas dan pensil) _hardware address_ perangkat bersangkutan, punya saya adalah `00:50:8D:9D:D1:84`.

Setelah kita mengetahui jenis perangkat yang digunakan, sekarang kita perlu membuat skrip yang akan mengaktifkan opsi WOL di ethernet kita setiap kali komputer dinyalakan. Di terminal, ketikkan

`sudo vi /etc/init.d/wakeonlanconfig`

`vi` bisa diganti dengan editor kesayangan masing-masing, gedit, pico, nano, whatever.

Lalu copy - paste tulisan di bawah ini dan simpan lalu keluar dari editor.

pre. #!/bin/bash
ethtool -s eth0 wol g
exit

Kemudian kita perlu membuat skrip yang kita buat menjadi _executable_

`sudo chmod a+x /etc/init.d/wakeonlanconfig`

Dan membuat skrip yang kita buat jalan saat komputer dinyalakan

`sudo update-rc.d -f wakeonlanconfig defaults`

Pengaturan di komputer tujuan (yang akan "dibangunkan") sudah selesai. Untuk memastikan, bisa dicoba jalankan

`sudo /etc/init.d/wakeonlanconfig`

Jika tidak ada error, berarti kita bisa mematikan komputer.

`sudo halt` atau `sudo shutdown -h now`

Sekarang beralih ke komputer yang akan "membangunkan" komputer tadi. Pertama-tama kita harus memasang paket wakeonlan. Jika menggunakan ubuntu, aktifkan repositori _universe_ dan lakukan

`sudo apt-get install wakeonlan`

Setelah selesai, jalankan perintah `wakeonlan` ditambah _hardware address_ komputer yang akan dibangunkan tadi. Kalau punya saya jadi

`wakeonlan 00:50:8D:9D:D1:84`

Tunggu beberapa saat, dan komputer bisa diakses ;)

_(diambil secara brutal dari [HOWTO: Set your system up for Wake On LAN (WOL)](http://ubuntuforums.org/showthread.php?t=234588))_

<!-- {"time": "2008-01-26 20:38:38", "title": "Catatan: Wake On LAN (WOL)"} -->
