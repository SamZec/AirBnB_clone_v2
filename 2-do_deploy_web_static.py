#!/usr/bin/python3
"""distributes archive to servers"""

from fabric.api import local, env
from datetime import datetime
from pathlib import Path
from fabric.operations import run, put
import os
from fabric.contrib import files

time = datetime.now()
year = time.strftime("%Y")
month = time.month
day = time.day
hour = time.hour
minute = time.minute
second = time.second
filename = "web_static_{}{}{}{}{}{}".format(year, month,
                                            day, hour, minute, second)
command = "tar -cvzf versions/{}.tgz web_static".format(filename)

env.hosts = ['ubuntu@52.201.222.10', 'ubuntu@34.232.70.226']
env.key_filename = "~/.ssh/id_rsa.pub"
file_path = "versions/" + filename + ".tgz"


def do_pack():
    """creates an archive"""
    local("mkdir -p versions")
    local(command)
    my_file = Path("versions/{}.tgz".format(filename))
    if my_file.is_file():
        return "versions/{}.tgz".format(filename)
    else:
        return None


def do_deploy(archive_path):
    """deploys archive to server"""
    if not os.path.isfile(archive_path):
        return False
    filename = archive_path.split("/")[1]
    name_ext = filename.split(".")[0]
    try:
        # Puts archive on server
        put(archive_path, '/tmp/')
        # Makes directory
        if not files.exists('/data/web_static/releases/{}'.format(name_ext)):
            run('sudo mkdir -p /data/web_static/releases/{}'.format(name_ext))
        # Uncompresses archive
        run('sudo tar -xvf\
                /tmp/{}.tgz -C\
                /data/web_static/releases/{}'.format(name_ext, name_no_ext))
        # remove tgz file from temp
        run('sudo rm /tmp/{}.tgz'.format(name_no_ext))
        # move file to proper location
        run('sudo mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}/'.format(name_no_ext, name_ext))
        run('sudo rm -rf\
                /data/web_static/releases/{}/web_static'.format(name_ext))
        # Remove old symlink
        if files.exists('/data/web_static/current'):
            run('sudo rm -rf /data/web_static/current')
        # Create new symlink
        run('sudo ln -s\
                /data/web_static/releases/{}\
                /data/web_static/current'.format(name_no_ext))
        print("New version deployed!")
        return True
    except Exception:
        return False
