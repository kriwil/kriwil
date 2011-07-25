## gentoo: patching source before emerge

Penting nih, baru belajar [gentoo](http://gentoo.org) soalnya. Patch source code sebelum diinstall.

	# ebuild myebuild fetch (if you don't have it in distfiles)
	# ebuild myebuild unpack (unpacked to /var/tmp/portage/packagename/something)
	# ebuild myebuild compile
	# ebuild myebuild install
	# ebuild myebuild qmerge

Catatan:
`myebuild` merupakan path ke `/usr/portage/blabla/appname/app.ebuild`

<!-- {"time": "2008-07-11 02:36:48", "title": "gentoo: patching source before emerge"} -->
