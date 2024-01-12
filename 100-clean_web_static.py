#!/usr/bin/python3
# A Fabfile that is to delete the out-of-date archiveser.

import os

from fabric.api import *

env.hosts = ["52.91.137.7", "100.25.33.74"]


def do_clean(numbr=0):
    """Deleting all the out-of-date archiveser.
    Args:
        numbr (int): The numb of the archiveser thats to be kept.
    If numb 0 or 1,keep archive that are of most recent archive.
    If numb is 2, keeps only the top 2 most recent archiveser,
    etc.
    """

    numbr = max(1, int(numbr))
    archiveser = sorted(os.listdir("versions"))
    [archiveser.pop() for i in range(numbr)]
    with lcd("versions"):
        [local("rm ./{}".format(x)) for x in archiveser]

    with cd("/data/web_static/releases"):
        archiveser = run("ls -tr").split()
        archiveser = [x for x in archiveser if "web_static_" in x]
        [archiveser.pop() for i in range(numbr)]
        [run("rm -rf ./{}".format(x)) for x in archiveser]
