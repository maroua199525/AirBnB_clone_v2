#!/usr/bin/python3
""" Module fabric.api that generates a .tgz
archive from the contents of the web_static folder of your AirBnB Clone repo"""


from fabric.api import task, local

@task
def do_pack():
    run("mkdir -p versions")

