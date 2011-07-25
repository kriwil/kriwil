## Gak Bisa Mount NTFS External Drive

Pernah gak bisa mount hard disk external yang menggunakan NTFS di linux? Biasanya terjadi karena pas di windows kita gak umount/disconnect/unplug drive itu terlebih dahulu sebelum mematikan/restart komputer.

Cara paling logis adalah restart ke windows trus umount/disconnect/unplug drive itu dulu, trus balik lagi ke linux. Tapi jadi ribet dong yah. Yang benar itu pakai perintah `ntfsfix`.

    ntfsfix <device>

Misal kalau device external kita ada di `/dev/sdb1`,

    ntfsfix /dev/sdb1

Semoga bisa membantu.

<!-- {"time": "2008-04-01 16:27:43", "title": "Gak Bisa Mount NTFS External Drive"} -->
