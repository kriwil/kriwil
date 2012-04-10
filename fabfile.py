from fabric.contrib.project import rsync_project


def push():
    local = "output/"
    remote = "/home/kriwil/webapps/kriwilcom/"
    rsync_project(remote, local, delete=True)
