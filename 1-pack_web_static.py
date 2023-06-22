#!/usr/bin/python3
"""creates an archive from web_static"""

from fabric.api import local
from datetime import datetime
from pathlib import Path

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


def do_pack():
    """creates an archive"""
    local("mkdir -p versions")
    local(command)
    my_file = Path("versions/{}.tgz".format(filename))
    if my_file.is_file():
        return "versions/{}.tgz".format(filename)
    else:
        return None
