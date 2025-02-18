#!/usr/bin/python3
"""creates an archive from web_static"""

from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """
    generate tgz archive using fabric
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions") is False:
        local(" mkdir versions")
    local('tar -cvzf ' + file_path + ' web_static')
    if os.path.exists(file_path):
        return file_path
    return None
